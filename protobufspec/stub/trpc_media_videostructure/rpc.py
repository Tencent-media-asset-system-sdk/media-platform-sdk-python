# -*- coding: utf-8 -*-
"""This is RPC module
Code generated by trpc-go/trpc-go-cmdline. DO NOT EDIT.
Source: video_structure.proto
"""
from typing import List, Callable, Tuple

from trpc import client
from trpc import codec
from trpc import server
from trpc import context
from trpc.codec.message import Message
from . import pb

#pylint: disable=unnecessary-pass


# AITagService defines service
class AITagServicer:
    """Abstract base class of server"""
    
    #pylint: disable=invalid-name
    async def CreateAITagTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest) -> pb.CreateVideoStructureTaskResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')
    #pylint: disable=invalid-name
    async def DescribeAITagTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest) -> pb.DescribeAITagTaskDataResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')
    #pylint: disable=invalid-name
    async def DescribeAITagAudioTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest) -> pb.DescribeAITagAudioTaskDataResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')
    #pylint: disable=invalid-name
    async def DescribeAITagImageTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest) -> pb.DescribeAITagImageTaskDataResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')
    #pylint: disable=invalid-name
    async def DescribeAITagTextTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest) -> pb.DescribeAITagTextTaskDataResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')
    #pylint: disable=invalid-name
    async def DescribeVideoShotCover(self, ctx: context.Context, request: pb.DescribeVideoShotCoverRequest) -> pb.DescribeVideoShotCoverResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')

AITagServiceName = "trpc.media.videostructure.AITag"  # pylint: disable=invalid-name

# add AITagServicer to server
# pylint: disable=invalid-name
def register_AITagServicer_server(svr: server.Server, servicer: AITagServicer, fix_rpc_name: bool = False):
    """Register service to server"""
    rpc_method_handlers = []
    rpc_stream_handlers = []
    
    rpc_method_handlers.append(
        server.Method(
            name="/CreateAITagTask",
            req_cls=pb.CreateVideoStructureTaskRequest,
            rsp_cls=pb.CreateVideoStructureTaskResponse,
            impl_func=servicer.CreateAITagTask))
    
    rpc_method_handlers.append(
        server.Method(
            name="/DescribeAITagTaskData",
            req_cls=pb.DescribeAITagTaskDataRequest,
            rsp_cls=pb.DescribeAITagTaskDataResponse,
            impl_func=servicer.DescribeAITagTaskData))
    
    rpc_method_handlers.append(
        server.Method(
            name="/DescribeAITagAudioTaskData",
            req_cls=pb.DescribeAITagTaskDataRequest,
            rsp_cls=pb.DescribeAITagAudioTaskDataResponse,
            impl_func=servicer.DescribeAITagAudioTaskData))
    
    rpc_method_handlers.append(
        server.Method(
            name="/DescribeAITagImageTaskData",
            req_cls=pb.DescribeAITagTaskDataRequest,
            rsp_cls=pb.DescribeAITagImageTaskDataResponse,
            impl_func=servicer.DescribeAITagImageTaskData))
    
    rpc_method_handlers.append(
        server.Method(
            name="/DescribeAITagTextTaskData",
            req_cls=pb.DescribeAITagTaskDataRequest,
            rsp_cls=pb.DescribeAITagTextTaskDataResponse,
            impl_func=servicer.DescribeAITagTextTaskData))
    
    rpc_method_handlers.append(
        server.Method(
            name="/DescribeVideoShotCover",
            req_cls=pb.DescribeVideoShotCoverRequest,
            rsp_cls=pb.DescribeVideoShotCoverResponse,
            impl_func=servicer.DescribeVideoShotCover))
    
    desc = server.ServiceDesc(
        service_name="/" + AITagServiceName,
        methods=rpc_method_handlers)

    svr.register(desc, fix_rpc_name)


