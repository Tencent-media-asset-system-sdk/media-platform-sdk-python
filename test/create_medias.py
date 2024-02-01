from mediasdk.protobufspec import media_pb2_grpc
from mediasdk.grpc_mock.cert import Cert

proxy = media_pb2_grpc.Media()
cert = Cert("114.132.239.24", 0, "16111e9bb6ca4708abb0b4db2f", "fd46f3cb84c141ffa52dd9c8d6", 1, 1)


req = {
    "MediaUnionInfoSet": [
        {
            "MediaInfo": {
                "MediaName": "test-beijingninzao-6mins.mp4",
                "MediaType":1,
                "MediaTag":1,
                "MediaSource":1,
            },
            "DomainGroupInfo": {
                "DomainGroupType":1
            },
            "FileInfo": {
                "FileName": "test-beijingninzao-6mins.mp4",
                "FileURL": "https://ai-media-1256936300.cos.ap-guangzhou.myqcloud.com/test_data/test-beijingninzao-6mins.mp4"
            },
            "MediaWorkflowTemplateInfo": {
                "WorkflowMode":1,
                "AutoMatchTemplate": True,
            }
        }
    ]
}

rsp = proxy.CreateMedias(request=req, target=cert)

print(rsp)

