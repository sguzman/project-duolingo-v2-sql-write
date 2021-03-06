# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sql_write.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sql_write.proto',
  package='sql_write',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fsql_write.proto\x12\tsql_write\"\x12\n\x03\x41\x63k\x12\x0b\n\x03msg\x18\x01 \x01(\x08\"\x16\n\x05Users\x12\r\n\x05names\x18\x01 \x03(\t2<\n\x08SQLWrite\x12\x30\n\nWriteUsers\x12\x10.sql_write.Users\x1a\x0e.sql_write.Ack\"\x00\x62\x06proto3'
)




_ACK = _descriptor.Descriptor(
  name='Ack',
  full_name='sql_write.Ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='sql_write.Ack.msg', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=48,
)


_USERS = _descriptor.Descriptor(
  name='Users',
  full_name='sql_write.Users',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='sql_write.Users.names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=72,
)

DESCRIPTOR.message_types_by_name['Ack'] = _ACK
DESCRIPTOR.message_types_by_name['Users'] = _USERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ack = _reflection.GeneratedProtocolMessageType('Ack', (_message.Message,), {
  'DESCRIPTOR' : _ACK,
  '__module__' : 'sql_write_pb2'
  # @@protoc_insertion_point(class_scope:sql_write.Ack)
  })
_sym_db.RegisterMessage(Ack)

Users = _reflection.GeneratedProtocolMessageType('Users', (_message.Message,), {
  'DESCRIPTOR' : _USERS,
  '__module__' : 'sql_write_pb2'
  # @@protoc_insertion_point(class_scope:sql_write.Users)
  })
_sym_db.RegisterMessage(Users)



_SQLWRITE = _descriptor.ServiceDescriptor(
  name='SQLWrite',
  full_name='sql_write.SQLWrite',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=74,
  serialized_end=134,
  methods=[
  _descriptor.MethodDescriptor(
    name='WriteUsers',
    full_name='sql_write.SQLWrite.WriteUsers',
    index=0,
    containing_service=None,
    input_type=_USERS,
    output_type=_ACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SQLWRITE)

DESCRIPTOR.services_by_name['SQLWrite'] = _SQLWRITE

# @@protoc_insertion_point(module_scope)