# client proxy
class AITagClientProxy:
    """Client proxy"""
    
    def CreateAITagTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest, options: List[Callable] = None) -> pb.CreateVideoStructureTaskResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncCreateAITagTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest, options: List[Callable] = None) -> pb.CreateVideoStructureTaskResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    
    def DescribeAITagTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagTaskDataResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncDescribeAITagTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagTaskDataResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    
    def DescribeAITagAudioTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagAudioTaskDataResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncDescribeAITagAudioTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagAudioTaskDataResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    
    def DescribeAITagImageTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagImageTaskDataResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncDescribeAITagImageTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagImageTaskDataResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    
    def DescribeAITagTextTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagTextTaskDataResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncDescribeAITagTextTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagTextTaskDataResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    
    def DescribeVideoShotCover(self, ctx: context.Context, request: pb.DescribeVideoShotCoverRequest, options: List[Callable] = None) -> pb.DescribeVideoShotCoverResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncDescribeVideoShotCover(self, ctx: context.Context, request: pb.DescribeVideoShotCoverRequest, options: List[Callable] = None) -> pb.DescribeVideoShotCoverResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    

class AITagClientProxyImpl(AITagClientProxy):
    """Client proxy implementation"""
    def __init__(self, service_name: str = None, fix_rpc_name: bool = True):
        self.client = client.get_client()
        self.options = {}

    @staticmethod
    def _clone_client_message(ctx: context.Context, rpc_name: str, callee_method: str) -> Tuple[context.Context, Message]:
        """Clone client message
        :param ctx: context of data processing.
        :param rpc_name: name of rpc.
        :param callee_method: method of callee
        :return: tuple
        """
        ctx, msg = codec.clone_client_message(ctx)
        msg.set_client_rpc_name(rpc_name)
        msg.set_callee_service_name(AITagServiceName)
        msg.set_callee_method(callee_method)
        return ctx, msg

    
    def CreateAITagTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest, options: List[Callable] = None) -> pb.CreateVideoStructureTaskResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.CreateVideoStructureTaskResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/CreateAITagTask', 'CreateAITagTask')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncCreateAITagTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest, options: List[Callable] = None) -> pb.CreateVideoStructureTaskResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.CreateVideoStructureTaskResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/CreateAITagTask', 'CreateAITagTask')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
    def DescribeAITagTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagTaskDataResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeAITagTaskDataResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeAITagTaskData', 'DescribeAITagTaskData')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncDescribeAITagTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagTaskDataResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeAITagTaskDataResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeAITagTaskData', 'DescribeAITagTaskData')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
    def DescribeAITagAudioTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagAudioTaskDataResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeAITagAudioTaskDataResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeAITagAudioTaskData', 'DescribeAITagAudioTaskData')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncDescribeAITagAudioTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagAudioTaskDataResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeAITagAudioTaskDataResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeAITagAudioTaskData', 'DescribeAITagAudioTaskData')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
    def DescribeAITagImageTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagImageTaskDataResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeAITagImageTaskDataResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeAITagImageTaskData', 'DescribeAITagImageTaskData')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncDescribeAITagImageTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagImageTaskDataResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeAITagImageTaskDataResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeAITagImageTaskData', 'DescribeAITagImageTaskData')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
    def DescribeAITagTextTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagTextTaskDataResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeAITagTextTaskDataResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeAITagTextTaskData', 'DescribeAITagTextTaskData')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncDescribeAITagTextTaskData(self, ctx: context.Context, request: pb.DescribeAITagTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAITagTextTaskDataResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeAITagTextTaskDataResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeAITagTextTaskData', 'DescribeAITagTextTaskData')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
    def DescribeVideoShotCover(self, ctx: context.Context, request: pb.DescribeVideoShotCoverRequest, options: List[Callable] = None) -> pb.DescribeVideoShotCoverResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeVideoShotCoverResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeVideoShotCover', 'DescribeVideoShotCover')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncDescribeVideoShotCover(self, ctx: context.Context, request: pb.DescribeVideoShotCoverRequest, options: List[Callable] = None) -> pb.DescribeVideoShotCoverResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeVideoShotCoverResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeVideoShotCover', 'DescribeVideoShotCover')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
