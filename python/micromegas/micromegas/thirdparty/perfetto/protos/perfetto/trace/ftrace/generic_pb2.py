# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protos/perfetto/trace/ftrace/generic.proto
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
    'protos/perfetto/trace/ftrace/generic.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*protos/perfetto/trace/ftrace/generic.proto\x12\x0fperfetto.protos\"\xc2\x01\n\x12GenericFtraceEvent\x12\x12\n\nevent_name\x18\x01 \x01(\t\x12\x38\n\x05\x66ield\x18\x02 \x03(\x0b\x32).perfetto.protos.GenericFtraceEvent.Field\x1a^\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\tstr_value\x18\x03 \x01(\tH\x00\x12\x13\n\tint_value\x18\x04 \x01(\x03H\x00\x12\x14\n\nuint_value\x18\x05 \x01(\x04H\x00\x42\x07\n\x05value')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.ftrace.generic_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GENERICFTRACEEVENT']._serialized_start=64
  _globals['_GENERICFTRACEEVENT']._serialized_end=258
  _globals['_GENERICFTRACEEVENT_FIELD']._serialized_start=164
  _globals['_GENERICFTRACEEVENT_FIELD']._serialized_end=258
# @@protoc_insertion_point(module_scope)
