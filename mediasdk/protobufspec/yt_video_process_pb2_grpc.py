# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import mediasdk.grpc_mock as grpc

from . import yt_video_process_pb2 as yt__video__process__pb2


class YTVideoProcessStub(object):
    """interface defines
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateVideoProcessTask = channel.unary_unary(
                '/trpc.media.ytvideoprocess.YTVideoProcess/CreateVideoProcessTask',
                request_serializer=yt__video__process__pb2.CreateVideoProcessTaskRequest.SerializeToString,
                response_deserializer=yt__video__process__pb2.CreateVideoProcessResponse.FromString,
                )
        self.DescribeVideoProcessDetail = channel.unary_unary(
                '/trpc.media.ytvideoprocess.YTVideoProcess/DescribeVideoProcessDetail',
                request_serializer=yt__video__process__pb2.DescribeVideoProcessDetailRequest.SerializeToString,
                response_deserializer=yt__video__process__pb2.DescribeVideoProcessDetailResponse.FromString,
                )
        self.UpdateVideoProcessTask = channel.unary_unary(
                '/trpc.media.ytvideoprocess.YTVideoProcess/UpdateVideoProcessTask',
                request_serializer=yt__video__process__pb2.UpdateVideoProcessTaskRequest.SerializeToString,
                response_deserializer=yt__video__process__pb2.UpdateVideoProcessResponse.FromString,
                )
        self.StopVideoProcessTask = channel.unary_unary(
                '/trpc.media.ytvideoprocess.YTVideoProcess/StopVideoProcessTask',
                request_serializer=yt__video__process__pb2.StopVideoProcessTaskRequest.SerializeToString,
                response_deserializer=yt__video__process__pb2.StopVideoProcessTaskResponse.FromString,
                )


class YTVideoProcessServicer(object):
    """interface defines
    """

    def CreateVideoProcessTask(self, request, context):
        """创建视频处理任务
        @alias=/CreateVideoProcessTask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeVideoProcessDetail(self, request, context):
        """获取视频处理详情
        @alias=/DescribeVideoProcessDetail
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateVideoProcessTask(self, request, context):
        """更新视频处理任务
        @alias=/UpdateVideoProcessTask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopVideoProcessTask(self, request, context):
        """停止任务，内部使用对外不暴露
        @alias=/StopVideoProcessTask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_YTVideoProcessServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateVideoProcessTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateVideoProcessTask,
                    request_deserializer=yt__video__process__pb2.CreateVideoProcessTaskRequest.FromString,
                    response_serializer=yt__video__process__pb2.CreateVideoProcessResponse.SerializeToString,
            ),
            'DescribeVideoProcessDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeVideoProcessDetail,
                    request_deserializer=yt__video__process__pb2.DescribeVideoProcessDetailRequest.FromString,
                    response_serializer=yt__video__process__pb2.DescribeVideoProcessDetailResponse.SerializeToString,
            ),
            'UpdateVideoProcessTask': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateVideoProcessTask,
                    request_deserializer=yt__video__process__pb2.UpdateVideoProcessTaskRequest.FromString,
                    response_serializer=yt__video__process__pb2.UpdateVideoProcessResponse.SerializeToString,
            ),
            'StopVideoProcessTask': grpc.unary_unary_rpc_method_handler(
                    servicer.StopVideoProcessTask,
                    request_deserializer=yt__video__process__pb2.StopVideoProcessTaskRequest.FromString,
                    response_serializer=yt__video__process__pb2.StopVideoProcessTaskResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trpc.media.ytvideoprocess.YTVideoProcess', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class YTVideoProcess(object):
    """interface defines
    """

    @staticmethod
    def CreateVideoProcessTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.ytvideoprocess.YTVideoProcess/CreateVideoProcessTask',
            yt__video__process__pb2.CreateVideoProcessTaskRequest.SerializeToString,
            yt__video__process__pb2.CreateVideoProcessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeVideoProcessDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.ytvideoprocess.YTVideoProcess/DescribeVideoProcessDetail',
            yt__video__process__pb2.DescribeVideoProcessDetailRequest.SerializeToString,
            yt__video__process__pb2.DescribeVideoProcessDetailResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateVideoProcessTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.ytvideoprocess.YTVideoProcess/UpdateVideoProcessTask',
            yt__video__process__pb2.UpdateVideoProcessTaskRequest.SerializeToString,
            yt__video__process__pb2.UpdateVideoProcessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopVideoProcessTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.ytvideoprocess.YTVideoProcess/StopVideoProcessTask',
            yt__video__process__pb2.StopVideoProcessTaskRequest.SerializeToString,
            yt__video__process__pb2.StopVideoProcessTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)