# AICatalogService defines service
class AICatalogServicer:
    """Abstract base class of server"""
    
    #pylint: disable=invalid-name
    async def CreateAICatalogTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest) -> pb.CreateVideoStructureTaskResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')
    #pylint: disable=invalid-name
    async def DescribeAICatalogTaskData(self, ctx: context.Context, request: pb.DescribeAICatalogTaskDataRequest) -> pb.DescribeAICatalogTaskDataResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')

AICatalogServiceName = "trpc.media.videostructure.AICatalog"  # pylint: disable=invalid-name

# add AICatalogServicer to server
# pylint: disable=invalid-name
def register_AICatalogServicer_server(svr: server.Server, servicer: AICatalogServicer, fix_rpc_name: bool = False):
    """Register service to server"""
    rpc_method_handlers = []
    rpc_stream_handlers = []
    
    rpc_method_handlers.append(
        server.Method(
            name="/CreateAICatalogTask",
            req_cls=pb.CreateVideoStructureTaskRequest,
            rsp_cls=pb.CreateVideoStructureTaskResponse,
            impl_func=servicer.CreateAICatalogTask))
    
    rpc_method_handlers.append(
        server.Method(
            name="/DescribeAICatalogTaskData",
            req_cls=pb.DescribeAICatalogTaskDataRequest,
            rsp_cls=pb.DescribeAICatalogTaskDataResponse,
            impl_func=servicer.DescribeAICatalogTaskData))
    
    desc = server.ServiceDesc(
        service_name="/" + AICatalogServiceName,
        methods=rpc_method_handlers)

    svr.register(desc, fix_rpc_name)


# client proxy
class AICatalogClientProxy:
    """Client proxy"""
    
    def CreateAICatalogTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest, options: List[Callable] = None) -> pb.CreateVideoStructureTaskResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncCreateAICatalogTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest, options: List[Callable] = None) -> pb.CreateVideoStructureTaskResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    
    def DescribeAICatalogTaskData(self, ctx: context.Context, request: pb.DescribeAICatalogTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAICatalogTaskDataResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncDescribeAICatalogTaskData(self, ctx: context.Context, request: pb.DescribeAICatalogTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAICatalogTaskDataResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    

class AICatalogClientProxyImpl(AICatalogClientProxy):
    """Client proxy implementation"""
    def __init__(self, service_name: str = None, fix_rpc_name: bool = True):
        self.client = client.get_client()
        self.options = {}

    @staticmethod
    def _clone_client_message(ctx: context.Context, rpc_name: str, callee_method: str) -> Tuple[context.Context, Message]:
        """Clone client message
        :param ctx: context of data processing.
        :param rpc_name: name of rpc.
        :param callee_method: method of callee
        :return: tuple
        """
        ctx, msg = codec.clone_client_message(ctx)
        msg.set_client_rpc_name(rpc_name)
        msg.set_callee_service_name(AICatalogServiceName)
        msg.set_callee_method(callee_method)
        return ctx, msg

    
    def CreateAICatalogTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest, options: List[Callable] = None) -> pb.CreateVideoStructureTaskResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.CreateVideoStructureTaskResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/CreateAICatalogTask', 'CreateAICatalogTask')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncCreateAICatalogTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest, options: List[Callable] = None) -> pb.CreateVideoStructureTaskResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.CreateVideoStructureTaskResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/CreateAICatalogTask', 'CreateAICatalogTask')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
    def DescribeAICatalogTaskData(self, ctx: context.Context, request: pb.DescribeAICatalogTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAICatalogTaskDataResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeAICatalogTaskDataResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeAICatalogTaskData', 'DescribeAICatalogTaskData')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncDescribeAICatalogTaskData(self, ctx: context.Context, request: pb.DescribeAICatalogTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAICatalogTaskDataResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeAICatalogTaskDataResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeAICatalogTaskData', 'DescribeAICatalogTaskData')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
