# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shot_match.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10shot_match.proto\x12\x14trpc.media.shotmatch\"!\n\rShotMatchInfo\x12\x10\n\x08ScoreSet\x18\x01 \x03(\x02\"J\n\x11ShotMatchTaskData\x12\x35\n\x08MatchSet\x18\x01 \x03(\x0b\x32#.trpc.media.shotmatch.ShotMatchInfoBYZWgithub.com/Tencent-media-asset-system-sdk/media-platform-sdk-go/protobuf-spec/shotmatchb\x06proto3')



_SHOTMATCHINFO = DESCRIPTOR.message_types_by_name['ShotMatchInfo']
_SHOTMATCHTASKDATA = DESCRIPTOR.message_types_by_name['ShotMatchTaskData']
ShotMatchInfo = _reflection.GeneratedProtocolMessageType('ShotMatchInfo', (_message.Message,), {
  'DESCRIPTOR' : _SHOTMATCHINFO,
  '__module__' : 'shot_match_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.shotmatch.ShotMatchInfo)
  })
_sym_db.RegisterMessage(ShotMatchInfo)

ShotMatchTaskData = _reflection.GeneratedProtocolMessageType('ShotMatchTaskData', (_message.Message,), {
  'DESCRIPTOR' : _SHOTMATCHTASKDATA,
  '__module__' : 'shot_match_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.shotmatch.ShotMatchTaskData)
  })
_sym_db.RegisterMessage(ShotMatchTaskData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZWgithub.com/Tencent-media-asset-system-sdk/media-platform-sdk-go/protobuf-spec/shotmatch'
  _SHOTMATCHINFO._serialized_start=42
  _SHOTMATCHINFO._serialized_end=75
  _SHOTMATCHTASKDATA._serialized_start=77
  _SHOTMATCHTASKDATA._serialized_end=151
# @@protoc_insertion_point(module_scope)