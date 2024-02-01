# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto
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
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63ommon.proto\x12\x11trpc.media.common\x1a\x1cgoogle/protobuf/struct.proto\x1a\x19google/protobuf/any.proto\"Y\n\x0fOperateResponse\x12\x30\n\x06Status\x18\x01 \x01(\x0e\x32 .trpc.media.common.OperateStatus\x12\x14\n\x0c\x46\x61iledReason\x18\x02 \x01(\t\"t\n\x0cTaskTemplate\x12\x10\n\x08TaskName\x18\x01 \x01(\t\x12\x11\n\tApiModule\x18\x02 \x01(\t\x12\x13\n\x0b\x43\x61llbackURL\x18\x03 \x01(\t\x12*\n\tParameter\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"3\n\rFlowDirection\x12\x0f\n\x07UpIndex\x18\x01 \x01(\r\x12\x11\n\tDownIndex\x18\x02 \x01(\r\"\x88\x01\n\x10WorkflowTemplate\x12\x38\n\x0fTaskTemplateSet\x18\x01 \x03(\x0b\x32\x1f.trpc.media.common.TaskTemplate\x12:\n\x10\x46lowDirectionSet\x18\x02 \x03(\x0b\x32 .trpc.media.common.FlowDirection\"{\n\x0f\x44omainGroupInfo\x12G\n\x0f\x44omainGroupType\x18\x01 \x01(\x0e\x32\".trpc.media.common.DomainGroupTypeR\ngroup_type\x12\x1f\n\rDomainGroupId\x18\x02 \x01(\tR\x08group_id\"[\n\x06\x46ilter\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x31\n\nFilterType\x18\x02 \x01(\x0e\x32\x1d.trpc.media.common.FilterType\x12\x10\n\x08ValueSet\x18\x03 \x03(\t\"E\n\x06Sorter\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12-\n\x08SortType\x18\x02 \x01(\x0e\x32\x1b.trpc.media.common.SortType\".\n\x08UserInfo\x12\x0b\n\x03Uin\x18\x01 \x01(\t\x12\x15\n\rSubAccountUin\x18\x02 \x01(\t\"\\\n\x07\x44\x65leter\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x31\n\nDeleteType\x18\x02 \x01(\x0e\x32\x1d.trpc.media.common.DeleteType\x12\x10\n\x08ValueSet\x18\x03 \x03(\t\"9\n\tStampInfo\x12\x16\n\x0eStartTimestamp\x18\x01 \x01(\t\x12\x14\n\x0c\x45ndTimestamp\x18\x02 \x01(\t\";\n\x04Rect\x12\t\n\x01X\x18\x01 \x01(\x05\x12\t\n\x01Y\x18\x02 \x01(\x05\x12\r\n\x05Width\x18\x03 \x01(\x05\x12\x0e\n\x06Height\x18\x04 \x01(\x05\"<\n\x05Rectf\x12\t\n\x01X\x18\x01 \x01(\x02\x12\t\n\x01Y\x18\x02 \x01(\x02\x12\r\n\x05Width\x18\x03 \x01(\x02\x12\x0e\n\x06Height\x18\x04 \x01(\x02\"k\n\x12TranscodeMediaInfo\x12\x18\n\x10TranscodeMediaId\x18\x01 \x01(\t\x12;\n\x14TranscodeMediaStatus\x18\x03 \x01(\x0e\x32\x1d.trpc.media.common.TaskStatus\"2\n\x0cTimeInterval\x12\x11\n\tStartTime\x18\x01 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x02 \x01(\t\",\n\x08\x44\x61yRange\x12\x10\n\x08StartDay\x18\x01 \x01(\t\x12\x0e\n\x06\x45ndDay\x18\x02 \x01(\t\"\x97\x04\n\x08TaskInfo\x12\x0e\n\x06TaskId\x18\x01 \x01(\t\x12\x10\n\x08TaskName\x18\x02 \x01(\t\x12\x11\n\tApiModule\x18\x03 \x01(\t\x12\x0f\n\x07MediaId\x18\x04 \x01(\t\x12\x11\n\tMediaName\x18\x05 \x01(\t\x12\x15\n\rMediaDuration\x18\x06 \x01(\x02\x12\x31\n\nTaskStatus\x18\x07 \x01(\x0e\x32\x1d.trpc.media.common.TaskStatus\x12\x14\n\x0cTaskProgress\x18\x08 \x01(\x02\x12\x14\n\x0cTaskTimeCost\x18\t \x01(\r\x12\x15\n\rTaskStartTime\x18\n \x01(\t\x12\x16\n\x0eTaskCreateTime\x18\x0b \x01(\t\x12\x14\n\x0c\x46\x61iledReason\x18\x0c \x01(\t\x12\x12\n\nCreateUser\x18\r \x01(\t\x12\x16\n\x0eTaskUpdateTime\x18\x0e \x01(\t\x12\x41\n\x12TranscodeMediaInfo\x18\x0f \x01(\x0b\x32%.trpc.media.common.TranscodeMediaInfo\x12\x0e\n\x06\x46lowId\x18\x10 \x01(\t\x12\x11\n\tParameter\x18\x11 \x01(\t\x12/\n\tMediaType\x18\x12 \x01(\x0e\x32\x1c.trpc.media.common.MediaType\x12\x34\n\x08MediaTag\x18\x13 \x01(\x0e\x32\".trpc.media.common.CategoryTagType*F\n\rOperateStatus\x12\x1a\n\x16OPERATE_STATUS_SUCCESS\x10\x00\x12\x19\n\x15OPERATE_STATUS_FAILED\x10\x01*\xf6\x01\n\x0f\x43\x61tegoryTagType\x12\x1b\n\x17\x43\x41TEGORY_TAG_TYPE_OTHER\x10\x00\x12\x1a\n\x16\x43\x41TEGORY_TAG_TYPE_NEWS\x10\x01\x12#\n\x1f\x43\x41TEGORY_TAG_TYPE_ENTERTAINMENT\x10\x02\x12\x1b\n\x17\x43\x41TEGORY_TAG_TYPE_MOVIE\x10\x03\x12!\n\x1d\x43\x41TEGORY_TAG_TYPE_COMPETITION\x10\x04\x12!\n\x1d\x43\x41TEGORY_TAG_TYPE_DOCUMENTARY\x10\x05\x12\"\n\x1e\x43\x41TEGORY_TAG_TYPE_INTERNETINFO\x10\x06*\xa0\x04\n\x0bMediaStatus\x12\x18\n\x14MEDIA_STATUS_INVALID\x10\x00\x12\x18\n\x14MEDIA_STATUS_CREATED\x10\x01\x12\x1f\n\x1bMEDIA_STATUS_COMMIT_SUCCESS\x10\x02\x12\x1e\n\x1aMEDIA_STATUS_COMMIT_FAILED\x10\x03\x12\x1f\n\x1bMEDIA_STATUS_IMPORT_WAITING\x10\x04\x12!\n\x1dMEDIA_STATUS_IMPORT_ANALYSING\x10\x05\x12 \n\x1cMEDIA_STATUS_IMPORT_ANALYSED\x10\x06\x12\x1e\n\x1aMEDIA_STATUS_IMPORT_FAILED\x10\x07\x12\x1e\n\x1aMEDIA_STATUS_IMPORT_STOPED\x10\x08\x12\x1d\n\x19MEDIA_STATUS_DELETED_SOFT\x10\t\x12\x1d\n\x19MEDIA_STATUS_DELETED_HARD\x10\n\x12,\n(MEDIA_STATUS_IMPORT_ANALYSING_COVER_DONE\x10\x0b\x12%\n!MEDIA_STATUS_DELETED_SOFT_WAITING\x10\x0c\x12%\n!MEDIA_STATUS_DELETED_HARD_WAITING\x10\r\x12\x1e\n\x1aMEDIA_STATUS_WAIT_DOWNLOAD\x10\x0e\x12\x1c\n\x18MEDIA_STATUS_DOWNLOADING\x10\x0f*\xcd\x01\n\tMediaType\x12\x14\n\x10MEDIA_TYPE_OTHER\x10\x00\x12\x14\n\x10MEDIA_TYPE_VIDEO\x10\x01\x12\x14\n\x10MEDIA_TYPE_IMAGE\x10\x02\x12\x14\n\x10MEDIA_TYPE_AUDIO\x10\x03\x12\x17\n\x13MEDIA_TYPE_DOCUMENT\x10\x04\x12\x19\n\x15MEDIA_TYPE_MANUSCRIPT\x10\x05\x12\x15\n\x11MEDIA_TYPE_STREAM\x10\x06\x12\x1d\n\x19MEDIA_TYPE_AI_TASK_RESULT\x10\x07*\xbe\x02\n\x0fMediaSourceType\x12\x1b\n\x17MEDIA_SOURCE_TYPE_OTHER\x10\x00\x12 \n\x1cMEDIA_SOURCE_TYPE_FRONT_PAGE\x10\x01\x12\x1a\n\x16MEDIA_SOURCE_TYPE_IVSS\x10\x02\x12\x1a\n\x16MEDIA_SOURCE_TYPE_IVSR\x10\x03\x12\x1f\n\x1bMEDIA_SOURCE_TYPE_TRANSCODE\x10\x04\x12\x1a\n\x16MEDIA_SOURCE_TYPE_IVSC\x10\x05\x12\x1a\n\x16MEDIA_SOURCE_TYPE_IVLD\x10\x06\x12#\n\x1fMEDIA_SOURCE_TYPE_EXTRACT_IMAGE\x10\x07\x12\x1b\n\x17MEDIA_SOURCE_TYPE_IVROT\x10\x08\x12\x19\n\x15MEDIA_SOURCE_TYPE_TTS\x10\t*;\n\x08LangType\x12\x16\n\x12LANG_TYPE_MANDARIN\x10\x00\x12\x17\n\x13LANG_TYPE_CANTONESE\x10\x01*\xeb\x01\n\nFilterType\x12\x15\n\x11\x46ILTER_TYPE_EQUAL\x10\x00\x12\x19\n\x15\x46ILTER_TYPE_NOT_EQUAL\x10\x01\x12\x17\n\x13\x46ILTER_TYPE_GREATER\x10\x02\x12\x1d\n\x19\x46ILTER_TYPE_GREATER_EQUAL\x10\x03\x12\x14\n\x10\x46ILTER_TYPE_LESS\x10\x04\x12\x1a\n\x16\x46ILTER_TYPE_LESS_EQUAL\x10\x05\x12\x12\n\x0e\x46ILTER_TYPE_IN\x10\x06\x12\x16\n\x12\x46ILTER_TYPE_NOT_IN\x10\x07\x12\x15\n\x11\x46ILTER_TYPE_REGEX\x10\x08*\x90\x01\n\x0cWorkflowMode\x12\x18\n\x14WORKFLOW_MODE_SYSTEM\x10\x00\x12\x1a\n\x16WORKFLOW_MODE_CUSTOMER\x10\x01\x12%\n!WORKFLOW_MODE_CUSTOMER_SUBVERSION\x10\x02\x12#\n\x1fWORKFLOW_MODE_SYSTEM_SUBVERSION\x10\x03*\xa0\x02\n\x15WorkflowComponentType\x12$\n WORKFLOW_COMPONENT_TYPE_DOWNLOAD\x10\x00\x12 \n\x1cWORKFLOW_COMPONENT_TYPE_IVLD\x10\x01\x12*\n&WORKFLOW_COMPONENT_TYPE_FORMAT_CONVERT\x10\x02\x12\x33\n/WORKFLOW_COMPONENT_TYPE_VIDEO_QUALITY_EVALUTION\x10\x03\x12,\n(WORKFLOW_COMPONENT_TYPE_PERSON_RETRIEVAL\x10\x04\x12\x30\n,WORKFLOW_COMPONENT_TYPE_VIDEO_CONTENT_SAFETY\x10\x05*1\n\x08SortType\x12\x11\n\rSORT_TYPE_ASC\x10\x00\x12\x12\n\x0eSORT_TYPE_DESC\x10\x01*8\n\nDeleteType\x12\x14\n\x10\x44\x45LETE_TYPE_SOFT\x10\x00\x12\x14\n\x10\x44\x45LETE_TYPE_HARD\x10\x01*R\n\x08\x42indType\x12\x13\n\x0f\x42IND_TYPE_COVER\x10\x00\x12\x18\n\x14\x42IND_TYPE_SUBVERSION\x10\x01\x12\x17\n\x13\x42IND_TYPE_TRANSCODE\x10\x02*\xdc\x01\n\x0f\x44omainGroupType\x12\x1d\n\x19\x44OMAIN_GROUP_TYPE_PRIVATE\x10\x00\x12\x1c\n\x18\x44OMAIN_GROUP_TYPE_PUBLIC\x10\x01\x12#\n\x1f\x44OMAIN_GROUP_TYPE_PUBLIC_CENTER\x10\x02\x12\'\n#DOMAIN_GROUP_TYPE_PUBLIC_DEPARTMENT\x10\x03\x12!\n\x1d\x44OMAIN_GROUP_TYPE_INDEPENDENT\x10\x04\x12\x1b\n\x17\x44OMAIN_GROUP_TYPE_GROUP\x10\x05*\x7f\n\x11RetrieveInputType\x12\x1c\n\x18RETRIEVE_INPUT_TYPE_TEXT\x10\x00\x12&\n\"RETRIEVE_INPUT_TYPE_IMAGE_MEDIA_ID\x10\x01\x12$\n RETRIEVE_INPUT_TYPE_IMAGE_BASE64\x10\x02*b\n\x15RetrieveHitSourceType\x12$\n RETRIEVE_HIT_SOURCE_TYPE_DEFAULT\x10\x00\x12#\n\x1fRETRIEVE_HIT_SOURCE_TYPE_ENGINE\x10\x01*R\n\x10\x45xtractImageType\x12\x1d\n\x19\x45XTRACT_IMAGE_TYPE_BASE64\x10\x00\x12\x1f\n\x1b\x45XTRACT_IMAGE_TYPE_MEDIA_ID\x10\x01*\xdd\x01\n\x16WorkflowTemplateStatus\x12!\n\x1dWORKFLOW_TEMPLATE_STATUS_INIT\x10\x00\x12%\n!WORKFLOW_TEMPLATE_STATUS_INACTIVE\x10\x01\x12#\n\x1fWORKFLOW_TEMPLATE_STATUS_ACTIVE\x10\x02\x12)\n%WORKFLOW_TEMPLATE_STATUS_DELETED_SOFT\x10\x03\x12)\n%WORKFLOW_TEMPLATE_STATUS_DELETED_HARD\x10\x04*O\n\x0fRetrieveTagType\x12\x1e\n\x1aRETRIEVE_TAG_TYPE_LANDMARK\x10\x00\x12\x1c\n\x18RETRIEVE_TAG_TYPE_PERSON\x10\x01*\x89\x02\n\nTaskStatus\x12\x17\n\x13TASK_STATUS_INVALID\x10\x00\x12\x17\n\x13TASK_STATUS_CREATED\x10\x01\x12\x17\n\x13TASK_STATUS_WAITING\x10\x02\x12\x19\n\x15TASK_STATUS_ANALYSING\x10\x03\x12\x18\n\x14TASK_STATUS_ANALYSED\x10\x04\x12\x16\n\x12TASK_STATUS_FAILED\x10\x05\x12\x16\n\x12TASK_STATUS_STOPED\x10\x06\x12\x17\n\x13TASK_STATUS_DELETED\x10\x07\x12\x19\n\x15TASK_STATUS_EXPORTING\x10\x08\x12\x17\n\x13TASK_STATUS_CLEANED\x10\tBYZWgithub.com/Tencent-media-asset-system-sdk/media-platform-sdk-go/protobuf-spec/apicommonb\x06proto3')

_OPERATESTATUS = DESCRIPTOR.enum_types_by_name['OperateStatus']
OperateStatus = enum_type_wrapper.EnumTypeWrapper(_OPERATESTATUS)
_CATEGORYTAGTYPE = DESCRIPTOR.enum_types_by_name['CategoryTagType']
CategoryTagType = enum_type_wrapper.EnumTypeWrapper(_CATEGORYTAGTYPE)
_MEDIASTATUS = DESCRIPTOR.enum_types_by_name['MediaStatus']
MediaStatus = enum_type_wrapper.EnumTypeWrapper(_MEDIASTATUS)
_MEDIATYPE = DESCRIPTOR.enum_types_by_name['MediaType']
MediaType = enum_type_wrapper.EnumTypeWrapper(_MEDIATYPE)
_MEDIASOURCETYPE = DESCRIPTOR.enum_types_by_name['MediaSourceType']
MediaSourceType = enum_type_wrapper.EnumTypeWrapper(_MEDIASOURCETYPE)
_LANGTYPE = DESCRIPTOR.enum_types_by_name['LangType']
LangType = enum_type_wrapper.EnumTypeWrapper(_LANGTYPE)
_FILTERTYPE = DESCRIPTOR.enum_types_by_name['FilterType']
FilterType = enum_type_wrapper.EnumTypeWrapper(_FILTERTYPE)
_WORKFLOWMODE = DESCRIPTOR.enum_types_by_name['WorkflowMode']
WorkflowMode = enum_type_wrapper.EnumTypeWrapper(_WORKFLOWMODE)
_WORKFLOWCOMPONENTTYPE = DESCRIPTOR.enum_types_by_name['WorkflowComponentType']
WorkflowComponentType = enum_type_wrapper.EnumTypeWrapper(_WORKFLOWCOMPONENTTYPE)
_SORTTYPE = DESCRIPTOR.enum_types_by_name['SortType']
SortType = enum_type_wrapper.EnumTypeWrapper(_SORTTYPE)
_DELETETYPE = DESCRIPTOR.enum_types_by_name['DeleteType']
DeleteType = enum_type_wrapper.EnumTypeWrapper(_DELETETYPE)
_BINDTYPE = DESCRIPTOR.enum_types_by_name['BindType']
BindType = enum_type_wrapper.EnumTypeWrapper(_BINDTYPE)
_DOMAINGROUPTYPE = DESCRIPTOR.enum_types_by_name['DomainGroupType']
DomainGroupType = enum_type_wrapper.EnumTypeWrapper(_DOMAINGROUPTYPE)
_RETRIEVEINPUTTYPE = DESCRIPTOR.enum_types_by_name['RetrieveInputType']
RetrieveInputType = enum_type_wrapper.EnumTypeWrapper(_RETRIEVEINPUTTYPE)
_RETRIEVEHITSOURCETYPE = DESCRIPTOR.enum_types_by_name['RetrieveHitSourceType']
RetrieveHitSourceType = enum_type_wrapper.EnumTypeWrapper(_RETRIEVEHITSOURCETYPE)
_EXTRACTIMAGETYPE = DESCRIPTOR.enum_types_by_name['ExtractImageType']
ExtractImageType = enum_type_wrapper.EnumTypeWrapper(_EXTRACTIMAGETYPE)
_WORKFLOWTEMPLATESTATUS = DESCRIPTOR.enum_types_by_name['WorkflowTemplateStatus']
WorkflowTemplateStatus = enum_type_wrapper.EnumTypeWrapper(_WORKFLOWTEMPLATESTATUS)
_RETRIEVETAGTYPE = DESCRIPTOR.enum_types_by_name['RetrieveTagType']
RetrieveTagType = enum_type_wrapper.EnumTypeWrapper(_RETRIEVETAGTYPE)
_TASKSTATUS = DESCRIPTOR.enum_types_by_name['TaskStatus']
TaskStatus = enum_type_wrapper.EnumTypeWrapper(_TASKSTATUS)
OPERATE_STATUS_SUCCESS = 0
OPERATE_STATUS_FAILED = 1
CATEGORY_TAG_TYPE_OTHER = 0
CATEGORY_TAG_TYPE_NEWS = 1
CATEGORY_TAG_TYPE_ENTERTAINMENT = 2
CATEGORY_TAG_TYPE_MOVIE = 3
CATEGORY_TAG_TYPE_COMPETITION = 4
CATEGORY_TAG_TYPE_DOCUMENTARY = 5
CATEGORY_TAG_TYPE_INTERNETINFO = 6
MEDIA_STATUS_INVALID = 0
MEDIA_STATUS_CREATED = 1
MEDIA_STATUS_COMMIT_SUCCESS = 2
MEDIA_STATUS_COMMIT_FAILED = 3
MEDIA_STATUS_IMPORT_WAITING = 4
MEDIA_STATUS_IMPORT_ANALYSING = 5
MEDIA_STATUS_IMPORT_ANALYSED = 6
MEDIA_STATUS_IMPORT_FAILED = 7
MEDIA_STATUS_IMPORT_STOPED = 8
MEDIA_STATUS_DELETED_SOFT = 9
MEDIA_STATUS_DELETED_HARD = 10
MEDIA_STATUS_IMPORT_ANALYSING_COVER_DONE = 11
MEDIA_STATUS_DELETED_SOFT_WAITING = 12
MEDIA_STATUS_DELETED_HARD_WAITING = 13
MEDIA_STATUS_WAIT_DOWNLOAD = 14
MEDIA_STATUS_DOWNLOADING = 15
MEDIA_TYPE_OTHER = 0
MEDIA_TYPE_VIDEO = 1
MEDIA_TYPE_IMAGE = 2
MEDIA_TYPE_AUDIO = 3
MEDIA_TYPE_DOCUMENT = 4
MEDIA_TYPE_MANUSCRIPT = 5
MEDIA_TYPE_STREAM = 6
MEDIA_TYPE_AI_TASK_RESULT = 7
MEDIA_SOURCE_TYPE_OTHER = 0
MEDIA_SOURCE_TYPE_FRONT_PAGE = 1
MEDIA_SOURCE_TYPE_IVSS = 2
MEDIA_SOURCE_TYPE_IVSR = 3
MEDIA_SOURCE_TYPE_TRANSCODE = 4
MEDIA_SOURCE_TYPE_IVSC = 5
MEDIA_SOURCE_TYPE_IVLD = 6
MEDIA_SOURCE_TYPE_EXTRACT_IMAGE = 7
MEDIA_SOURCE_TYPE_IVROT = 8
MEDIA_SOURCE_TYPE_TTS = 9
LANG_TYPE_MANDARIN = 0
LANG_TYPE_CANTONESE = 1
FILTER_TYPE_EQUAL = 0
FILTER_TYPE_NOT_EQUAL = 1
FILTER_TYPE_GREATER = 2
FILTER_TYPE_GREATER_EQUAL = 3
FILTER_TYPE_LESS = 4
FILTER_TYPE_LESS_EQUAL = 5
FILTER_TYPE_IN = 6
FILTER_TYPE_NOT_IN = 7
FILTER_TYPE_REGEX = 8
WORKFLOW_MODE_SYSTEM = 0
WORKFLOW_MODE_CUSTOMER = 1
WORKFLOW_MODE_CUSTOMER_SUBVERSION = 2
WORKFLOW_MODE_SYSTEM_SUBVERSION = 3
WORKFLOW_COMPONENT_TYPE_DOWNLOAD = 0
WORKFLOW_COMPONENT_TYPE_IVLD = 1
WORKFLOW_COMPONENT_TYPE_FORMAT_CONVERT = 2
WORKFLOW_COMPONENT_TYPE_VIDEO_QUALITY_EVALUTION = 3
WORKFLOW_COMPONENT_TYPE_PERSON_RETRIEVAL = 4
WORKFLOW_COMPONENT_TYPE_VIDEO_CONTENT_SAFETY = 5
SORT_TYPE_ASC = 0
SORT_TYPE_DESC = 1
DELETE_TYPE_SOFT = 0
DELETE_TYPE_HARD = 1
BIND_TYPE_COVER = 0
BIND_TYPE_SUBVERSION = 1
BIND_TYPE_TRANSCODE = 2
DOMAIN_GROUP_TYPE_PRIVATE = 0
DOMAIN_GROUP_TYPE_PUBLIC = 1
DOMAIN_GROUP_TYPE_PUBLIC_CENTER = 2
DOMAIN_GROUP_TYPE_PUBLIC_DEPARTMENT = 3
DOMAIN_GROUP_TYPE_INDEPENDENT = 4
DOMAIN_GROUP_TYPE_GROUP = 5
RETRIEVE_INPUT_TYPE_TEXT = 0
RETRIEVE_INPUT_TYPE_IMAGE_MEDIA_ID = 1
RETRIEVE_INPUT_TYPE_IMAGE_BASE64 = 2
RETRIEVE_HIT_SOURCE_TYPE_DEFAULT = 0
RETRIEVE_HIT_SOURCE_TYPE_ENGINE = 1
EXTRACT_IMAGE_TYPE_BASE64 = 0
EXTRACT_IMAGE_TYPE_MEDIA_ID = 1
WORKFLOW_TEMPLATE_STATUS_INIT = 0
WORKFLOW_TEMPLATE_STATUS_INACTIVE = 1
WORKFLOW_TEMPLATE_STATUS_ACTIVE = 2
WORKFLOW_TEMPLATE_STATUS_DELETED_SOFT = 3
WORKFLOW_TEMPLATE_STATUS_DELETED_HARD = 4
RETRIEVE_TAG_TYPE_LANDMARK = 0
RETRIEVE_TAG_TYPE_PERSON = 1
TASK_STATUS_INVALID = 0
TASK_STATUS_CREATED = 1
TASK_STATUS_WAITING = 2
TASK_STATUS_ANALYSING = 3
TASK_STATUS_ANALYSED = 4
TASK_STATUS_FAILED = 5
TASK_STATUS_STOPED = 6
TASK_STATUS_DELETED = 7
TASK_STATUS_EXPORTING = 8
TASK_STATUS_CLEANED = 9


_OPERATERESPONSE = DESCRIPTOR.message_types_by_name['OperateResponse']
_TASKTEMPLATE = DESCRIPTOR.message_types_by_name['TaskTemplate']
_FLOWDIRECTION = DESCRIPTOR.message_types_by_name['FlowDirection']
_WORKFLOWTEMPLATE = DESCRIPTOR.message_types_by_name['WorkflowTemplate']
_DOMAINGROUPINFO = DESCRIPTOR.message_types_by_name['DomainGroupInfo']
_FILTER = DESCRIPTOR.message_types_by_name['Filter']
_SORTER = DESCRIPTOR.message_types_by_name['Sorter']
_USERINFO = DESCRIPTOR.message_types_by_name['UserInfo']
_DELETER = DESCRIPTOR.message_types_by_name['Deleter']
_STAMPINFO = DESCRIPTOR.message_types_by_name['StampInfo']
_RECT = DESCRIPTOR.message_types_by_name['Rect']
_RECTF = DESCRIPTOR.message_types_by_name['Rectf']
_TRANSCODEMEDIAINFO = DESCRIPTOR.message_types_by_name['TranscodeMediaInfo']
_TIMEINTERVAL = DESCRIPTOR.message_types_by_name['TimeInterval']
_DAYRANGE = DESCRIPTOR.message_types_by_name['DayRange']
_TASKINFO = DESCRIPTOR.message_types_by_name['TaskInfo']
OperateResponse = _reflection.GeneratedProtocolMessageType('OperateResponse', (_message.Message,), {
  'DESCRIPTOR' : _OPERATERESPONSE,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.OperateResponse)
  })
_sym_db.RegisterMessage(OperateResponse)

TaskTemplate = _reflection.GeneratedProtocolMessageType('TaskTemplate', (_message.Message,), {
  'DESCRIPTOR' : _TASKTEMPLATE,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.TaskTemplate)
  })
