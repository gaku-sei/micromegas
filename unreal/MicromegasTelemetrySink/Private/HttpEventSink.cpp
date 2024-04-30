#include "MicromegasTelemetrySink/HttpEventSink.h"
#include "HAL/PlatformProcess.h"
#include "HAL/Runnable.h"
#include "HAL/RunnableThread.h"
#include "HAL/ThreadManager.h"
#include "HttpModule.h"
#include "InsertBlockRequest.h"
#include "InsertProcessRequest.h"
#include "InsertStreamRequest.h"
#include "Interfaces/IHttpResponse.h"
#include "LogDependencies.h"
#include "MicromegasTelemetrySink/FlushMonitor.h"
#include "MicromegasTelemetrySink/Log.h"
#include "MicromegasTracing/Dispatch.h"
#include "MicromegasTracing/EventStream.h"
#include "MicromegasTracing/LogBlock.h"
#include "MicromegasTracing/Macros.h"
#include "MicromegasTracing/ProcessInfo.h"
#include <sstream>
#include <string>
#if PLATFORM_WINDOWS
	#include "Windows/WindowsSystemIncludes.h"
	#include "Windows/WindowsHWrapper.h"
#endif

DEFINE_LOG_CATEGORY(LogMicromegasTelemetrySink);

namespace
{
	void OnProcessRequestComplete(FHttpRequestPtr HttpRequest, FHttpResponsePtr HttpResponse, bool bSucceeded)
	{
		int32 code = HttpResponse ? HttpResponse->GetResponseCode() : 0;
		if (!bSucceeded || code != 200)
		{
			UE_LOG(LogMicromegasTelemetrySink, Error, TEXT("Request completed with code=%d response=%s"), code, HttpResponse ? *(HttpResponse->GetContentAsString()) : TEXT(""));
		}
	}

	uint64 GetTscFrequency()
	{
#if PLATFORM_WINDOWS
		LARGE_INTEGER Frequency;
		verify(QueryPerformanceFrequency(&Frequency));
		return Frequency.QuadPart;
#else
		return static_cast<uint64>(1.0 / FPlatformTime::GetSecondsPerCycle64());
#endif
	}

} // namespace

RemoteSink::RemoteSink(const FString& baseUrl, const MicromegasTracing::ProcessInfoPtr& ThisProcess, const SharedTelemetryAuthenticator& Auth)
	: BaseUrl(baseUrl)
	, Process(ThisProcess)
	, Auth(Auth)
	, QueueSize(0)
	, RequestShutdown(false)
{
	Thread.Reset(FRunnableThread::Create(this, TEXT("MicromegasRemoteTelemetrySink")));
	Flusher.Reset(new FlushMonitor(this));
}

RemoteSink::~RemoteSink()
{
}

void RemoteSink::OnStartup(const MicromegasTracing::ProcessInfoPtr& processInfo)
{
	FPlatformAtomics::InterlockedIncrement(&QueueSize);
	Queue.Enqueue([this, processInfo]() {
		TArray<uint8> body = FormatInsertProcessRequest(*processInfo);
		SendBinaryRequest(TEXT("insert_process"), body);
	});
	WakeupThread->Trigger();
}

void RemoteSink::OnShutdown()
{
	MICROMEGAS_LOG_STATIC(TEXT("MicromegasTelemetrySink"), MicromegasTracing::LogLevel::Info, TEXT("Shutting down"));
	Flusher.Reset();
	MicromegasTracing::FlushLogStream();
	MicromegasTracing::FlushMetricStream();
	RequestShutdown = true;
	WakeupThread->Trigger();
	Thread->WaitForCompletion();
}

void RemoteSink::OnInitLogStream(const MicromegasTracing::LogStreamPtr& stream)
{
	IncrementQueueSize();
	Queue.Enqueue([this, stream]() {
		TArray<uint8> body = FormatInsertLogStreamRequest(*stream);
		SendBinaryRequest(TEXT("insert_stream"), body);
	});
	WakeupThread->Trigger();
}

void RemoteSink::OnInitMetricStream(const MicromegasTracing::MetricStreamPtr& stream)
{
	IncrementQueueSize();
	Queue.Enqueue([this, stream]() {
		TArray<uint8> body = FormatInsertMetricStreamRequest(*stream);
		SendBinaryRequest(TEXT("insert_stream"), body);
	});
	WakeupThread->Trigger();
}

void RemoteSink::OnInitThreadStream(MicromegasTracing::ThreadStream* stream)
{
	const uint32 threadId = FPlatformTLS::GetCurrentThreadId();
	const FString& threadName = FThreadManager::GetThreadName(threadId);

	stream->SetProperty(TEXT("thread-name"), *threadName);
	stream->SetProperty(TEXT("thread-id"), *FString::Format(TEXT("{0}"), { threadId }));

	IncrementQueueSize();
	Queue.Enqueue([this, stream]() {
		TArray<uint8> body = FormatInsertThreadStreamRequest(*stream);
		SendBinaryRequest(TEXT("insert_stream"), body);
	});
	WakeupThread->Trigger();
}

void RemoteSink::OnProcessLogBlock(const MicromegasTracing::LogBlockPtr& block)
{
	IncrementQueueSize();
	Queue.Enqueue([this, block]() {
		TArray<uint8> content = FormatBlockRequest(*Process, *block);
		SendBinaryRequest(TEXT("insert_block"), content);
	});
	WakeupThread->Trigger();
}

