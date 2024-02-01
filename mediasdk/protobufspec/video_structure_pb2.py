# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: video_structure.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15video_structure.proto\x12\x19trpc.media.videostructure\x1a\x0c\x63ommon.proto\"W\n\tAudioInfo\x12\x0f\n\x07\x43ontent\x18\x01 \x01(\t\x12\x16\n\x0eStartTimeStamp\x18\x02 \x01(\x02\x12\x14\n\x0c\x45ndTimeStamp\x18\x03 \x01(\x02\x12\x0b\n\x03Tag\x18\x04 \x01(\t\"V\n\x08TextInfo\x12\x0b\n\x03Tag\x18\x01 \x01(\t\x12\x0f\n\x07\x43ontent\x18\x02 \x01(\t\x12\x16\n\x0eStartTimeStamp\x18\x03 \x01(\x02\x12\x14\n\x0c\x45ndTimeStamp\x18\x04 \x01(\x02\"]\n\x0f\x41ppearFrameInfo\x12%\n\x04Rect\x18\x01 \x01(\x0b\x32\x17.trpc.media.common.Rect\x12\x12\n\nFrameIndex\x18\x02 \x01(\t\x12\x0f\n\x07Quality\x18\x03 \x01(\x02\"\xda\x01\n\x0e\x41ppearTimeInfo\x12\x16\n\x0eStartTimeStamp\x18\x01 \x01(\x02\x12\x14\n\x0c\x45ndTimeStamp\x18\x02 \x01(\x02\x12\x14\n\x0cImageMediaId\x18\x03 \x01(\t\x12\x12\n\nConfidence\x18\x04 \x01(\x02\x12\x17\n\x0fStartFrameIndex\x18\x05 \x01(\t\x12\x15\n\rEndFrameIndex\x18\x06 \x01(\t\x12@\n\x0c\x44\x65tailFrames\x18\x07 \x03(\x0b\x32*.trpc.media.videostructure.AppearFrameInfo\"N\n\x11\x41ppearPostionInfo\x12\r\n\x05Index\x18\x01 \x01(\x05\x12\x15\n\rStartPosition\x18\x02 \x01(\x05\x12\x13\n\x0b\x45ndPosition\x18\x03 \x01(\x05\"\xe3\x02\n\rPersonTagInfo\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x0b\n\x03Job\x18\x02 \x01(\t\x12\x16\n\x0e\x46irstAppearTab\x18\x03 \x01(\t\x12\x44\n\x0e\x41udioAppearSet\x18\x04 \x03(\x0b\x32,.trpc.media.videostructure.AppearPostionInfo\x12\x43\n\rTextAppearSet\x18\x05 \x03(\x0b\x32,.trpc.media.videostructure.AppearPostionInfo\x12\x42\n\x0fVisionAppearSet\x18\x06 \x03(\x0b\x32).trpc.media.videostructure.AppearTimeInfo\x12+\n\nAppearRect\x18\x07 \x01(\x0b\x32\x17.trpc.media.common.Rect\x12\x11\n\tSensitive\x18\x08 \x01(\x05\x12\x10\n\x08PersonID\x18\t \x01(\t\"\x84\x01\n\x16L1ClassifiedPersonInfo\x12\x14\n\x0c\x43lassifyName\x18\x01 \x01(\t\x12T\n\x19L2ClassifiedPersonInfoSet\x18\x02 \x03(\x0b\x32\x31.trpc.media.videostructure.L2ClassifiedPersonInfo\"k\n\x16L2ClassifiedPersonInfo\x12\x14\n\x0c\x43lassifyName\x18\x01 \x01(\t\x12;\n\tPersonSet\x18\x02 \x03(\x0b\x32(.trpc.media.videostructure.PersonTagInfo\"\xc7\x01\n\rUnknownPerson\x12\x42\n\x0fVisionAppearSet\x18\x01 \x03(\x0b\x32).trpc.media.videostructure.AppearTimeInfo\x12\x19\n\x11PutLibraryAllowed\x18\x02 \x01(\x08\x12+\n\nAppearRect\x18\x03 \x01(\x0b\x32\x17.trpc.media.common.Rect\x12\x11\n\tSensitive\x18\x04 \x01(\x05\x12\x17\n\x0fUnknownPersonID\x18\x05 \x01(\t\"\x85\x03\n\rMultiLevelTag\x12\x0f\n\x07TagName\x18\x01 \x01(\t\x12;\n\tSubTagSet\x18\x02 \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12\r\n\x05Level\x18\x03 \x01(\x05\x12\x16\n\x0e\x46irstAppearTab\x18\x04 \x01(\t\x12\x44\n\x0e\x41udioAppearSet\x18\x05 \x03(\x0b\x32,.trpc.media.videostructure.AppearPostionInfo\x12\x43\n\rTextAppearSet\x18\x06 \x03(\x0b\x32,.trpc.media.videostructure.AppearPostionInfo\x12\x42\n\x0fVisionAppearSet\x18\x07 \x03(\x0b\x32).trpc.media.videostructure.AppearTimeInfo\x12\r\n\x05Score\x18\x08 \x01(\x01\x12\x13\n\x0bIsSensitive\x18\t \x01(\x08\x12\x0c\n\x04Rank\x18\n \x01(\x05\"\xf9\x03\n\nMajorEvent\x12\x11\n\tEventName\x18\x01 \x01(\t\x12>\n\x0c\x45ventTimeSet\x18\x02 \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12?\n\rEventPlaceSet\x18\x03 \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12\x46\n\x14\x45ventOrganizationSet\x18\x04 \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12@\n\x0e\x45ventPersonSet\x18\x05 \x03(\x0b\x32(.trpc.media.videostructure.PersonTagInfo\x12\x37\n\x05\x45vent\x18\x06 \x01(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12H\n\x16\x45ventVictimPositionSet\x18\x07 \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12J\n\x18\x45ventCriminalPositionSet\x18\x08 \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\"\x8e\x04\n\nAILensInfo\x12\x0c\n\x04Type\x18\x01 \x01(\t\x12\x14\n\x0cImageMediaId\x18\x02 \x01(\t\x12\x16\n\x0eStartTimeStamp\x18\x03 \x01(\x02\x12\x14\n\x0c\x45ndTimeStamp\x18\x04 \x01(\x02\x12R\n\x17\x43lassifiedPersonInfoSet\x18\x05 \x03(\x0b\x32\x31.trpc.media.videostructure.L1ClassifiedPersonInfo\x12<\n\nTextTagSet\x18\x06 \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12=\n\x0b\x46rameTagSet\x18\x07 \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12\x0f\n\x07Scenery\x18\x08 \x01(\t\x12\x14\n\x0c\x46ilmingAngle\x18\t \x01(\t\x12\x14\n\x0cShootingMode\x18\n \x01(\t\x12\x17\n\x0f\x41uxiliaryTagSet\x18\x0b \x03(\t\x12\n\n\x02ID\x18\x0c \x01(\t\x12\r\n\x05Title\x18\r \x01(\t\x12\x42\n\x10UnknownPersonSet\x18\x0e \x03(\x0b\x32(.trpc.media.videostructure.UnknownPerson\x12\x13\n\x0bSceneryShot\x18\x0f \x01(\t\x12\x13\n\x0b\x41\x63tualSound\x18\x10 \x01(\x08\"\xfb\x03\n\x0b\x41ISceneInfo\x12\x0c\n\x04Type\x18\x01 \x01(\t\x12\x14\n\x0cImageMediaId\x18\x02 \x01(\t\x12\x16\n\x0eStartTimeStamp\x18\x03 \x01(\x02\x12\x14\n\x0c\x45ndTimeStamp\x18\x04 \x01(\x02\x12R\n\x17\x43lassifiedPersonInfoSet\x18\x05 \x03(\x0b\x32\x31.trpc.media.videostructure.L1ClassifiedPersonInfo\x12<\n\nTextTagSet\x18\x06 \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12=\n\x0b\x46rameTagSet\x18\x07 \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12\x13\n\x0b\x46ineGrained\x18\x08 \x01(\t\x12\x14\n\x0cLensIndexSet\x18\t \x03(\x05\x12\n\n\x02ID\x18\n \x01(\t\x12\x42\n\x10UnknownPersonSet\x18\x0b \x03(\x0b\x32(.trpc.media.videostructure.UnknownPerson\x12N\n\x13SuspiciousPersonSet\x18\x0c \x03(\x0b\x32\x31.trpc.media.videostructure.L1ClassifiedPersonInfo\"\x95\x06\n\rAISnippetInfo\x12\x0c\n\x04Type\x18\x02 \x01(\t\x12\x14\n\x0cImageMediaId\x18\x03 \x01(\t\x12\x16\n\x0eStartTimeStamp\x18\x04 \x01(\x02\x12\x14\n\x0c\x45ndTimeStamp\x18\x05 \x01(\x02\x12\x10\n\x08TitleSet\x18\x06 \x03(\t\x12\x12\n\nSummarySet\x18\x07 \x03(\t\x12=\n\x0bHostInfoSet\x18\x08 \x03(\x0b\x32(.trpc.media.videostructure.PersonTagInfo\x12\x41\n\x0fReporterInfoSet\x18\t \x03(\x0b\x32(.trpc.media.videostructure.PersonTagInfo\x12R\n\x17\x43lassifiedPersonInfoSet\x18\n \x03(\x0b\x32\x31.trpc.media.videostructure.L1ClassifiedPersonInfo\x12<\n\nTextTagSet\x18\x0b \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12=\n\x0b\x46rameTagSet\x18\x0c \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12\x15\n\rSummaryTagSet\x18\r \x03(\t\x12\x15\n\rSceneIndexSet\x18\x0e \x03(\x05\x12\x14\n\x0cLensIndexSet\x18\x0f \x03(\x05\x12\n\n\x02ID\x18\x10 \x01(\t\x12<\n\rMajorEventSet\x18\x11 \x03(\x0b\x32%.trpc.media.videostructure.MajorEvent\x12\x17\n\x0fShortSummarySet\x18\x12 \x03(\t\x12\x42\n\x10UnknownPersonSet\x18\x13 \x03(\x0b\x32(.trpc.media.videostructure.UnknownPerson\x12N\n\x13SuspiciousPersonSet\x18\x14 \x03(\x0b\x32\x31.trpc.media.videostructure.L1ClassifiedPersonInfo\"Q\n\x10\x41udioCaptionInfo\x12\x16\n\x0eStartTimeStamp\x18\x01 \x01(\x02\x12\x14\n\x0c\x45ndTimeStamp\x18\x02 \x01(\x02\x12\x0f\n\x07\x43ontent\x18\x03 \x01(\t\"\xc8\x07\n\x08ShowInfo\x12\x30\n\x04Type\x18\x01 \x01(\x0e\x32\".trpc.media.common.CategoryTagType\x12\x0c\n\x04\x44\x61te\x18\x02 \x01(\t\x12\x0c\n\x04Logo\x18\x03 \x01(\t\x12\x0e\n\x06\x43olumn\x18\x04 \x01(\t\x12\x0e\n\x06Source\x18\x05 \x01(\t\x12\x14\n\x0cImageMediaId\x18\x06 \x01(\t\x12\x12\n\nSummarySet\x18\x07 \x03(\t\x12\x10\n\x08TitleSet\x18\x08 \x03(\t\x12:\n\x0c\x41udioInfoSet\x18\t \x03(\x0b\x32$.trpc.media.videostructure.AudioInfo\x12\x38\n\x0bTextInfoSet\x18\n \x03(\x0b\x32#.trpc.media.videostructure.TextInfo\x12=\n\x0bHostInfoSet\x18\x0b \x03(\x0b\x32(.trpc.media.videostructure.PersonTagInfo\x12\x41\n\x0fReporterInfoSet\x18\x0c \x03(\x0b\x32(.trpc.media.videostructure.PersonTagInfo\x12R\n\x17\x43lassifiedPersonInfoSet\x18\r \x03(\x0b\x32\x31.trpc.media.videostructure.L1ClassifiedPersonInfo\x12<\n\nTextTagSet\x18\x0e \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12=\n\x0b\x46rameTagSet\x18\x0f \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12\x1a\n\x12MediaClassifierSet\x18\x11 \x03(\t\x12\x15\n\rSummaryTagSet\x18\x12 \x03(\t\x12\x42\n\x10UnknownPersonSet\x18\x13 \x03(\x0b\x32(.trpc.media.videostructure.UnknownPerson\x12\x44\n\x0f\x41udioCaptionSet\x18\x14 \x03(\x0b\x32+.trpc.media.videostructure.AudioCaptionInfo\x12<\n\rSymbolInfoSet\x18\x15 \x03(\x0b\x32%.trpc.media.videostructure.SymbolInfo\x12N\n\x13SuspiciousPersonSet\x18\x16 \x03(\x0b\x32\x31.trpc.media.videostructure.L1ClassifiedPersonInfo\"H\n\x08ImageOcr\x12\x0f\n\x07\x43ontent\x18\x01 \x01(\t\x12+\n\nAppearRect\x18\x02 \x01(\x0b\x32\x17.trpc.media.common.Rect\"F\n\tImageLogo\x12\x0c\n\x04Logo\x18\x01 \x01(\t\x12+\n\nAppearRect\x18\x02 \x01(\x0b\x32\x17.trpc.media.common.Rect\"F\n\rAITagTaskData\x12\x35\n\x08ShowInfo\x18\x01 \x01(\x0b\x32#.trpc.media.videostructure.ShowInfo\"\xd4\x01\n\x12\x41ITagAudioTaskData\x12:\n\x0c\x41udioInfoSet\x18\x01 \x03(\x0b\x32$.trpc.media.videostructure.AudioInfo\x12<\n\nTextTagSet\x18\x02 \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12\x44\n\x0f\x41udioCaptionSet\x18\x03 \x03(\x0b\x32+.trpc.media.videostructure.AudioCaptionInfo\"s\n\x11\x41ITagTextTaskData\x12\x0f\n\x07\x43ontent\x18\x01 \x01(\t\x12\x0f\n\x07Summary\x18\x02 \x01(\t\x12<\n\nTextTagSet\x18\x03 \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\"\x9e\x04\n\x12\x41ITagImageTaskData\x12\x33\n\x06OcrSet\x18\x01 \x03(\x0b\x32#.trpc.media.videostructure.ImageOcr\x12=\n\x0b\x46rameTagSet\x18\x02 \x03(\x0b\x32(.trpc.media.videostructure.MultiLevelTag\x12R\n\x17\x43lassifiedPersonInfoSet\x18\x03 \x03(\x0b\x32\x31.trpc.media.videostructure.L1ClassifiedPersonInfo\x12\x34\n\x06TvLogo\x18\x04 \x01(\x0b\x32$.trpc.media.videostructure.ImageLogo\x12\x38\n\nSourceLogo\x18\x05 \x01(\x0b\x32$.trpc.media.videostructure.ImageLogo\x12\x42\n\x10UnknownPersonSet\x18\x06 \x03(\x0b\x32(.trpc.media.videostructure.UnknownPerson\x12<\n\rSymbolInfoSet\x18\x07 \x03(\x0b\x32%.trpc.media.videostructure.SymbolInfo\x12N\n\x13SuspiciousPersonSet\x18\x08 \x03(\x0b\x32\x31.trpc.media.videostructure.L1ClassifiedPersonInfo\"\x86\x02\n\x11\x41ICatalogTaskData\x12\x35\n\x08ShowInfo\x18\x01 \x01(\x0b\x32#.trpc.media.videostructure.ShowInfo\x12@\n\x0eSnippetInfoSet\x18\x02 \x03(\x0b\x32(.trpc.media.videostructure.AISnippetInfo\x12<\n\x0cSceneInfoSet\x18\x03 \x03(\x0b\x32&.trpc.media.videostructure.AISceneInfo\x12:\n\x0bLensInfoSet\x18\x04 \x03(\x0b\x32%.trpc.media.videostructure.AILensInfo\"\x88\x01\n\rAICutTaskData\x12\x35\n\x08ShowInfo\x18\x01 \x01(\x0b\x32#.trpc.media.videostructure.ShowInfo\x12@\n\x0eSnippetInfoSet\x18\x02 \x03(\x0b\x32(.trpc.media.videostructure.AISnippetInfo\"Y\n\x1f\x43reateVideoStructureTaskRequest\x12\x0f\n\x07MediaId\x18\x01 \x01(\t\x12\x10\n\x08TaskName\x18\x04 \x01(\t\x12\x13\n\x0b\x43\x61llbackURL\x18\x05 \x01(\t\"2\n CreateVideoStructureTaskResponse\x12\x0e\n\x06TaskId\x18\x02 \x01(\t\".\n\x1c\x44\x65scribeAITagTaskDataRequest\x12\x0e\n\x06TaskId\x18\x01 \x01(\t\"^\n\x1d\x44\x65scribeVideoShotCoverRequest\x12\x0f\n\x07MediaId\x18\x01 \x01(\t\x12\x16\n\x0eStartTimeStamp\x18\x02 \x01(\x02\x12\x14\n\x0c\x45ndTimeStamp\x18\x03 \x01(\x02\"r\n\x1e\x44\x65scribeVideoShotCoverResponse\x12-\n\x08TaskInfo\x18\x01 \x01(\x0b\x32\x1b.trpc.media.common.TaskInfo\x12\x0f\n\x07\x43overId\x18\x02 \x01(\t\x12\x10\n\x08\x43overUrl\x18\x03 \x01(\t\"\x8a\x01\n\x1d\x44\x65scribeAITagTaskDataResponse\x12:\n\x08TaskData\x18\x01 \x01(\x0b\x32(.trpc.media.videostructure.AITagTaskData\x12-\n\x08TaskInfo\x18\x02 \x01(\x0b\x32\x1b.trpc.media.common.TaskInfo\"\x94\x01\n\"DescribeAITagImageTaskDataResponse\x12?\n\x08TaskData\x18\x01 \x01(\x0b\x32-.trpc.media.videostructure.AITagImageTaskData\x12-\n\x08TaskInfo\x18\x02 \x01(\x0b\x32\x1b.trpc.media.common.TaskInfo\"\x94\x01\n\"DescribeAITagAudioTaskDataResponse\x12?\n\x08TaskData\x18\x01 \x01(\x0b\x32-.trpc.media.videostructure.AITagAudioTaskData\x12-\n\x08TaskInfo\x18\x02 \x01(\x0b\x32\x1b.trpc.media.common.TaskInfo\"\x92\x01\n!DescribeAITagTextTaskDataResponse\x12>\n\x08TaskData\x18\x01 \x01(\x0b\x32,.trpc.media.videostructure.AITagTextTaskData\x12-\n\x08TaskInfo\x18\x02 \x01(\x0b\x32\x1b.trpc.media.common.TaskInfo\"F\n DescribeAICatalogTaskDataRequest\x12\x0e\n\x06TaskId\x18\x01 \x01(\t\x12\x12\n\nOutputMode\x18\x02 \x01(\r\"\x92\x01\n!DescribeAICatalogTaskDataResponse\x12>\n\x08TaskData\x18\x01 \x01(\x0b\x32,.trpc.media.videostructure.AICatalogTaskData\x12-\n\x08TaskInfo\x18\x02 \x01(\x0b\x32\x1b.trpc.media.common.TaskInfo\".\n\x1c\x44\x65scribeAICutTaskDataRequest\x12\x0e\n\x06TaskId\x18\x01 \x01(\t\"\x8a\x01\n\x1d\x44\x65scribeAICutTaskDataResponse\x12:\n\x08TaskData\x18\x01 \x01(\x0b\x32(.trpc.media.videostructure.AICutTaskData\x12-\n\x08TaskInfo\x18\x02 \x01(\x0b\x32\x1b.trpc.media.common.TaskInfo\"\xa2\x01\n\nSymbolInfo\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x0c\n\x04Type\x18\x02 \x01(\t\x12\x11\n\tStartTime\x18\x03 \x01(\x02\x12\x0f\n\x07\x45ndTime\x18\x04 \x01(\x02\x12<\n\tPositions\x18\x05 \x03(\x0b\x32).trpc.media.videostructure.SymbolPosition\x12\x16\n\x0e\x46irstAppearTab\x18\x06 \x01(\t\"w\n\x0eSymbolPosition\x12\x12\n\nConfidence\x18\x01 \x01(\x02\x12\x12\n\nFrameIndex\x18\x02 \x01(\x05\x12\x11\n\tTimeStamp\x18\x03 \x01(\x02\x12*\n\x08Position\x18\x04 \x01(\x0b\x32\x18.trpc.media.common.Rectf2\xf4\x06\n\x05\x41ITag\x12\x8a\x01\n\x0f\x43reateAITagTask\x12:.trpc.media.videostructure.CreateVideoStructureTaskRequest\x1a;.trpc.media.videostructure.CreateVideoStructureTaskResponse\x12\x8a\x01\n\x15\x44\x65scribeAITagTaskData\x12\x37.trpc.media.videostructure.DescribeAITagTaskDataRequest\x1a\x38.trpc.media.videostructure.DescribeAITagTaskDataResponse\x12\x94\x01\n\x1a\x44\x65scribeAITagAudioTaskData\x12\x37.trpc.media.videostructure.DescribeAITagTaskDataRequest\x1a=.trpc.media.videostructure.DescribeAITagAudioTaskDataResponse\x12\x94\x01\n\x1a\x44\x65scribeAITagImageTaskData\x12\x37.trpc.media.videostructure.DescribeAITagTaskDataRequest\x1a=.trpc.media.videostructure.DescribeAITagImageTaskDataResponse\x12\x92\x01\n\x19\x44\x65scribeAITagTextTaskData\x12\x37.trpc.media.videostructure.DescribeAITagTaskDataRequest\x1a<.trpc.media.videostructure.DescribeAITagTextTaskDataResponse\x12\x8d\x01\n\x16\x44\x65scribeVideoShotCover\x12\x38.trpc.media.videostructure.DescribeVideoShotCoverRequest\x1a\x39.trpc.media.videostructure.DescribeVideoShotCoverResponse2\xb5\x02\n\tAICatalog\x12\x8e\x01\n\x13\x43reateAICatalogTask\x12:.trpc.media.videostructure.CreateVideoStructureTaskRequest\x1a;.trpc.media.videostructure.CreateVideoStructureTaskResponse\x12\x96\x01\n\x19\x44\x65scribeAICatalogTaskData\x12;.trpc.media.videostructure.DescribeAICatalogTaskDataRequest\x1a<.trpc.media.videostructure.DescribeAICatalogTaskDataResponse2\xa1\x02\n\x05\x41ICut\x12\x8a\x01\n\x0f\x43reateAICutTask\x12:.trpc.media.videostructure.CreateVideoStructureTaskRequest\x1a;.trpc.media.videostructure.CreateVideoStructureTaskResponse\x12\x8a\x01\n\x15\x44\x65scribeAICutTaskData\x12\x37.trpc.media.videostructure.DescribeAICutTaskDataRequest\x1a\x38.trpc.media.videostructure.DescribeAICutTaskDataResponseB^Z\\github.com/Tencent-media-asset-system-sdk/media-platform-sdk-go/protobuf-spec/videostructureb\x06proto3')



