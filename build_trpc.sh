#!/bin/bash

set -e

# module=`cat go.mod | grep module | awk {'print $2'}`

# find ./proto/media -type f -name "*.proto" -exec sed -i "s#git.code.oa.com/yt-media-ai-videounderstanding/yt-ai-media-middle-platform-api#${module}#g" {} \;

# 兼容 sdk-prometheus-trpc-go
trpc create --api-version=1 --protofile=proto/media/common.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/video_structure.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/ai_tag_analyse.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python

trpc create --api-version=1 --protofile=proto/media/person_retrieval.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/media.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/task.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/video_cut.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/task_data.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/video_quality_evaluation.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/snapshot.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=2 --protofile=proto/media/person_user_define.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/video_erase.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/custom_feature.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python

trpc create --api-version=1 --protofile=proto/media/toolkit.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/media_crop.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/domain_group.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/workflow_template.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python

trpc create --api-version=1 --protofile=proto/media/yt_video_process.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/ai_video_process.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python

trpc create --api-version=1 --protofile=proto/media/text_summarization.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python
trpc create --api-version=1 --protofile=proto/media/shot_match.proto --rpconly -o protobufspec/ --mock=false --alias --nogomod --lang=python

# find ./protobufspec -type f -name "*.trpc.go" -exec sed -i "s#git.code.oa.com/trpc-go/trpc-go#${module}/trpc_mock#g" {} \;