_sym_db.RegisterMessage(TaskTemplate)

FlowDirection = _reflection.GeneratedProtocolMessageType('FlowDirection', (_message.Message,), {
  'DESCRIPTOR' : _FLOWDIRECTION,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.FlowDirection)
  })
_sym_db.RegisterMessage(FlowDirection)

WorkflowTemplate = _reflection.GeneratedProtocolMessageType('WorkflowTemplate', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWTEMPLATE,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.WorkflowTemplate)
  })
_sym_db.RegisterMessage(WorkflowTemplate)

DomainGroupInfo = _reflection.GeneratedProtocolMessageType('DomainGroupInfo', (_message.Message,), {
  'DESCRIPTOR' : _DOMAINGROUPINFO,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.DomainGroupInfo)
  })
_sym_db.RegisterMessage(DomainGroupInfo)

Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), {
  'DESCRIPTOR' : _FILTER,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.Filter)
  })
_sym_db.RegisterMessage(Filter)

Sorter = _reflection.GeneratedProtocolMessageType('Sorter', (_message.Message,), {
  'DESCRIPTOR' : _SORTER,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.Sorter)
  })
_sym_db.RegisterMessage(Sorter)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)

Deleter = _reflection.GeneratedProtocolMessageType('Deleter', (_message.Message,), {
  'DESCRIPTOR' : _DELETER,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.Deleter)
  })