_AUDIOINFO = DESCRIPTOR.message_types_by_name['AudioInfo']
_TEXTINFO = DESCRIPTOR.message_types_by_name['TextInfo']
_APPEARFRAMEINFO = DESCRIPTOR.message_types_by_name['AppearFrameInfo']
_APPEARTIMEINFO = DESCRIPTOR.message_types_by_name['AppearTimeInfo']
_APPEARPOSTIONINFO = DESCRIPTOR.message_types_by_name['AppearPostionInfo']
_PERSONTAGINFO = DESCRIPTOR.message_types_by_name['PersonTagInfo']
_L1CLASSIFIEDPERSONINFO = DESCRIPTOR.message_types_by_name['L1ClassifiedPersonInfo']
_L2CLASSIFIEDPERSONINFO = DESCRIPTOR.message_types_by_name['L2ClassifiedPersonInfo']
_UNKNOWNPERSON = DESCRIPTOR.message_types_by_name['UnknownPerson']
_MULTILEVELTAG = DESCRIPTOR.message_types_by_name['MultiLevelTag']
_MAJOREVENT = DESCRIPTOR.message_types_by_name['MajorEvent']
_AILENSINFO = DESCRIPTOR.message_types_by_name['AILensInfo']
_AISCENEINFO = DESCRIPTOR.message_types_by_name['AISceneInfo']
_AISNIPPETINFO = DESCRIPTOR.message_types_by_name['AISnippetInfo']
_AUDIOCAPTIONINFO = DESCRIPTOR.message_types_by_name['AudioCaptionInfo']
_SHOWINFO = DESCRIPTOR.message_types_by_name['ShowInfo']
_IMAGEOCR = DESCRIPTOR.message_types_by_name['ImageOcr']
_IMAGELOGO = DESCRIPTOR.message_types_by_name['ImageLogo']
_AITAGTASKDATA = DESCRIPTOR.message_types_by_name['AITagTaskData']
_AITAGAUDIOTASKDATA = DESCRIPTOR.message_types_by_name['AITagAudioTaskData']
_AITAGTEXTTASKDATA = DESCRIPTOR.message_types_by_name['AITagTextTaskData']
_AITAGIMAGETASKDATA = DESCRIPTOR.message_types_by_name['AITagImageTaskData']
_AICATALOGTASKDATA = DESCRIPTOR.message_types_by_name['AICatalogTaskData']
_AICUTTASKDATA = DESCRIPTOR.message_types_by_name['AICutTaskData']
_CREATEVIDEOSTRUCTURETASKREQUEST = DESCRIPTOR.message_types_by_name['CreateVideoStructureTaskRequest']
_CREATEVIDEOSTRUCTURETASKRESPONSE = DESCRIPTOR.message_types_by_name['CreateVideoStructureTaskResponse']
_DESCRIBEAITAGTASKDATAREQUEST = DESCRIPTOR.message_types_by_name['DescribeAITagTaskDataRequest']
_DESCRIBEVIDEOSHOTCOVERREQUEST = DESCRIPTOR.message_types_by_name['DescribeVideoShotCoverRequest']
_DESCRIBEVIDEOSHOTCOVERRESPONSE = DESCRIPTOR.message_types_by_name['DescribeVideoShotCoverResponse']
_DESCRIBEAITAGTASKDATARESPONSE = DESCRIPTOR.message_types_by_name['DescribeAITagTaskDataResponse']
_DESCRIBEAITAGIMAGETASKDATARESPONSE = DESCRIPTOR.message_types_by_name['DescribeAITagImageTaskDataResponse']
_DESCRIBEAITAGAUDIOTASKDATARESPONSE = DESCRIPTOR.message_types_by_name['DescribeAITagAudioTaskDataResponse']
_DESCRIBEAITAGTEXTTASKDATARESPONSE = DESCRIPTOR.message_types_by_name['DescribeAITagTextTaskDataResponse']
_DESCRIBEAICATALOGTASKDATAREQUEST = DESCRIPTOR.message_types_by_name['DescribeAICatalogTaskDataRequest']
_DESCRIBEAICATALOGTASKDATARESPONSE = DESCRIPTOR.message_types_by_name['DescribeAICatalogTaskDataResponse']
_DESCRIBEAICUTTASKDATAREQUEST = DESCRIPTOR.message_types_by_name['DescribeAICutTaskDataRequest']
_DESCRIBEAICUTTASKDATARESPONSE = DESCRIPTOR.message_types_by_name['DescribeAICutTaskDataResponse']
_SYMBOLINFO = DESCRIPTOR.message_types_by_name['SymbolInfo']
_SYMBOLPOSITION = DESCRIPTOR.message_types_by_name['SymbolPosition']
AudioInfo = _reflection.GeneratedProtocolMessageType('AudioInfo', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOINFO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.AudioInfo)
  })
