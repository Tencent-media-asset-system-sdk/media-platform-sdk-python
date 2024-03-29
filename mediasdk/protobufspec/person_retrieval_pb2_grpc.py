# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import mediasdk.grpc_mock as grpc

from . import person_retrieval_pb2 as person__retrieval__pb2


class PersonRetrievalStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePersonRetrievalTask = channel.unary_unary(
                '/trpc.media.personretrieval.PersonRetrieval/CreatePersonRetrievalTask',
                request_serializer=person__retrieval__pb2.CreatePersonRetrievalTaskRequest.SerializeToString,
                response_deserializer=person__retrieval__pb2.CreatePersonRetrievalTaskResponse.FromString,
                )
        self.DescribePersonRetrievalTaskData = channel.unary_unary(
                '/trpc.media.personretrieval.PersonRetrieval/DescribePersonRetrievalTaskData',
                request_serializer=person__retrieval__pb2.DescribePersonRetrievalTaskDataRequest.SerializeToString,
                response_deserializer=person__retrieval__pb2.DescribePersonRetrievalTaskDataResponse.FromString,
                )
        self.RetrievalImage = channel.unary_unary(
                '/trpc.media.personretrieval.PersonRetrieval/RetrievalImage',
                request_serializer=person__retrieval__pb2.RetrievalImageRequest.SerializeToString,
                response_deserializer=person__retrieval__pb2.RetrievalImageResponse.FromString,
                )


class PersonRetrievalServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreatePersonRetrievalTask(self, request, context):
        """@alias=/CreatePersonRetrievalTask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribePersonRetrievalTaskData(self, request, context):
        """@alias=/DescribePersonRetrievalTaskData
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrievalImage(self, request, context):
        """@alias=/RetrievalImage
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PersonRetrievalServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePersonRetrievalTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePersonRetrievalTask,
                    request_deserializer=person__retrieval__pb2.CreatePersonRetrievalTaskRequest.FromString,
                    response_serializer=person__retrieval__pb2.CreatePersonRetrievalTaskResponse.SerializeToString,
            ),
            'DescribePersonRetrievalTaskData': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribePersonRetrievalTaskData,
                    request_deserializer=person__retrieval__pb2.DescribePersonRetrievalTaskDataRequest.FromString,
                    response_serializer=person__retrieval__pb2.DescribePersonRetrievalTaskDataResponse.SerializeToString,
            ),
            'RetrievalImage': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrievalImage,
                    request_deserializer=person__retrieval__pb2.RetrievalImageRequest.FromString,
                    response_serializer=person__retrieval__pb2.RetrievalImageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trpc.media.personretrieval.PersonRetrieval', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PersonRetrieval(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreatePersonRetrievalTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.personretrieval.PersonRetrieval/CreatePersonRetrievalTask',
            person__retrieval__pb2.CreatePersonRetrievalTaskRequest.SerializeToString,
            person__retrieval__pb2.CreatePersonRetrievalTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribePersonRetrievalTaskData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.personretrieval.PersonRetrieval/DescribePersonRetrievalTaskData',
            person__retrieval__pb2.DescribePersonRetrievalTaskDataRequest.SerializeToString,
            person__retrieval__pb2.DescribePersonRetrievalTaskDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrievalImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.personretrieval.PersonRetrieval/RetrievalImage',
            person__retrieval__pb2.RetrievalImageRequest.SerializeToString,
            person__retrieval__pb2.RetrievalImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
