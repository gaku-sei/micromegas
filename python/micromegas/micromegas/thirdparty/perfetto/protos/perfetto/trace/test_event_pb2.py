# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protos/perfetto/trace/test_event.proto
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
    'protos/perfetto/trace/test_event.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.perfetto.trace.track_event import debug_annotation_pb2 as protos_dot_perfetto_dot_trace_dot_track__event_dot_debug__annotation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&protos/perfetto/trace/test_event.proto\x12\x0fperfetto.protos\x1a\x38protos/perfetto/trace/track_event/debug_annotation.proto\"\xfb\x02\n\tTestEvent\x12\x0b\n\x03str\x18\x01 \x01(\t\x12\x11\n\tseq_value\x18\x02 \x01(\r\x12\x0f\n\x07\x63ounter\x18\x03 \x01(\x04\x12\x0f\n\x07is_last\x18\x04 \x01(\x08\x12\x37\n\x07payload\x18\x05 \x01(\x0b\x32&.perfetto.protos.TestEvent.TestPayload\x1a\xf2\x01\n\x0bTestPayload\x12\x0b\n\x03str\x18\x01 \x03(\t\x12\x36\n\x06nested\x18\x02 \x03(\x0b\x32&.perfetto.protos.TestEvent.TestPayload\x12\x15\n\rsingle_string\x18\x04 \x01(\t\x12\x12\n\nsingle_int\x18\x05 \x01(\x05\x12\x15\n\rrepeated_ints\x18\x06 \x03(\x05\x12\x1f\n\x17remaining_nesting_depth\x18\x03 \x01(\r\x12;\n\x11\x64\x65\x62ug_annotations\x18\x07 \x03(\x0b\x32 .perfetto.protos.DebugAnnotation')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.test_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TESTEVENT']._serialized_start=118
  _globals['_TESTEVENT']._serialized_end=497
  _globals['_TESTEVENT_TESTPAYLOAD']._serialized_start=255
  _globals['_TESTEVENT_TESTPAYLOAD']._serialized_end=497
# @@protoc_insertion_point(module_scope)