_sym_db.RegisterMessage(AudioInfo)

TextInfo = _reflection.GeneratedProtocolMessageType('TextInfo', (_message.Message,), {
  'DESCRIPTOR' : _TEXTINFO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.TextInfo)
  })
_sym_db.RegisterMessage(TextInfo)

AppearFrameInfo = _reflection.GeneratedProtocolMessageType('AppearFrameInfo', (_message.Message,), {
  'DESCRIPTOR' : _APPEARFRAMEINFO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.AppearFrameInfo)
  })
_sym_db.RegisterMessage(AppearFrameInfo)

AppearTimeInfo = _reflection.GeneratedProtocolMessageType('AppearTimeInfo', (_message.Message,), {
  'DESCRIPTOR' : _APPEARTIMEINFO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.AppearTimeInfo)
  })
_sym_db.RegisterMessage(AppearTimeInfo)

AppearPostionInfo = _reflection.GeneratedProtocolMessageType('AppearPostionInfo', (_message.Message,), {
  'DESCRIPTOR' : _APPEARPOSTIONINFO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.AppearPostionInfo)
  })
_sym_db.RegisterMessage(AppearPostionInfo)

PersonTagInfo = _reflection.GeneratedProtocolMessageType('PersonTagInfo', (_message.Message,), {
  'DESCRIPTOR' : _PERSONTAGINFO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.PersonTagInfo)
  })
