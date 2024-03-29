# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yt_video_process.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16yt_video_process.proto\x12\x19trpc.media.ytvideoprocess\x1a\x1cgoogle/protobuf/struct.proto\x1a\x0c\x63ommon.proto\"\x99\x03\n\x12VideoProcessOption\x12\x18\n\x10OutputVideoCodec\x18\x01 \x01(\t\x12\x1e\n\x16OutputVideoPeakBitrate\x18\x02 \x01(\x05\x12\x13\n\x0bOutputWidth\x18\x03 \x01(\x05\x12\x14\n\x0cOutputHeight\x18\x04 \x01(\x05\x12\n\n\x02SR\x18\x05 \x01(\x05\x12\x0e\n\x06Interp\x18\x06 \x01(\x05\x12\x11\n\tOutputFps\x18\x07 \x01(\x05\x12\x19\n\x11\x43olorEnhanceLevel\x18\x08 \x01(\x05\x12\x15\n\rDescratchGray\x18\x16 \x01(\x05\x12\x16\n\x0e\x44\x65scratchColor\x18\x17 \x01(\x05\x12\x13\n\x0b\x46\x61\x63\x65\x45nhance\x18\x18 \x01(\x05\x12\x15\n\rLargeFaceMode\x18\x19 \x01(\x05\x12\x15\n\rSmallFaceMode\x18\x1a \x01(\x05\x12\x13\n\x0bRefColorize\x18\x1b \x01(\x05\x12\x16\n\x0eRefColorizeImg\x18\x1c \x01(\t\x12\x13\n\x0b\x44\x65hazeLevel\x18\x1d \x01(\x02\x12\x0f\n\x07SDR2HDR\x18) \x01(\x05\x12\x0f\n\x07HDRType\x18* \x01(\t\"\xdf\x01\n\x1d\x43reateVideoProcessTaskRequest\x12\x0f\n\x07MediaId\x18\x02 \x01(\t\x12\x10\n\x08TaskName\x18\x05 \x01(\t\x12\x13\n\x0b\x43\x61llbackURL\x18\x06 \x01(\t\x12@\n\x0bProcessType\x18\x0b \x01(\x0e\x32+.trpc.media.ytvideoprocess.VideoProcessType\x12\x44\n\rProcessOption\x18\x0c \x01(\x0b\x32-.trpc.media.ytvideoprocess.VideoProcessOption\",\n\x1a\x43reateVideoProcessResponse\x12\x0e\n\x06TaskId\x18\x03 \x01(\t\"\x82\x02\n\x0bVideoDetail\x12\x0f\n\x07VideoID\x18\x01 \x01(\x05\x12\x10\n\x08VideoURL\x18\x02 \x01(\t\x12\x13\n\x0bVideoWebURL\x18\x03 \x01(\t\x12\x0e\n\x06Height\x18\x04 \x01(\x05\x12\r\n\x05Width\x18\x05 \x01(\x05\x12\x0b\n\x03\x46PS\x18\x06 \x01(\x02\x12\x0f\n\x07\x42itRate\x18\x07 \x01(\x02\x12\x0c\n\x04Size\x18\x08 \x01(\x02\x12\x0c\n\x04VMAF\x18\t \x01(\x02\x12\x0c\n\x04PSNR\x18\n \x01(\x02\x12\x0c\n\x04SSIM\x18\x0b \x01(\x02\x12\r\n\x05LPIPS\x18\x0c \x01(\x02\x12\x10\n\x08ImageUrl\x18\r \x01(\t\x12\x11\n\tBandWidth\x18\x0f \x01(\x05\x12\x12\n\nVideoCodec\x18\x10 \x01(\t\"F\n\x16VideoProcessTaskDetail\x12\x15\n\rSourceMediaId\x18\x03 \x01(\t\x12\x15\n\rTargetMediaId\x18\x04 \x01(\t\"3\n!DescribeVideoProcessDetailRequest\x12\x0e\n\x06TaskId\x18\x02 \x01(\t\"\xe0\x01\n\"DescribeVideoProcessDetailResponse\x12-\n\x08TaskInfo\x18\x03 \x01(\x0b\x32\x1b.trpc.media.common.TaskInfo\x12\x45\n\nTaskDetail\x18\x04 \x01(\x0b\x32\x31.trpc.media.ytvideoprocess.VideoProcessTaskDetail\x12\x44\n\rProcessOption\x18\x05 \x01(\x0b\x32-.trpc.media.ytvideoprocess.VideoProcessOption\"-\n\x1bStopVideoProcessTaskRequest\x12\x0e\n\x06TaskId\x18\x02 \x01(\t\".\n\x1cStopVideoProcessTaskResponse\x12\x0e\n\x06TaskId\x18\x03 \x01(\t\"\xaa\x01\n\x1dUpdateVideoProcessTaskRequest\x12\x0f\n\x07MediaId\x18\x02 \x01(\t\x12\x0e\n\x06TaskId\x18\x03 \x01(\t\x12\x44\n\rProcessOption\x18\x0b \x01(\x0b\x32-.trpc.media.ytvideoprocess.VideoProcessOption\x12\x11\n\tAutoStart\x18\x0c \x01(\x08\x12\x0f\n\x07ImageId\x18\r \x01(\t\",\n\x1aUpdateVideoProcessResponse\x12\x0e\n\x06TaskId\x18\x03 \x01(\t*}\n\x10VideoProcessType\x12\x14\n\x10YTProcessUnknown\x10\x00\x12\x16\n\x11YTSuperResolution\x10\xd1\x0f\x12\x12\n\rYTVideoRepair\x10\xd2\x0f\x12\x15\n\x10YTVideoTranscode\x10\xd3\x0f\x12\x10\n\x0bYTVideoCrop\x10\xd4\x0f\x32\xce\x04\n\x0eYTVideoProcess\x12\x89\x01\n\x16\x43reateVideoProcessTask\x12\x38.trpc.media.ytvideoprocess.CreateVideoProcessTaskRequest\x1a\x35.trpc.media.ytvideoprocess.CreateVideoProcessResponse\x12\x99\x01\n\x1a\x44\x65scribeVideoProcessDetail\x12<.trpc.media.ytvideoprocess.DescribeVideoProcessDetailRequest\x1a=.trpc.media.ytvideoprocess.DescribeVideoProcessDetailResponse\x12\x89\x01\n\x16UpdateVideoProcessTask\x12\x38.trpc.media.ytvideoprocess.UpdateVideoProcessTaskRequest\x1a\x35.trpc.media.ytvideoprocess.UpdateVideoProcessResponse\x12\x87\x01\n\x14StopVideoProcessTask\x12\x36.trpc.media.ytvideoprocess.StopVideoProcessTaskRequest\x1a\x37.trpc.media.ytvideoprocess.StopVideoProcessTaskResponseB^Z\\github.com/Tencent-media-asset-system-sdk/media-platform-sdk-go/protobuf-spec/ytvideoprocessb\x06proto3')

