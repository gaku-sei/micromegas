# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protos/perfetto/config/data_source_config.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    1,
    '',
    'protos/perfetto/config/data_source_config.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.perfetto.config.android import android_game_intervention_list_config_pb2 as protos_dot_perfetto_dot_config_dot_android_dot_android__game__intervention__list__config__pb2
from protos.perfetto.config.android import android_input_event_config_pb2 as protos_dot_perfetto_dot_config_dot_android_dot_android__input__event__config__pb2
from protos.perfetto.config.android import android_log_config_pb2 as protos_dot_perfetto_dot_config_dot_android_dot_android__log__config__pb2
from protos.perfetto.config.android import android_polled_state_config_pb2 as protos_dot_perfetto_dot_config_dot_android_dot_android__polled__state__config__pb2
from protos.perfetto.config.android import android_system_property_config_pb2 as protos_dot_perfetto_dot_config_dot_android_dot_android__system__property__config__pb2
from protos.perfetto.config.android import android_sdk_sysprop_guard_config_pb2 as protos_dot_perfetto_dot_config_dot_android_dot_android__sdk__sysprop__guard__config__pb2
from protos.perfetto.config.android import network_trace_config_pb2 as protos_dot_perfetto_dot_config_dot_android_dot_network__trace__config__pb2
from protos.perfetto.config.android import packages_list_config_pb2 as protos_dot_perfetto_dot_config_dot_android_dot_packages__list__config__pb2
from protos.perfetto.config.android import pixel_modem_config_pb2 as protos_dot_perfetto_dot_config_dot_android_dot_pixel__modem__config__pb2
from protos.perfetto.config.android import protolog_config_pb2 as protos_dot_perfetto_dot_config_dot_android_dot_protolog__config__pb2
from protos.perfetto.config.android import surfaceflinger_layers_config_pb2 as protos_dot_perfetto_dot_config_dot_android_dot_surfaceflinger__layers__config__pb2
from protos.perfetto.config.android import surfaceflinger_transactions_config_pb2 as protos_dot_perfetto_dot_config_dot_android_dot_surfaceflinger__transactions__config__pb2
from protos.perfetto.config.chrome import chrome_config_pb2 as protos_dot_perfetto_dot_config_dot_chrome_dot_chrome__config__pb2
from protos.perfetto.config.chrome import v8_config_pb2 as protos_dot_perfetto_dot_config_dot_chrome_dot_v8__config__pb2
from protos.perfetto.config.etw import etw_config_pb2 as protos_dot_perfetto_dot_config_dot_etw_dot_etw__config__pb2
from protos.perfetto.config.ftrace import ftrace_config_pb2 as protos_dot_perfetto_dot_config_dot_ftrace_dot_ftrace__config__pb2
from protos.perfetto.config.gpu import gpu_counter_config_pb2 as protos_dot_perfetto_dot_config_dot_gpu_dot_gpu__counter__config__pb2
from protos.perfetto.config.gpu import vulkan_memory_config_pb2 as protos_dot_perfetto_dot_config_dot_gpu_dot_vulkan__memory__config__pb2
from protos.perfetto.config.inode_file import inode_file_config_pb2 as protos_dot_perfetto_dot_config_dot_inode__file_dot_inode__file__config__pb2
from protos.perfetto.config import interceptor_config_pb2 as protos_dot_perfetto_dot_config_dot_interceptor__config__pb2
from protos.perfetto.config.power import android_power_config_pb2 as protos_dot_perfetto_dot_config_dot_power_dot_android__power__config__pb2
from protos.perfetto.config.statsd import statsd_tracing_config_pb2 as protos_dot_perfetto_dot_config_dot_statsd_dot_statsd__tracing__config__pb2
from protos.perfetto.config.process_stats import process_stats_config_pb2 as protos_dot_perfetto_dot_config_dot_process__stats_dot_process__stats__config__pb2
from protos.perfetto.config.profiling import heapprofd_config_pb2 as protos_dot_perfetto_dot_config_dot_profiling_dot_heapprofd__config__pb2
from protos.perfetto.config.profiling import java_hprof_config_pb2 as protos_dot_perfetto_dot_config_dot_profiling_dot_java__hprof__config__pb2
from protos.perfetto.config.profiling import perf_event_config_pb2 as protos_dot_perfetto_dot_config_dot_profiling_dot_perf__event__config__pb2
from protos.perfetto.config.sys_stats import sys_stats_config_pb2 as protos_dot_perfetto_dot_config_dot_sys__stats_dot_sys__stats__config__pb2
from protos.perfetto.config import test_config_pb2 as protos_dot_perfetto_dot_config_dot_test__config__pb2
from protos.perfetto.config.track_event import track_event_config_pb2 as protos_dot_perfetto_dot_config_dot_track__event_dot_track__event__config__pb2
from protos.perfetto.config.system_info import system_info_pb2 as protos_dot_perfetto_dot_config_dot_system__info_dot_system__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/protos/perfetto/config/data_source_config.proto\x12\x0fperfetto.protos\x1aJprotos/perfetto/config/android/android_game_intervention_list_config.proto\x1a?protos/perfetto/config/android/android_input_event_config.proto\x1a\x37protos/perfetto/config/android/android_log_config.proto\x1a@protos/perfetto/config/android/android_polled_state_config.proto\x1a\x43protos/perfetto/config/android/android_system_property_config.proto\x1a\x45protos/perfetto/config/android/android_sdk_sysprop_guard_config.proto\x1a\x39protos/perfetto/config/android/network_trace_config.proto\x1a\x39protos/perfetto/config/android/packages_list_config.proto\x1a\x37protos/perfetto/config/android/pixel_modem_config.proto\x1a\x34protos/perfetto/config/android/protolog_config.proto\x1a\x41protos/perfetto/config/android/surfaceflinger_layers_config.proto\x1aGprotos/perfetto/config/android/surfaceflinger_transactions_config.proto\x1a\x31protos/perfetto/config/chrome/chrome_config.proto\x1a-protos/perfetto/config/chrome/v8_config.proto\x1a+protos/perfetto/config/etw/etw_config.proto\x1a\x31protos/perfetto/config/ftrace/ftrace_config.proto\x1a\x33protos/perfetto/config/gpu/gpu_counter_config.proto\x1a\x35protos/perfetto/config/gpu/vulkan_memory_config.proto\x1a\x39protos/perfetto/config/inode_file/inode_file_config.proto\x1a/protos/perfetto/config/interceptor_config.proto\x1a\x37protos/perfetto/config/power/android_power_config.proto\x1a\x39protos/perfetto/config/statsd/statsd_tracing_config.proto\x1a?protos/perfetto/config/process_stats/process_stats_config.proto\x1a\x37protos/perfetto/config/profiling/heapprofd_config.proto\x1a\x38protos/perfetto/config/profiling/java_hprof_config.proto\x1a\x38protos/perfetto/config/profiling/perf_event_config.proto\x1a\x37protos/perfetto/config/sys_stats/sys_stats_config.proto\x1a(protos/perfetto/config/test_config.proto\x1a;protos/perfetto/config/track_event/track_event_config.proto\x1a\x34protos/perfetto/config/system_info/system_info.proto\"\xf1\x13\n\x10\x44\x61taSourceConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rtarget_buffer\x18\x02 \x01(\r\x12\x19\n\x11trace_duration_ms\x18\x03 \x01(\r\x12)\n!prefer_suspend_clock_for_duration\x18z \x01(\x08\x12\x17\n\x0fstop_timeout_ms\x18\x07 \x01(\r\x12\x1f\n\x17\x65nable_extra_guardrails\x18\x06 \x01(\x08\x12M\n\x11session_initiator\x18\x08 \x01(\x0e\x32\x32.perfetto.protos.DataSourceConfig.SessionInitiator\x12\x1a\n\x12tracing_session_id\x18\x04 \x01(\x04\x12\x38\n\rftrace_config\x18\x64 \x01(\x0b\x32\x1d.perfetto.protos.FtraceConfigB\x02(\x01\x12?\n\x11inode_file_config\x18\x66 \x01(\x0b\x32 .perfetto.protos.InodeFileConfigB\x02(\x01\x12\x45\n\x14process_stats_config\x18g \x01(\x0b\x32#.perfetto.protos.ProcessStatsConfigB\x02(\x01\x12=\n\x10sys_stats_config\x18h \x01(\x0b\x32\x1f.perfetto.protos.SysStatsConfigB\x02(\x01\x12>\n\x10heapprofd_config\x18i \x01(\x0b\x32 .perfetto.protos.HeapprofdConfigB\x02(\x01\x12?\n\x11java_hprof_config\x18n \x01(\x0b\x32 .perfetto.protos.JavaHprofConfigB\x02(\x01\x12\x45\n\x14\x61ndroid_power_config\x18j \x01(\x0b\x32#.perfetto.protos.AndroidPowerConfigB\x02(\x01\x12\x41\n\x12\x61ndroid_log_config\x18k \x01(\x0b\x32!.perfetto.protos.AndroidLogConfigB\x02(\x01\x12\x41\n\x12gpu_counter_config\x18l \x01(\x0b\x32!.perfetto.protos.GpuCounterConfigB\x02(\x01\x12\x65\n%android_game_intervention_list_config\x18t \x01(\x0b\x32\x32.perfetto.protos.AndroidGameInterventionListConfigB\x02(\x01\x12\x45\n\x14packages_list_config\x18m \x01(\x0b\x32#.perfetto.protos.PackagesListConfigB\x02(\x01\x12?\n\x11perf_event_config\x18o \x01(\x0b\x32 .perfetto.protos.PerfEventConfigB\x02(\x01\x12\x45\n\x14vulkan_memory_config\x18p \x01(\x0b\x32#.perfetto.protos.VulkanMemoryConfigB\x02(\x01\x12\x41\n\x12track_event_config\x18q \x01(\x0b\x32!.perfetto.protos.TrackEventConfigB\x02(\x01\x12R\n\x1b\x61ndroid_polled_state_config\x18r \x01(\x0b\x32).perfetto.protos.AndroidPolledStateConfigB\x02(\x01\x12X\n\x1e\x61ndroid_system_property_config\x18v \x01(\x0b\x32,.perfetto.protos.AndroidSystemPropertyConfigB\x02(\x01\x12G\n\x15statsd_tracing_config\x18u \x01(\x0b\x32$.perfetto.protos.StatsdTracingConfigB\x02(\x01\x12=\n\x12system_info_config\x18w \x01(\x0b\x32!.perfetto.protos.SystemInfoConfig\x12\x34\n\rchrome_config\x18\x65 \x01(\x0b\x32\x1d.perfetto.protos.ChromeConfig\x12\x30\n\tv8_config\x18\x7f \x01(\x0b\x32\x19.perfetto.protos.V8ConfigB\x02(\x01\x12>\n\x12interceptor_config\x18s \x01(\x0b\x32\".perfetto.protos.InterceptorConfig\x12R\n\x1bnetwork_packet_trace_config\x18x \x01(\x0b\x32).perfetto.protos.NetworkPacketTraceConfigB\x02(\x01\x12U\n\x1csurfaceflinger_layers_config\x18y \x01(\x0b\x32+.perfetto.protos.SurfaceFlingerLayersConfigB\x02(\x01\x12\x61\n\"surfaceflinger_transactions_config\x18{ \x01(\x0b\x32\x31.perfetto.protos.SurfaceFlingerTransactionsConfigB\x02(\x01\x12[\n android_sdk_sysprop_guard_config\x18| \x01(\x0b\x32-.perfetto.protos.AndroidSdkSyspropGuardConfigB\x02(\x01\x12\x32\n\netw_config\x18} \x01(\x0b\x32\x1a.perfetto.protos.EtwConfigB\x02(\x01\x12<\n\x0fprotolog_config\x18~ \x01(\x0b\x32\x1f.perfetto.protos.ProtoLogConfigB\x02(\x01\x12Q\n\x1a\x61ndroid_input_event_config\x18\x80\x01 \x01(\x0b\x32(.perfetto.protos.AndroidInputEventConfigB\x02(\x01\x12\x42\n\x12pixel_modem_config\x18\x81\x01 \x01(\x0b\x32!.perfetto.protos.PixelModemConfigB\x02(\x01\x12\x16\n\rlegacy_config\x18\xe8\x07 \x01(\t\x12\x31\n\x0b\x66or_testing\x18\xe9\x07 \x01(\x0b\x32\x1b.perfetto.protos.TestConfig\"[\n\x10SessionInitiator\x12!\n\x1dSESSION_INITIATOR_UNSPECIFIED\x10\x00\x12$\n SESSION_INITIATOR_TRUSTED_SYSTEM\x10\x01J\x0b\x08\xff\xff\xff\x7f\x10\x80\x80\x80\x80\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.config.data_source_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['ftrace_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['ftrace_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['inode_file_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['inode_file_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['process_stats_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['process_stats_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['sys_stats_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['sys_stats_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['heapprofd_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['heapprofd_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['java_hprof_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['java_hprof_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['android_power_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['android_power_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['android_log_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['android_log_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['gpu_counter_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['gpu_counter_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['android_game_intervention_list_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['android_game_intervention_list_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['packages_list_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['packages_list_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['perf_event_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['perf_event_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['vulkan_memory_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['vulkan_memory_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['track_event_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['track_event_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['android_polled_state_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['android_polled_state_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['android_system_property_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['android_system_property_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['statsd_tracing_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['statsd_tracing_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['v8_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['v8_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['network_packet_trace_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['network_packet_trace_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['surfaceflinger_layers_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['surfaceflinger_layers_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['surfaceflinger_transactions_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['surfaceflinger_transactions_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['android_sdk_sysprop_guard_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['android_sdk_sysprop_guard_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['etw_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['etw_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['protolog_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['protolog_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['android_input_event_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['android_input_event_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG'].fields_by_name['pixel_modem_config']._loaded_options = None
  _globals['_DATASOURCECONFIG'].fields_by_name['pixel_modem_config']._serialized_options = b'(\001'
  _globals['_DATASOURCECONFIG']._serialized_start=1820
  _globals['_DATASOURCECONFIG']._serialized_end=4365
  _globals['_DATASOURCECONFIG_SESSIONINITIATOR']._serialized_start=4261
  _globals['_DATASOURCECONFIG_SESSIONINITIATOR']._serialized_end=4352
# @@protoc_insertion_point(module_scope)