_sym_db.RegisterMessage(PersonTagInfo)

L1ClassifiedPersonInfo = _reflection.GeneratedProtocolMessageType('L1ClassifiedPersonInfo', (_message.Message,), {
  'DESCRIPTOR' : _L1CLASSIFIEDPERSONINFO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.L1ClassifiedPersonInfo)
  })
_sym_db.RegisterMessage(L1ClassifiedPersonInfo)

L2ClassifiedPersonInfo = _reflection.GeneratedProtocolMessageType('L2ClassifiedPersonInfo', (_message.Message,), {
  'DESCRIPTOR' : _L2CLASSIFIEDPERSONINFO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.L2ClassifiedPersonInfo)
  })
_sym_db.RegisterMessage(L2ClassifiedPersonInfo)

UnknownPerson = _reflection.GeneratedProtocolMessageType('UnknownPerson', (_message.Message,), {
  'DESCRIPTOR' : _UNKNOWNPERSON,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.UnknownPerson)
  })
_sym_db.RegisterMessage(UnknownPerson)

MultiLevelTag = _reflection.GeneratedProtocolMessageType('MultiLevelTag', (_message.Message,), {
  'DESCRIPTOR' : _MULTILEVELTAG,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.MultiLevelTag)
  })
_sym_db.RegisterMessage(MultiLevelTag)

