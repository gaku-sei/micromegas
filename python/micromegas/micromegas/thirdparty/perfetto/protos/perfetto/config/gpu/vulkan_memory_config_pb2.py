# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protos/perfetto/config/gpu/vulkan_memory_config.proto
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
    'protos/perfetto/config/gpu/vulkan_memory_config.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5protos/perfetto/config/gpu/vulkan_memory_config.proto\x12\x0fperfetto.protos\"Z\n\x12VulkanMemoryConfig\x12!\n\x19track_driver_memory_usage\x18\x01 \x01(\x08\x12!\n\x19track_device_memory_usage\x18\x02 \x01(\x08')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.config.gpu.vulkan_memory_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_VULKANMEMORYCONFIG']._serialized_start=74
  _globals['_VULKANMEMORYCONFIG']._serialized_end=164
# @@protoc_insertion_point(module_scope)