_sym_db.RegisterMessage(Deleter)

StampInfo = _reflection.GeneratedProtocolMessageType('StampInfo', (_message.Message,), {
  'DESCRIPTOR' : _STAMPINFO,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.StampInfo)
  })
_sym_db.RegisterMessage(StampInfo)

Rect = _reflection.GeneratedProtocolMessageType('Rect', (_message.Message,), {
  'DESCRIPTOR' : _RECT,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.Rect)
  })
_sym_db.RegisterMessage(Rect)

Rectf = _reflection.GeneratedProtocolMessageType('Rectf', (_message.Message,), {
  'DESCRIPTOR' : _RECTF,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.Rectf)
  })
_sym_db.RegisterMessage(Rectf)

TranscodeMediaInfo = _reflection.GeneratedProtocolMessageType('TranscodeMediaInfo', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCODEMEDIAINFO,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.TranscodeMediaInfo)
  })
_sym_db.RegisterMessage(TranscodeMediaInfo)

TimeInterval = _reflection.GeneratedProtocolMessageType('TimeInterval', (_message.Message,), {
  'DESCRIPTOR' : _TIMEINTERVAL,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.TimeInterval)
  })
_sym_db.RegisterMessage(TimeInterval)

DayRange = _reflection.GeneratedProtocolMessageType('DayRange', (_message.Message,), {
  'DESCRIPTOR' : _DAYRANGE,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.DayRange)
  })