_VIDEOPROCESSTYPE = DESCRIPTOR.enum_types_by_name['VideoProcessType']
VideoProcessType = enum_type_wrapper.EnumTypeWrapper(_VIDEOPROCESSTYPE)
YTProcessUnknown = 0
YTSuperResolution = 2001
YTVideoRepair = 2002
YTVideoTranscode = 2003
YTVideoCrop = 2004


_VIDEOPROCESSOPTION = DESCRIPTOR.message_types_by_name['VideoProcessOption']
_CREATEVIDEOPROCESSTASKREQUEST = DESCRIPTOR.message_types_by_name['CreateVideoProcessTaskRequest']
_CREATEVIDEOPROCESSRESPONSE = DESCRIPTOR.message_types_by_name['CreateVideoProcessResponse']
_VIDEODETAIL = DESCRIPTOR.message_types_by_name['VideoDetail']
_VIDEOPROCESSTASKDETAIL = DESCRIPTOR.message_types_by_name['VideoProcessTaskDetail']
_DESCRIBEVIDEOPROCESSDETAILREQUEST = DESCRIPTOR.message_types_by_name['DescribeVideoProcessDetailRequest']
_DESCRIBEVIDEOPROCESSDETAILRESPONSE = DESCRIPTOR.message_types_by_name['DescribeVideoProcessDetailResponse']
_STOPVIDEOPROCESSTASKREQUEST = DESCRIPTOR.message_types_by_name['StopVideoProcessTaskRequest']
_STOPVIDEOPROCESSTASKRESPONSE = DESCRIPTOR.message_types_by_name['StopVideoProcessTaskResponse']
_UPDATEVIDEOPROCESSTASKREQUEST = DESCRIPTOR.message_types_by_name['UpdateVideoProcessTaskRequest']
_UPDATEVIDEOPROCESSRESPONSE = DESCRIPTOR.message_types_by_name['UpdateVideoProcessResponse']
VideoProcessOption = _reflection.GeneratedProtocolMessageType('VideoProcessOption', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOPROCESSOPTION,
  '__module__' : 'yt_video_process_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.ytvideoprocess.VideoProcessOption)
  })
_sym_db.RegisterMessage(VideoProcessOption)

CreateVideoProcessTaskRequest = _reflection.GeneratedProtocolMessageType('CreateVideoProcessTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVIDEOPROCESSTASKREQUEST,
  '__module__' : 'yt_video_process_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.ytvideoprocess.CreateVideoProcessTaskRequest)
  })
_sym_db.RegisterMessage(CreateVideoProcessTaskRequest)

CreateVideoProcessResponse = _reflection.GeneratedProtocolMessageType('CreateVideoProcessResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVIDEOPROCESSRESPONSE,
  '__module__' : 'yt_video_process_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.ytvideoprocess.CreateVideoProcessResponse)
  })
_sym_db.RegisterMessage(CreateVideoProcessResponse)

VideoDetail = _reflection.GeneratedProtocolMessageType('VideoDetail', (_message.Message,), {
  'DESCRIPTOR' : _VIDEODETAIL,
  '__module__' : 'yt_video_process_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.ytvideoprocess.VideoDetail)
  })