# AICutService defines service
class AICutServicer:
    """Abstract base class of server"""
    
    #pylint: disable=invalid-name
    async def CreateAICutTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest) -> pb.CreateVideoStructureTaskResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')
    #pylint: disable=invalid-name
    async def DescribeAICutTaskData(self, ctx: context.Context, request: pb.DescribeAICutTaskDataRequest) -> pb.DescribeAICutTaskDataResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')

AICutServiceName = "trpc.media.videostructure.AICut"  # pylint: disable=invalid-name

# add AICutServicer to server
# pylint: disable=invalid-name
def register_AICutServicer_server(svr: server.Server, servicer: AICutServicer, fix_rpc_name: bool = False):
    """Register service to server"""
    rpc_method_handlers = []
    rpc_stream_handlers = []
    
    rpc_method_handlers.append(
        server.Method(
            name="/CreateAICutTask",
            req_cls=pb.CreateVideoStructureTaskRequest,
            rsp_cls=pb.CreateVideoStructureTaskResponse,
            impl_func=servicer.CreateAICutTask))
    
    rpc_method_handlers.append(
        server.Method(
            name="/DescribeAICutTaskData",
            req_cls=pb.DescribeAICutTaskDataRequest,
            rsp_cls=pb.DescribeAICutTaskDataResponse,
            impl_func=servicer.DescribeAICutTaskData))
    
    desc = server.ServiceDesc(
        service_name="/" + AICutServiceName,
        methods=rpc_method_handlers)

    svr.register(desc, fix_rpc_name)


# client proxy
class AICutClientProxy:
    """Client proxy"""
    
    def CreateAICutTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest, options: List[Callable] = None) -> pb.CreateVideoStructureTaskResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncCreateAICutTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest, options: List[Callable] = None) -> pb.CreateVideoStructureTaskResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    
    def DescribeAICutTaskData(self, ctx: context.Context, request: pb.DescribeAICutTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAICutTaskDataResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncDescribeAICutTaskData(self, ctx: context.Context, request: pb.DescribeAICutTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAICutTaskDataResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    

class AICutClientProxyImpl(AICutClientProxy):
    """Client proxy implementation"""
    def __init__(self, service_name: str = None, fix_rpc_name: bool = True):
        self.client = client.get_client()
        self.options = {}

    @staticmethod
    def _clone_client_message(ctx: context.Context, rpc_name: str, callee_method: str) -> Tuple[context.Context, Message]:
        """Clone client message
        :param ctx: context of data processing.
        :param rpc_name: name of rpc.
        :param callee_method: method of callee
        :return: tuple
        """
        ctx, msg = codec.clone_client_message(ctx)
        msg.set_client_rpc_name(rpc_name)
        msg.set_callee_service_name(AICutServiceName)
        msg.set_callee_method(callee_method)
        return ctx, msg

    
    def CreateAICutTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest, options: List[Callable] = None) -> pb.CreateVideoStructureTaskResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.CreateVideoStructureTaskResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/CreateAICutTask', 'CreateAICutTask')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncCreateAICutTask(self, ctx: context.Context, request: pb.CreateVideoStructureTaskRequest, options: List[Callable] = None) -> pb.CreateVideoStructureTaskResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.CreateVideoStructureTaskResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/CreateAICutTask', 'CreateAICutTask')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
    def DescribeAICutTaskData(self, ctx: context.Context, request: pb.DescribeAICutTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAICutTaskDataResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeAICutTaskDataResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeAICutTaskData', 'DescribeAICutTaskData')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncDescribeAICutTaskData(self, ctx: context.Context, request: pb.DescribeAICutTaskDataRequest, options: List[Callable] = None) -> pb.DescribeAICutTaskDataResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeAICutTaskDataResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeAICutTaskData', 'DescribeAICutTaskData')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    