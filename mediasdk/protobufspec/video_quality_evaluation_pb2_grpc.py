# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import mediasdk.grpc_mock as grpc

from . import video_quality_evaluation_pb2 as video__quality__evaluation__pb2


class VideoQualityEvaluationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateVideoQualityEvaluationTask = channel.unary_unary(
                '/trpc.media.videoquality.VideoQualityEvaluation/CreateVideoQualityEvaluationTask',
                request_serializer=video__quality__evaluation__pb2.CreateVideoQualityEvaluationTaskRequest.SerializeToString,
                response_deserializer=video__quality__evaluation__pb2.CreateVideoQualityEvaluationTaskResponse.FromString,
                )
        self.DescribeVideoQualityEvaluationTaskData = channel.unary_unary(
                '/trpc.media.videoquality.VideoQualityEvaluation/DescribeVideoQualityEvaluationTaskData',
                request_serializer=video__quality__evaluation__pb2.DescribeVideoQualityEvaluationTaskDataRequest.SerializeToString,
                response_deserializer=video__quality__evaluation__pb2.DescribeVideoQualityEvaluationTaskDataResponse.FromString,
                )
        self.DescribeLiveVideoQualityEvaluationTaskData = channel.unary_unary(
                '/trpc.media.videoquality.VideoQualityEvaluation/DescribeLiveVideoQualityEvaluationTaskData',
                request_serializer=video__quality__evaluation__pb2.DescribeVideoQualityEvaluationTaskDataRequest.SerializeToString,
                response_deserializer=video__quality__evaluation__pb2.DescribeLiveVideoQualityEvaluationTaskDataResponse.FromString,
                )
        self.DescribeVideoQualityLimitList = channel.unary_unary(
                '/trpc.media.videoquality.VideoQualityEvaluation/DescribeVideoQualityLimitList',
                request_serializer=video__quality__evaluation__pb2.DescribeVideoQualityLimitListRequest.SerializeToString,
                response_deserializer=video__quality__evaluation__pb2.DescribeVideoQualityLimitListResponse.FromString,
                )


class VideoQualityEvaluationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateVideoQualityEvaluationTask(self, request, context):
        """@alias=/CreateVideoQualityEvaluationTask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeVideoQualityEvaluationTaskData(self, request, context):
        """@alias=/DescribeVideoQualityEvaluationTaskData
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeLiveVideoQualityEvaluationTaskData(self, request, context):
        """@alias=/DescribeLiveVideoQualityEvaluationTaskData
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeVideoQualityLimitList(self, request, context):
        """@alias=/DescribeVideoQualityLimitList
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VideoQualityEvaluationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateVideoQualityEvaluationTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateVideoQualityEvaluationTask,
                    request_deserializer=video__quality__evaluation__pb2.CreateVideoQualityEvaluationTaskRequest.FromString,
                    response_serializer=video__quality__evaluation__pb2.CreateVideoQualityEvaluationTaskResponse.SerializeToString,
            ),
            'DescribeVideoQualityEvaluationTaskData': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeVideoQualityEvaluationTaskData,
                    request_deserializer=video__quality__evaluation__pb2.DescribeVideoQualityEvaluationTaskDataRequest.FromString,
                    response_serializer=video__quality__evaluation__pb2.DescribeVideoQualityEvaluationTaskDataResponse.SerializeToString,
            ),
            'DescribeLiveVideoQualityEvaluationTaskData': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeLiveVideoQualityEvaluationTaskData,
                    request_deserializer=video__quality__evaluation__pb2.DescribeVideoQualityEvaluationTaskDataRequest.FromString,
                    response_serializer=video__quality__evaluation__pb2.DescribeLiveVideoQualityEvaluationTaskDataResponse.SerializeToString,
            ),
            'DescribeVideoQualityLimitList': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeVideoQualityLimitList,
                    request_deserializer=video__quality__evaluation__pb2.DescribeVideoQualityLimitListRequest.FromString,
                    response_serializer=video__quality__evaluation__pb2.DescribeVideoQualityLimitListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trpc.media.videoquality.VideoQualityEvaluation', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VideoQualityEvaluation(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateVideoQualityEvaluationTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.videoquality.VideoQualityEvaluation/CreateVideoQualityEvaluationTask',
            video__quality__evaluation__pb2.CreateVideoQualityEvaluationTaskRequest.SerializeToString,
            video__quality__evaluation__pb2.CreateVideoQualityEvaluationTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeVideoQualityEvaluationTaskData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.videoquality.VideoQualityEvaluation/DescribeVideoQualityEvaluationTaskData',
            video__quality__evaluation__pb2.DescribeVideoQualityEvaluationTaskDataRequest.SerializeToString,
            video__quality__evaluation__pb2.DescribeVideoQualityEvaluationTaskDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeLiveVideoQualityEvaluationTaskData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.videoquality.VideoQualityEvaluation/DescribeLiveVideoQualityEvaluationTaskData',
            video__quality__evaluation__pb2.DescribeVideoQualityEvaluationTaskDataRequest.SerializeToString,
            video__quality__evaluation__pb2.DescribeLiveVideoQualityEvaluationTaskDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeVideoQualityLimitList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.videoquality.VideoQualityEvaluation/DescribeVideoQualityLimitList',
            video__quality__evaluation__pb2.DescribeVideoQualityLimitListRequest.SerializeToString,
            video__quality__evaluation__pb2.DescribeVideoQualityLimitListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