void RemoteSink::OnProcessMetricBlock(const MicromegasTracing::MetricsBlockPtr& block)
{
	IncrementQueueSize();
	Queue.Enqueue([this, block]() {
		TArray<uint8> content = FormatBlockRequest(*Process, *block);
		SendBinaryRequest(TEXT("insert_block"), content);
	});
	WakeupThread->Trigger();
}

void RemoteSink::OnProcessThreadBlock(const MicromegasTracing::ThreadBlockPtr& block)
{
	MICROMEGAS_SPAN_SCOPE(TEXT("MicromegasTelemetrySink"), TEXT("OnProcessThreadBlock"));
	IncrementQueueSize();
	Queue.Enqueue([this, block]() {
		TArray<uint8> content = FormatBlockRequest(*Process, *block);
		SendBinaryRequest(TEXT("insert_block"), content);
	});
	WakeupThread->Trigger();
}

bool RemoteSink::IsBusy()
{
	return QueueSize > 0;
}

uint32 RemoteSink::Run()
{
	while (true)
	{
		Callback c;
		while (Queue.Dequeue(c))
		{
			int32 newQueueSize = FPlatformAtomics::InterlockedDecrement(&QueueSize);
			MICROMEGAS_IMETRIC(TEXT("MicromegasTelemetrySink"), MicromegasTracing::Verbosity::Min, TEXT("QueueSize"), TEXT("count"), newQueueSize);
			c();
		}

		if (RequestShutdown)
		{
			break;
		}
		WakeupThread->Wait();
	}
	return 0;
}

void RemoteSink::IncrementQueueSize()
{
	MICROMEGAS_SPAN_SCOPE(TEXT("MicromegasTelemetrySink"), TEXT("IncrementQueueSize"));
	int32 incrementedQueueSize = FPlatformAtomics::InterlockedIncrement(&QueueSize);
	MICROMEGAS_IMETRIC(TEXT("MicromegasTelemetrySink"), MicromegasTracing::Verbosity::Min, TEXT("QueueSize"), TEXT("count"), incrementedQueueSize);
}

void RemoteSink::SendBinaryRequest(const TCHAR* command, const TArray<uint8>& content)
{
	MICROMEGAS_SPAN_SCOPE(TEXT("MicromegasTelemetrySink"), TEXT("SendBinaryRequest"));
	TSharedRef<IHttpRequest, ESPMode::ThreadSafe> HttpRequest = FHttpModule::Get().CreateRequest();
	HttpRequest->SetURL(BaseUrl + command);
	HttpRequest->SetVerb(TEXT("POST"));
	HttpRequest->SetContent(content);
	HttpRequest->SetHeader(TEXT("Content-Type"), TEXT("application/octet-stream"));
	HttpRequest->OnProcessRequestComplete().BindStatic(&OnProcessRequestComplete);
	if (!Auth->Sign(*HttpRequest))
	{
		UE_LOG(LogMicromegasTelemetrySink, Warning, TEXT("Failed to sign telemetry http request"));
		return;
	}

	if (!HttpRequest->ProcessRequest())
	{
		UE_LOG(LogMicromegasTelemetrySink, Error, TEXT("Failed to initialize telemetry http request"));
	}
}

FString CreateGuid()
{
	return FGuid::NewGuid().ToString(EGuidFormats::DigitsWithHyphens);
}

FString GetDistro()
{
	return FString::Printf(TEXT("%s %s"), ANSI_TO_TCHAR(FPlatformProperties::PlatformName()), *FPlatformMisc::GetOSVersion());
}

void InitRemoteSink(const FString& BaseUrl, const SharedTelemetryAuthenticator& Auth)
{
	using namespace MicromegasTracing;
	UE_LOG(LogMicromegasTelemetrySink, Log, TEXT("Initializing Remote Telemetry Sink"));

	DualTime startTime = DualTime::Now();
	FString processId = CreateGuid();
	FString parentProcessId = FPlatformMisc::GetEnvironmentVariable(TEXT("MICROMEGAS_TELEMETRY_PARENT_PROCESS"));
	FPlatformMisc::SetEnvironmentVar(TEXT("MICROMEGAS_TELEMETRY_PARENT_PROCESS"), *processId);

	ProcessInfoPtr process(new ProcessInfo());
	process->ProcessId = processId;
	process->ParentProcessId = parentProcessId;
	process->Exe = FPlatformProcess::ExecutablePath();
	process->Username = FPlatformProcess::UserName(false);
	process->Computer = FPlatformProcess::ComputerName();
	process->Distro = GetDistro();
	process->CpuBrand = *FPlatformMisc::GetCPUBrand();
	process->TscFrequency = GetTscFrequency();
	process->StartTime = startTime;

	std::shared_ptr<EventSink> sink = std::make_shared<RemoteSink>(BaseUrl, process, Auth);
	const size_t LOG_BUFFER_SIZE = 10 * 1024 * 1024;
	const size_t METRICS_BUFFER_SIZE = 10 * 1024 * 1024;
	const size_t THREAD_BUFFER_SIZE = 10 * 1024 * 1024;

	Dispatch::Init(&CreateGuid, process, sink, LOG_BUFFER_SIZE, METRICS_BUFFER_SIZE, THREAD_BUFFER_SIZE);
	UE_LOG(LogMicromegasTelemetrySink, Log, TEXT("Initializing Legion Telemetry for process %s"), *process->ProcessId);
	MICROMEGAS_LOG_STATIC(TEXT("MicromegasTelemetrySink"), LogLevel::Info, TEXT("Telemetry enabled"));
}