MajorEvent = _reflection.GeneratedProtocolMessageType('MajorEvent', (_message.Message,), {
  'DESCRIPTOR' : _MAJOREVENT,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.MajorEvent)
  })
_sym_db.RegisterMessage(MajorEvent)

AILensInfo = _reflection.GeneratedProtocolMessageType('AILensInfo', (_message.Message,), {
  'DESCRIPTOR' : _AILENSINFO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.AILensInfo)
  })
_sym_db.RegisterMessage(AILensInfo)

AISceneInfo = _reflection.GeneratedProtocolMessageType('AISceneInfo', (_message.Message,), {
  'DESCRIPTOR' : _AISCENEINFO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.AISceneInfo)
  })
_sym_db.RegisterMessage(AISceneInfo)

AISnippetInfo = _reflection.GeneratedProtocolMessageType('AISnippetInfo', (_message.Message,), {
  'DESCRIPTOR' : _AISNIPPETINFO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.AISnippetInfo)
  })
_sym_db.RegisterMessage(AISnippetInfo)

AudioCaptionInfo = _reflection.GeneratedProtocolMessageType('AudioCaptionInfo', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOCAPTIONINFO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.AudioCaptionInfo)
  })
_sym_db.RegisterMessage(AudioCaptionInfo)

ShowInfo = _reflection.GeneratedProtocolMessageType('ShowInfo', (_message.Message,), {
  'DESCRIPTOR' : _SHOWINFO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.ShowInfo)
  })
