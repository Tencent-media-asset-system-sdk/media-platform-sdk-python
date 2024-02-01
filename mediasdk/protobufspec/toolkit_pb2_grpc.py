# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import mediasdk.grpc_mock as grpc

from . import toolkit_pb2 as toolkit__pb2


class ToolkitStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DescribeToolkits = channel.unary_unary(
                '/trpc.media.toolkit.Toolkit/DescribeToolkits',
                request_serializer=toolkit__pb2.DescribeToolkitsRequest.SerializeToString,
                response_deserializer=toolkit__pb2.DescribeToolkitsResponse.FromString,
                )


class ToolkitServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DescribeToolkits(self, request, context):
        """@alias=/DescribeToolkits
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ToolkitServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DescribeToolkits': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeToolkits,
                    request_deserializer=toolkit__pb2.DescribeToolkitsRequest.FromString,
                    response_serializer=toolkit__pb2.DescribeToolkitsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trpc.media.toolkit.Toolkit', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Toolkit(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DescribeToolkits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.toolkit.Toolkit/DescribeToolkits',
            toolkit__pb2.DescribeToolkitsRequest.SerializeToString,
            toolkit__pb2.DescribeToolkitsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)