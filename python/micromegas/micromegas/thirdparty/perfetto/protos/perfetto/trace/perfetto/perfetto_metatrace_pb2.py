# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protos/perfetto/trace/perfetto/perfetto_metatrace.proto
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
    'protos/perfetto/trace/perfetto/perfetto_metatrace.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7protos/perfetto/trace/perfetto/perfetto_metatrace.proto\x12\x0fperfetto.protos\"\xa1\x04\n\x11PerfettoMetatrace\x12\x12\n\x08\x65vent_id\x18\x01 \x01(\rH\x00\x12\x14\n\ncounter_id\x18\x02 \x01(\rH\x00\x12\x14\n\nevent_name\x18\x08 \x01(\tH\x00\x12\x18\n\x0e\x65vent_name_iid\x18\x0b \x01(\x04H\x00\x12\x16\n\x0c\x63ounter_name\x18\t \x01(\tH\x00\x12\x19\n\x11\x65vent_duration_ns\x18\x03 \x01(\x04\x12\x15\n\rcounter_value\x18\x04 \x01(\x05\x12\x11\n\tthread_id\x18\x05 \x01(\r\x12\x14\n\x0chas_overruns\x18\x06 \x01(\x08\x12\x34\n\x04\x61rgs\x18\x07 \x03(\x0b\x32&.perfetto.protos.PerfettoMetatrace.Arg\x12K\n\x10interned_strings\x18\n \x03(\x0b\x32\x31.perfetto.protos.PerfettoMetatrace.InternedString\x1a\x7f\n\x03\x41rg\x12\r\n\x03key\x18\x01 \x01(\tH\x00\x12\x11\n\x07key_iid\x18\x03 \x01(\x04H\x00\x12\x0f\n\x05value\x18\x02 \x01(\tH\x01\x12\x13\n\tvalue_iid\x18\x04 \x01(\x04H\x01\x42\x15\n\x13key_or_interned_keyB\x19\n\x17value_or_interned_value\x1a,\n\x0eInternedString\x12\x0b\n\x03iid\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\tB\r\n\x0brecord_type')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.perfetto.perfetto_metatrace_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PERFETTOMETATRACE']._serialized_start=77
  _globals['_PERFETTOMETATRACE']._serialized_end=622
  _globals['_PERFETTOMETATRACE_ARG']._serialized_start=434
  _globals['_PERFETTOMETATRACE_ARG']._serialized_end=561
  _globals['_PERFETTOMETATRACE_INTERNEDSTRING']._serialized_start=563
  _globals['_PERFETTOMETATRACE_INTERNEDSTRING']._serialized_end=607
# @@protoc_insertion_point(module_scope)
