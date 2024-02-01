#!/bin/bash

set -e

# module=`cat go.mod | grep module | awk {'print $2'}`

# find ./proto/media -type f -name "*.proto" -exec sed -i "s#git.code.oa.com/yt-media-ai-videounderstanding/yt-ai-media-middle-platform-api#${module}#g" {} \;


function gen() {
  dir=$1
  proto=$2
  mkdir -p ${dir}
  python3 -m grpc_tools.protoc --python_out=${dir} --grpc_python_out=${dir} -I ./proto/media ${proto}.proto
}

gen "mediasdk/protobufspec/" "common"

gen "mediasdk/protobufspec/" "media"

gen "mediasdk/protobufspec/" "video_structure"

gen "mediasdk/protobufspec/" "ai_tag_analyse"

gen "mediasdk/protobufspec/" "person_retrieval"

gen "mediasdk/protobufspec/" "task"

gen "mediasdk/protobufspec/" "video_cut"

gen "mediasdk/protobufspec/" "task_data"

gen "mediasdk/protobufspec/" "video_quality_evaluation"

gen "mediasdk/protobufspec/" "snapshot"

gen "mediasdk/protobufspec/" "person_user_define"

gen "mediasdk/protobufspec/" "video_erase"

gen "mediasdk/protobufspec/" "custom_feature"

gen "mediasdk/protobufspec/" "toolkit"

gen "mediasdk/protobufspec/" "media_crop"

gen "mediasdk/protobufspec/" "domain_group"

gen "mediasdk/protobufspec/" "workflow_template"

gen "mediasdk/protobufspec/" "yt_video_process"

gen "mediasdk/protobufspec/" "ai_video_process"

gen "mediasdk/protobufspec/" "text_summarization"

gen "mediasdk/protobufspec/" "shot_match"

find ./mediasdk/protobufspec -type f -name "*.py" -exec sed -i "s#import grpc#import grpc_mock as grpc#g" {} \;

sed -i -E 's/^(import.*_pb2)/from . \1/' ./mediasdk/protobufspec/*.py