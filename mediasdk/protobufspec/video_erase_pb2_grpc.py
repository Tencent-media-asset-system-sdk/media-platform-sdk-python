# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import mediasdk.grpc_mock as grpc

from . import video_erase_pb2 as video__erase__pb2


class RemoveLogoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateRemoveLogoTask = channel.unary_unary(
                '/trpc.media.videoerase.RemoveLogo/CreateRemoveLogoTask',
                request_serializer=video__erase__pb2.CreateRemoveLogoTaskRequest.SerializeToString,
                response_deserializer=video__erase__pb2.CreateRemoveLogoTaskResponse.FromString,
                )
        self.DescribeRemoveLogoTaskData = channel.unary_unary(
                '/trpc.media.videoerase.RemoveLogo/DescribeRemoveLogoTaskData',
                request_serializer=video__erase__pb2.DescribeRemoveLogoTaskDataRequest.SerializeToString,
                response_deserializer=video__erase__pb2.DescribeRemoveLogoTaskDataResponse.FromString,
                )


class RemoveLogoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateRemoveLogoTask(self, request, context):
        """@alias=/CreateRemoveLogoTask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeRemoveLogoTaskData(self, request, context):
        """@alias=/DescribeRemoveLogoTaskData
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RemoveLogoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateRemoveLogoTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRemoveLogoTask,
                    request_deserializer=video__erase__pb2.CreateRemoveLogoTaskRequest.FromString,
                    response_serializer=video__erase__pb2.CreateRemoveLogoTaskResponse.SerializeToString,
            ),
            'DescribeRemoveLogoTaskData': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeRemoveLogoTaskData,
                    request_deserializer=video__erase__pb2.DescribeRemoveLogoTaskDataRequest.FromString,
                    response_serializer=video__erase__pb2.DescribeRemoveLogoTaskDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trpc.media.videoerase.RemoveLogo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RemoveLogo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateRemoveLogoTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.videoerase.RemoveLogo/CreateRemoveLogoTask',
            video__erase__pb2.CreateRemoveLogoTaskRequest.SerializeToString,
            video__erase__pb2.CreateRemoveLogoTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeRemoveLogoTaskData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.videoerase.RemoveLogo/DescribeRemoveLogoTaskData',
            video__erase__pb2.DescribeRemoveLogoTaskDataRequest.SerializeToString,
            video__erase__pb2.DescribeRemoveLogoTaskDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class RemoveCaptionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateRemoveCaptionTask = channel.unary_unary(
                '/trpc.media.videoerase.RemoveCaption/CreateRemoveCaptionTask',
                request_serializer=video__erase__pb2.CreateRemoveCaptionTaskRequest.SerializeToString,
                response_deserializer=video__erase__pb2.CreateRemoveCaptionTaskResponse.FromString,
                )
        self.DescribeRemoveCaptionTaskData = channel.unary_unary(
                '/trpc.media.videoerase.RemoveCaption/DescribeRemoveCaptionTaskData',
                request_serializer=video__erase__pb2.DescribeRemoveCaptionTaskDataRequest.SerializeToString,
                response_deserializer=video__erase__pb2.DescribeRemoveCaptionTaskDataResponse.FromString,
                )


class RemoveCaptionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateRemoveCaptionTask(self, request, context):
        """@alias=/CreateRemoveCaptionTask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeRemoveCaptionTaskData(self, request, context):
        """@alias=/DescribeRemoveCaptionTaskData
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RemoveCaptionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateRemoveCaptionTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRemoveCaptionTask,
                    request_deserializer=video__erase__pb2.CreateRemoveCaptionTaskRequest.FromString,
                    response_serializer=video__erase__pb2.CreateRemoveCaptionTaskResponse.SerializeToString,
            ),
            'DescribeRemoveCaptionTaskData': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeRemoveCaptionTaskData,
                    request_deserializer=video__erase__pb2.DescribeRemoveCaptionTaskDataRequest.FromString,
                    response_serializer=video__erase__pb2.DescribeRemoveCaptionTaskDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trpc.media.videoerase.RemoveCaption', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RemoveCaption(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateRemoveCaptionTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.videoerase.RemoveCaption/CreateRemoveCaptionTask',
            video__erase__pb2.CreateRemoveCaptionTaskRequest.SerializeToString,
            video__erase__pb2.CreateRemoveCaptionTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeRemoveCaptionTaskData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.videoerase.RemoveCaption/DescribeRemoveCaptionTaskData',
            video__erase__pb2.DescribeRemoveCaptionTaskDataRequest.SerializeToString,
            video__erase__pb2.DescribeRemoveCaptionTaskDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