_sym_db.RegisterMessage(ShowInfo)

ImageOcr = _reflection.GeneratedProtocolMessageType('ImageOcr', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEOCR,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.ImageOcr)
  })
_sym_db.RegisterMessage(ImageOcr)

ImageLogo = _reflection.GeneratedProtocolMessageType('ImageLogo', (_message.Message,), {
  'DESCRIPTOR' : _IMAGELOGO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.ImageLogo)
  })
_sym_db.RegisterMessage(ImageLogo)

AITagTaskData = _reflection.GeneratedProtocolMessageType('AITagTaskData', (_message.Message,), {
  'DESCRIPTOR' : _AITAGTASKDATA,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.AITagTaskData)
  })
_sym_db.RegisterMessage(AITagTaskData)

AITagAudioTaskData = _reflection.GeneratedProtocolMessageType('AITagAudioTaskData', (_message.Message,), {
  'DESCRIPTOR' : _AITAGAUDIOTASKDATA,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.AITagAudioTaskData)
  })
_sym_db.RegisterMessage(AITagAudioTaskData)

AITagTextTaskData = _reflection.GeneratedProtocolMessageType('AITagTextTaskData', (_message.Message,), {
  'DESCRIPTOR' : _AITAGTEXTTASKDATA,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.AITagTextTaskData)
  })
_sym_db.RegisterMessage(AITagTextTaskData)