_sym_db.RegisterMessage(DayRange)

TaskInfo = _reflection.GeneratedProtocolMessageType('TaskInfo', (_message.Message,), {
  'DESCRIPTOR' : _TASKINFO,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.common.TaskInfo)
  })
_sym_db.RegisterMessage(TaskInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZWgithub.com/Tencent-media-asset-system-sdk/media-platform-sdk-go/protobuf-spec/apicommon'
  _OPERATESTATUS._serialized_start=1851
  _OPERATESTATUS._serialized_end=1921
  _CATEGORYTAGTYPE._serialized_start=1924
  _CATEGORYTAGTYPE._serialized_end=2170
  _MEDIASTATUS._serialized_start=2173
  _MEDIASTATUS._serialized_end=2717
  _MEDIATYPE._serialized_start=2720
  _MEDIATYPE._serialized_end=2925
  _MEDIASOURCETYPE._serialized_start=2928
  _MEDIASOURCETYPE._serialized_end=3246
  _LANGTYPE._serialized_start=3248
  _LANGTYPE._serialized_end=3307
  _FILTERTYPE._serialized_start=3310
  _FILTERTYPE._serialized_end=3545
  _WORKFLOWMODE._serialized_start=3548
  _WORKFLOWMODE._serialized_end=3692
  _WORKFLOWCOMPONENTTYPE._serialized_start=3695
  _WORKFLOWCOMPONENTTYPE._serialized_end=3983
  _SORTTYPE._serialized_start=3985
  _SORTTYPE._serialized_end=4034
  _DELETETYPE._serialized_start=4036
  _DELETETYPE._serialized_end=4092
  _BINDTYPE._serialized_start=4094
  _BINDTYPE._serialized_end=4176
  _DOMAINGROUPTYPE._serialized_start=4179
  _DOMAINGROUPTYPE._serialized_end=4399
  _RETRIEVEINPUTTYPE._serialized_start=4401
  _RETRIEVEINPUTTYPE._serialized_end=4528
  _RETRIEVEHITSOURCETYPE._serialized_start=4530
  _RETRIEVEHITSOURCETYPE._serialized_end=4628
  _EXTRACTIMAGETYPE._serialized_start=4630
  _EXTRACTIMAGETYPE._serialized_end=4712
  _WORKFLOWTEMPLATESTATUS._serialized_start=4715
  _WORKFLOWTEMPLATESTATUS._serialized_end=4936
  _RETRIEVETAGTYPE._serialized_start=4938
  _RETRIEVETAGTYPE._serialized_end=5017
  _TASKSTATUS._serialized_start=5020
  _TASKSTATUS._serialized_end=5285
  _OPERATERESPONSE._serialized_start=92
  _OPERATERESPONSE._serialized_end=181
  _TASKTEMPLATE._serialized_start=183
  _TASKTEMPLATE._serialized_end=299
  _FLOWDIRECTION._serialized_start=301
  _FLOWDIRECTION._serialized_end=352
  _WORKFLOWTEMPLATE._serialized_start=355
  _WORKFLOWTEMPLATE._serialized_end=491
  _DOMAINGROUPINFO._serialized_start=493
  _DOMAINGROUPINFO._serialized_end=616
  _FILTER._serialized_start=618
  _FILTER._serialized_end=709
  _SORTER._serialized_start=711
  _SORTER._serialized_end=780
  _USERINFO._serialized_start=782
  _USERINFO._serialized_end=828
  _DELETER._serialized_start=830
  _DELETER._serialized_end=922
  _STAMPINFO._serialized_start=924
  _STAMPINFO._serialized_end=981
  _RECT._serialized_start=983
  _RECT._serialized_end=1042
  _RECTF._serialized_start=1044
  _RECTF._serialized_end=1104
  _TRANSCODEMEDIAINFO._serialized_start=1106
  _TRANSCODEMEDIAINFO._serialized_end=1213
  _TIMEINTERVAL._serialized_start=1215
  _TIMEINTERVAL._serialized_end=1265
  _DAYRANGE._serialized_start=1267
  _DAYRANGE._serialized_end=1311
  _TASKINFO._serialized_start=1314
  _TASKINFO._serialized_end=1849
# @@protoc_insertion_point(module_scope)
