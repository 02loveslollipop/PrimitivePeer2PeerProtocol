# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: p2p.proto
# Protobuf Python Version: 5.27.2
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
    2,
    '',
    'p2p.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tp2p.proto\"-\n\x0e\x63onnectionData\x12\x0e\n\x06number\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\"!\n\x11\x64isconnectionData\x12\x0c\n\x04hash\x18\x01 \x01(\t\"\"\n\x0f\x63onnectionReply\x12\x0f\n\x07message\x18\x01 \x01(\x08\"%\n\x12\x64isconnectionReply\x12\x0f\n\x07message\x18\x01 \x01(\x08\x32j\n\x07Greeter\x12+\n\x04join\x12\x0f.connectionData\x1a\x10.connectionReply\"\x00\x12\x32\n\x05leave\x12\x12.disconnectionData\x1a\x13.disconnectionReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'p2p_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CONNECTIONDATA']._serialized_start=13
  _globals['_CONNECTIONDATA']._serialized_end=58
  _globals['_DISCONNECTIONDATA']._serialized_start=60
  _globals['_DISCONNECTIONDATA']._serialized_end=93
  _globals['_CONNECTIONREPLY']._serialized_start=95
  _globals['_CONNECTIONREPLY']._serialized_end=129
  _globals['_DISCONNECTIONREPLY']._serialized_start=131
  _globals['_DISCONNECTIONREPLY']._serialized_end=168
  _globals['_GREETER']._serialized_start=170
  _globals['_GREETER']._serialized_end=276
# @@protoc_insertion_point(module_scope)