AITagImageTaskData = _reflection.GeneratedProtocolMessageType('AITagImageTaskData', (_message.Message,), {
  'DESCRIPTOR' : _AITAGIMAGETASKDATA,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.AITagImageTaskData)
  })
_sym_db.RegisterMessage(AITagImageTaskData)

AICatalogTaskData = _reflection.GeneratedProtocolMessageType('AICatalogTaskData', (_message.Message,), {
  'DESCRIPTOR' : _AICATALOGTASKDATA,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.AICatalogTaskData)
  })
_sym_db.RegisterMessage(AICatalogTaskData)

AICutTaskData = _reflection.GeneratedProtocolMessageType('AICutTaskData', (_message.Message,), {
  'DESCRIPTOR' : _AICUTTASKDATA,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.AICutTaskData)
  })
_sym_db.RegisterMessage(AICutTaskData)

CreateVideoStructureTaskRequest = _reflection.GeneratedProtocolMessageType('CreateVideoStructureTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVIDEOSTRUCTURETASKREQUEST,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.CreateVideoStructureTaskRequest)
  })
_sym_db.RegisterMessage(CreateVideoStructureTaskRequest)

CreateVideoStructureTaskResponse = _reflection.GeneratedProtocolMessageType('CreateVideoStructureTaskResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVIDEOSTRUCTURETASKRESPONSE,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.CreateVideoStructureTaskResponse)
  })
_sym_db.RegisterMessage(CreateVideoStructureTaskResponse)

DescribeAITagTaskDataRequest = _reflection.GeneratedProtocolMessageType('DescribeAITagTaskDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEAITAGTASKDATAREQUEST,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.DescribeAITagTaskDataRequest)
  })
_sym_db.RegisterMessage(DescribeAITagTaskDataRequest)

DescribeVideoShotCoverRequest = _reflection.GeneratedProtocolMessageType('DescribeVideoShotCoverRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVIDEOSHOTCOVERREQUEST,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.DescribeVideoShotCoverRequest)
  })
_sym_db.RegisterMessage(DescribeVideoShotCoverRequest)

DescribeVideoShotCoverResponse = _reflection.GeneratedProtocolMessageType('DescribeVideoShotCoverResponse', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVIDEOSHOTCOVERRESPONSE,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.DescribeVideoShotCoverResponse)
  })
_sym_db.RegisterMessage(DescribeVideoShotCoverResponse)

DescribeAITagTaskDataResponse = _reflection.GeneratedProtocolMessageType('DescribeAITagTaskDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEAITAGTASKDATARESPONSE,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.DescribeAITagTaskDataResponse)
  })
_sym_db.RegisterMessage(DescribeAITagTaskDataResponse)

DescribeAITagImageTaskDataResponse = _reflection.GeneratedProtocolMessageType('DescribeAITagImageTaskDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEAITAGIMAGETASKDATARESPONSE,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.DescribeAITagImageTaskDataResponse)
  })
_sym_db.RegisterMessage(DescribeAITagImageTaskDataResponse)

DescribeAITagAudioTaskDataResponse = _reflection.GeneratedProtocolMessageType('DescribeAITagAudioTaskDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEAITAGAUDIOTASKDATARESPONSE,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.DescribeAITagAudioTaskDataResponse)
  })
_sym_db.RegisterMessage(DescribeAITagAudioTaskDataResponse)

DescribeAITagTextTaskDataResponse = _reflection.GeneratedProtocolMessageType('DescribeAITagTextTaskDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEAITAGTEXTTASKDATARESPONSE,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.DescribeAITagTextTaskDataResponse)
  })
_sym_db.RegisterMessage(DescribeAITagTextTaskDataResponse)

DescribeAICatalogTaskDataRequest = _reflection.GeneratedProtocolMessageType('DescribeAICatalogTaskDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEAICATALOGTASKDATAREQUEST,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.DescribeAICatalogTaskDataRequest)
  })
_sym_db.RegisterMessage(DescribeAICatalogTaskDataRequest)

DescribeAICatalogTaskDataResponse = _reflection.GeneratedProtocolMessageType('DescribeAICatalogTaskDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEAICATALOGTASKDATARESPONSE,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.DescribeAICatalogTaskDataResponse)
  })
_sym_db.RegisterMessage(DescribeAICatalogTaskDataResponse)

DescribeAICutTaskDataRequest = _reflection.GeneratedProtocolMessageType('DescribeAICutTaskDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEAICUTTASKDATAREQUEST,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.DescribeAICutTaskDataRequest)
  })
_sym_db.RegisterMessage(DescribeAICutTaskDataRequest)

DescribeAICutTaskDataResponse = _reflection.GeneratedProtocolMessageType('DescribeAICutTaskDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEAICUTTASKDATARESPONSE,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.DescribeAICutTaskDataResponse)
  })
_sym_db.RegisterMessage(DescribeAICutTaskDataResponse)

SymbolInfo = _reflection.GeneratedProtocolMessageType('SymbolInfo', (_message.Message,), {
  'DESCRIPTOR' : _SYMBOLINFO,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.SymbolInfo)
  })
_sym_db.RegisterMessage(SymbolInfo)

SymbolPosition = _reflection.GeneratedProtocolMessageType('SymbolPosition', (_message.Message,), {
  'DESCRIPTOR' : _SYMBOLPOSITION,
  '__module__' : 'video_structure_pb2'
  # @@protoc_insertion_point(class_scope:trpc.media.videostructure.SymbolPosition)
  })
_sym_db.RegisterMessage(SymbolPosition)