_sym_db.RegisterMessage(VideoDetail)

VideoProcessTaskDetail = _reflection.GeneratedProtocolMessageType('VideoProcessTaskDetail', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOPROCESSTASKDETAIL,
  '__module__' : 'yt_video_process_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.ytvideoprocess.VideoProcessTaskDetail)
  })
_sym_db.RegisterMessage(VideoProcessTaskDetail)

DescribeVideoProcessDetailRequest = _reflection.GeneratedProtocolMessageType('DescribeVideoProcessDetailRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVIDEOPROCESSDETAILREQUEST,
  '__module__' : 'yt_video_process_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.ytvideoprocess.DescribeVideoProcessDetailRequest)
  })
_sym_db.RegisterMessage(DescribeVideoProcessDetailRequest)

DescribeVideoProcessDetailResponse = _reflection.GeneratedProtocolMessageType('DescribeVideoProcessDetailResponse', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVIDEOPROCESSDETAILRESPONSE,
  '__module__' : 'yt_video_process_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.ytvideoprocess.DescribeVideoProcessDetailResponse)
  })
_sym_db.RegisterMessage(DescribeVideoProcessDetailResponse)

StopVideoProcessTaskRequest = _reflection.GeneratedProtocolMessageType('StopVideoProcessTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPVIDEOPROCESSTASKREQUEST,
  '__module__' : 'yt_video_process_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.ytvideoprocess.StopVideoProcessTaskRequest)
  })
_sym_db.RegisterMessage(StopVideoProcessTaskRequest)

StopVideoProcessTaskResponse = _reflection.GeneratedProtocolMessageType('StopVideoProcessTaskResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOPVIDEOPROCESSTASKRESPONSE,
  '__module__' : 'yt_video_process_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.ytvideoprocess.StopVideoProcessTaskResponse)
  })
_sym_db.RegisterMessage(StopVideoProcessTaskResponse)

UpdateVideoProcessTaskRequest = _reflection.GeneratedProtocolMessageType('UpdateVideoProcessTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVIDEOPROCESSTASKREQUEST,
  '__module__' : 'yt_video_process_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.ytvideoprocess.UpdateVideoProcessTaskRequest)
  })
_sym_db.RegisterMessage(UpdateVideoProcessTaskRequest)

UpdateVideoProcessResponse = _reflection.GeneratedProtocolMessageType('UpdateVideoProcessResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVIDEOPROCESSRESPONSE,
  '__module__' : 'yt_video_process_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.ytvideoprocess.UpdateVideoProcessResponse)
  })
_sym_db.RegisterMessage(UpdateVideoProcessResponse)

_YTVIDEOPROCESS = DESCRIPTOR.services_by_name['YTVideoProcess']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\\github.com/Tencent-media-asset-system-sdk/media-platform-sdk-go/protobuf-spec/ytvideoprocess'
  _VIDEOPROCESSTYPE._serialized_start=1708
  _VIDEOPROCESSTYPE._serialized_end=1833
  _VIDEOPROCESSOPTION._serialized_start=98
  _VIDEOPROCESSOPTION._serialized_end=507
  _CREATEVIDEOPROCESSTASKREQUEST._serialized_start=510
  _CREATEVIDEOPROCESSTASKREQUEST._serialized_end=733
  _CREATEVIDEOPROCESSRESPONSE._serialized_start=735
  _CREATEVIDEOPROCESSRESPONSE._serialized_end=779
  _VIDEODETAIL._serialized_start=782
  _VIDEODETAIL._serialized_end=1040
  _VIDEOPROCESSTASKDETAIL._serialized_start=1042
  _VIDEOPROCESSTASKDETAIL._serialized_end=1112
  _DESCRIBEVIDEOPROCESSDETAILREQUEST._serialized_start=1114
  _DESCRIBEVIDEOPROCESSDETAILREQUEST._serialized_end=1165
  _DESCRIBEVIDEOPROCESSDETAILRESPONSE._serialized_start=1168
  _DESCRIBEVIDEOPROCESSDETAILRESPONSE._serialized_end=1392
  _STOPVIDEOPROCESSTASKREQUEST._serialized_start=1394
  _STOPVIDEOPROCESSTASKREQUEST._serialized_end=1439
  _STOPVIDEOPROCESSTASKRESPONSE._serialized_start=1441
  _STOPVIDEOPROCESSTASKRESPONSE._serialized_end=1487
  _UPDATEVIDEOPROCESSTASKREQUEST._serialized_start=1490
  _UPDATEVIDEOPROCESSTASKREQUEST._serialized_end=1660
  _UPDATEVIDEOPROCESSRESPONSE._serialized_start=1662
  _UPDATEVIDEOPROCESSRESPONSE._serialized_end=1706
  _YTVIDEOPROCESS._serialized_start=1836
  _YTVIDEOPROCESS._serialized_end=2426
# @@protoc_insertion_point(module_scope)