_AITAG = DESCRIPTOR.services_by_name['AITag']
_AICATALOG = DESCRIPTOR.services_by_name['AICatalog']
_AICUT = DESCRIPTOR.services_by_name['AICut']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\\github.com/Tencent-media-asset-system-sdk/media-platform-sdk-go/protobuf-spec/videostructure'
  _AUDIOINFO._serialized_start=66
  _AUDIOINFO._serialized_end=153
  _TEXTINFO._serialized_start=155
  _TEXTINFO._serialized_end=241
  _APPEARFRAMEINFO._serialized_start=243
  _APPEARFRAMEINFO._serialized_end=336
  _APPEARTIMEINFO._serialized_start=339
  _APPEARTIMEINFO._serialized_end=557
  _APPEARPOSTIONINFO._serialized_start=559
  _APPEARPOSTIONINFO._serialized_end=637
  _PERSONTAGINFO._serialized_start=640
  _PERSONTAGINFO._serialized_end=995
  _L1CLASSIFIEDPERSONINFO._serialized_start=998
  _L1CLASSIFIEDPERSONINFO._serialized_end=1130
  _L2CLASSIFIEDPERSONINFO._serialized_start=1132
  _L2CLASSIFIEDPERSONINFO._serialized_end=1239
  _UNKNOWNPERSON._serialized_start=1242
  _UNKNOWNPERSON._serialized_end=1441
  _MULTILEVELTAG._serialized_start=1444
  _MULTILEVELTAG._serialized_end=1833
  _MAJOREVENT._serialized_start=1836
  _MAJOREVENT._serialized_end=2341
  _AILENSINFO._serialized_start=2344
  _AILENSINFO._serialized_end=2870
  _AISCENEINFO._serialized_start=2873
  _AISCENEINFO._serialized_end=3380
  _AISNIPPETINFO._serialized_start=3383
  _AISNIPPETINFO._serialized_end=4172
  _AUDIOCAPTIONINFO._serialized_start=4174
  _AUDIOCAPTIONINFO._serialized_end=4255
  _SHOWINFO._serialized_start=4258
  _SHOWINFO._serialized_end=5226
  _IMAGEOCR._serialized_start=5228
  _IMAGEOCR._serialized_end=5300
  _IMAGELOGO._serialized_start=5302
  _IMAGELOGO._serialized_end=5372
  _AITAGTASKDATA._serialized_start=5374
  _AITAGTASKDATA._serialized_end=5444
  _AITAGAUDIOTASKDATA._serialized_start=5447
  _AITAGAUDIOTASKDATA._serialized_end=5659
  _AITAGTEXTTASKDATA._serialized_start=5661
  _AITAGTEXTTASKDATA._serialized_end=5776
  _AITAGIMAGETASKDATA._serialized_start=5779
  _AITAGIMAGETASKDATA._serialized_end=6321
  _AICATALOGTASKDATA._serialized_start=6324
  _AICATALOGTASKDATA._serialized_end=6586
  _AICUTTASKDATA._serialized_start=6589
  _AICUTTASKDATA._serialized_end=6725
  _CREATEVIDEOSTRUCTURETASKREQUEST._serialized_start=6727
  _CREATEVIDEOSTRUCTURETASKREQUEST._serialized_end=6816
  _CREATEVIDEOSTRUCTURETASKRESPONSE._serialized_start=6818
  _CREATEVIDEOSTRUCTURETASKRESPONSE._serialized_end=6868
  _DESCRIBEAITAGTASKDATAREQUEST._serialized_start=6870
  _DESCRIBEAITAGTASKDATAREQUEST._serialized_end=6916
  _DESCRIBEVIDEOSHOTCOVERREQUEST._serialized_start=6918
  _DESCRIBEVIDEOSHOTCOVERREQUEST._serialized_end=7012
  _DESCRIBEVIDEOSHOTCOVERRESPONSE._serialized_start=7014
  _DESCRIBEVIDEOSHOTCOVERRESPONSE._serialized_end=7128
  _DESCRIBEAITAGTASKDATARESPONSE._serialized_start=7131
  _DESCRIBEAITAGTASKDATARESPONSE._serialized_end=7269
  _DESCRIBEAITAGIMAGETASKDATARESPONSE._serialized_start=7272
  _DESCRIBEAITAGIMAGETASKDATARESPONSE._serialized_end=7420
  _DESCRIBEAITAGAUDIOTASKDATARESPONSE._serialized_start=7423
  _DESCRIBEAITAGAUDIOTASKDATARESPONSE._serialized_end=7571
  _DESCRIBEAITAGTEXTTASKDATARESPONSE._serialized_start=7574
  _DESCRIBEAITAGTEXTTASKDATARESPONSE._serialized_end=7720
  _DESCRIBEAICATALOGTASKDATAREQUEST._serialized_start=7722
  _DESCRIBEAICATALOGTASKDATAREQUEST._serialized_end=7792
  _DESCRIBEAICATALOGTASKDATARESPONSE._serialized_start=7795
  _DESCRIBEAICATALOGTASKDATARESPONSE._serialized_end=7941
  _DESCRIBEAICUTTASKDATAREQUEST._serialized_start=7943
  _DESCRIBEAICUTTASKDATAREQUEST._serialized_end=7989
  _DESCRIBEAICUTTASKDATARESPONSE._serialized_start=7992
  _DESCRIBEAICUTTASKDATARESPONSE._serialized_end=8130
  _SYMBOLINFO._serialized_start=8133
  _SYMBOLINFO._serialized_end=8295
  _SYMBOLPOSITION._serialized_start=8297
  _SYMBOLPOSITION._serialized_end=8416
  _AITAG._serialized_start=8419
  _AITAG._serialized_end=9303
  _AICATALOG._serialized_start=9306
  _AICATALOG._serialized_end=9615
  _AICUT._serialized_start=9618
  _AICUT._serialized_end=9907
# @@protoc_insertion_point(module_scope)