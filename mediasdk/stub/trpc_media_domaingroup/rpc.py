# -*- coding: utf-8 -*-
"""This is RPC module
Code generated by trpc-go/trpc-go-cmdline. DO NOT EDIT.
Source: domain_group.proto
"""
from typing import List, Callable, Tuple

from trpc import client
from trpc import codec
from trpc import server
from trpc import context
from trpc.codec.message import Message
from . import pb

#pylint: disable=unnecessary-pass


# DomainGroupService defines service
class DomainGroupServicer:
    """Abstract base class of server"""
    
    #pylint: disable=invalid-name
    async def CreateDomainGroup(self, ctx: context.Context, request: pb.CreateDomainGroupRequest) -> pb.CreateDomainGroupResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')
    #pylint: disable=invalid-name
    async def DescribeDomainGroups(self, ctx: context.Context, request: pb.DescribeDomainGroupsRequest) -> pb.DescribeDomainGroupsResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')
    #pylint: disable=invalid-name
    async def DescribeDomainGroupDetails(self, ctx: context.Context, request: pb.DescribeDomainGroupDetailsRequest) -> pb.DescribeDomainGroupDetailsResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')
    #pylint: disable=invalid-name
    async def AddMediasToDomainGroups(self, ctx: context.Context, request: pb.AddMediasToDomainGroupsRequest) -> pb.AddMediasToDomainGroupsResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')
    #pylint: disable=invalid-name
    async def RemoveMediasFromDomainGroups(self, ctx: context.Context, request: pb.RemoveMediasFromDomainGroupsRequest) -> pb.RemoveMediasFromDomainGroupsResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')
    #pylint: disable=invalid-name
    async def DeleteDomainGroups(self, ctx: context.Context, request: pb.DeleteDomainGroupsRequest) -> pb.DeleteDomainGroupsResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')
    #pylint: disable=invalid-name
    async def ModifyDomainGroup(self, ctx: context.Context, request: pb.ModifyDomainGroupRequest) -> pb.ModifyDomainGroupResponse:
        """Abstract rpc method of server
        :param ctx: context of data processing.
        :param request: object of pb.
        """
        raise NotImplementedError('Method not implemented!')

DomainGroupServiceName = "trpc.media.domaingroup.DomainGroup"  # pylint: disable=invalid-name

# add DomainGroupServicer to server
# pylint: disable=invalid-name
def register_DomainGroupServicer_server(svr: server.Server, servicer: DomainGroupServicer, fix_rpc_name: bool = False):
    """Register service to server"""
    rpc_method_handlers = []
    rpc_stream_handlers = []
    
    rpc_method_handlers.append(
        server.Method(
            name="/CreateDomainGroup",
            req_cls=pb.CreateDomainGroupRequest,
            rsp_cls=pb.CreateDomainGroupResponse,
            impl_func=servicer.CreateDomainGroup))
    
    rpc_method_handlers.append(
        server.Method(
            name="/DescribeDomainGroups",
            req_cls=pb.DescribeDomainGroupsRequest,
            rsp_cls=pb.DescribeDomainGroupsResponse,
            impl_func=servicer.DescribeDomainGroups))
    
    rpc_method_handlers.append(
        server.Method(
            name="/DescribeDomainGroupDetails",
            req_cls=pb.DescribeDomainGroupDetailsRequest,
            rsp_cls=pb.DescribeDomainGroupDetailsResponse,
            impl_func=servicer.DescribeDomainGroupDetails))
    
    rpc_method_handlers.append(
        server.Method(
            name="/AddMediasToDomainGroups",
            req_cls=pb.AddMediasToDomainGroupsRequest,
            rsp_cls=pb.AddMediasToDomainGroupsResponse,
            impl_func=servicer.AddMediasToDomainGroups))
    
    rpc_method_handlers.append(
        server.Method(
            name="/RemoveMediasFromDomainGroups",
            req_cls=pb.RemoveMediasFromDomainGroupsRequest,
            rsp_cls=pb.RemoveMediasFromDomainGroupsResponse,
            impl_func=servicer.RemoveMediasFromDomainGroups))
    
    rpc_method_handlers.append(
        server.Method(
            name="/DeleteDomainGroups",
            req_cls=pb.DeleteDomainGroupsRequest,
            rsp_cls=pb.DeleteDomainGroupsResponse,
            impl_func=servicer.DeleteDomainGroups))
    
    rpc_method_handlers.append(
        server.Method(
            name="/ModifyDomainGroup",
            req_cls=pb.ModifyDomainGroupRequest,
            rsp_cls=pb.ModifyDomainGroupResponse,
            impl_func=servicer.ModifyDomainGroup))
    
    desc = server.ServiceDesc(
        service_name="/" + DomainGroupServiceName,
        methods=rpc_method_handlers)

    svr.register(desc, fix_rpc_name)


# client proxy
class DomainGroupClientProxy:
    """Client proxy"""
    
    def CreateDomainGroup(self, ctx: context.Context, request: pb.CreateDomainGroupRequest, options: List[Callable] = None) -> pb.CreateDomainGroupResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncCreateDomainGroup(self, ctx: context.Context, request: pb.CreateDomainGroupRequest, options: List[Callable] = None) -> pb.CreateDomainGroupResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    
    def DescribeDomainGroups(self, ctx: context.Context, request: pb.DescribeDomainGroupsRequest, options: List[Callable] = None) -> pb.DescribeDomainGroupsResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncDescribeDomainGroups(self, ctx: context.Context, request: pb.DescribeDomainGroupsRequest, options: List[Callable] = None) -> pb.DescribeDomainGroupsResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    
    def DescribeDomainGroupDetails(self, ctx: context.Context, request: pb.DescribeDomainGroupDetailsRequest, options: List[Callable] = None) -> pb.DescribeDomainGroupDetailsResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncDescribeDomainGroupDetails(self, ctx: context.Context, request: pb.DescribeDomainGroupDetailsRequest, options: List[Callable] = None) -> pb.DescribeDomainGroupDetailsResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    
    def AddMediasToDomainGroups(self, ctx: context.Context, request: pb.AddMediasToDomainGroupsRequest, options: List[Callable] = None) -> pb.AddMediasToDomainGroupsResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncAddMediasToDomainGroups(self, ctx: context.Context, request: pb.AddMediasToDomainGroupsRequest, options: List[Callable] = None) -> pb.AddMediasToDomainGroupsResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    
    def RemoveMediasFromDomainGroups(self, ctx: context.Context, request: pb.RemoveMediasFromDomainGroupsRequest, options: List[Callable] = None) -> pb.RemoveMediasFromDomainGroupsResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncRemoveMediasFromDomainGroups(self, ctx: context.Context, request: pb.RemoveMediasFromDomainGroupsRequest, options: List[Callable] = None) -> pb.RemoveMediasFromDomainGroupsResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    
    def DeleteDomainGroups(self, ctx: context.Context, request: pb.DeleteDomainGroupsRequest, options: List[Callable] = None) -> pb.DeleteDomainGroupsResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncDeleteDomainGroups(self, ctx: context.Context, request: pb.DeleteDomainGroupsRequest, options: List[Callable] = None) -> pb.DeleteDomainGroupsResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    
    def ModifyDomainGroup(self, ctx: context.Context, request: pb.ModifyDomainGroupRequest, options: List[Callable] = None) -> pb.ModifyDomainGroupResponse:
        """Client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass

    async def asyncModifyDomainGroup(self, ctx: context.Context, request: pb.ModifyDomainGroupRequest, options: List[Callable] = None) -> pb.ModifyDomainGroupResponse:
        """Async client stream method
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of rsp pb
        """
        pass
    

class DomainGroupClientProxyImpl(DomainGroupClientProxy):
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
        msg.set_callee_service_name(DomainGroupServiceName)
        msg.set_callee_method(callee_method)
        return ctx, msg

    
    def CreateDomainGroup(self, ctx: context.Context, request: pb.CreateDomainGroupRequest, options: List[Callable] = None) -> pb.CreateDomainGroupResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.CreateDomainGroupResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/CreateDomainGroup', 'CreateDomainGroup')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncCreateDomainGroup(self, ctx: context.Context, request: pb.CreateDomainGroupRequest, options: List[Callable] = None) -> pb.CreateDomainGroupResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.CreateDomainGroupResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/CreateDomainGroup', 'CreateDomainGroup')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
    def DescribeDomainGroups(self, ctx: context.Context, request: pb.DescribeDomainGroupsRequest, options: List[Callable] = None) -> pb.DescribeDomainGroupsResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeDomainGroupsResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeDomainGroups', 'DescribeDomainGroups')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncDescribeDomainGroups(self, ctx: context.Context, request: pb.DescribeDomainGroupsRequest, options: List[Callable] = None) -> pb.DescribeDomainGroupsResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeDomainGroupsResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeDomainGroups', 'DescribeDomainGroups')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
    def DescribeDomainGroupDetails(self, ctx: context.Context, request: pb.DescribeDomainGroupDetailsRequest, options: List[Callable] = None) -> pb.DescribeDomainGroupDetailsResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeDomainGroupDetailsResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeDomainGroupDetails', 'DescribeDomainGroupDetails')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncDescribeDomainGroupDetails(self, ctx: context.Context, request: pb.DescribeDomainGroupDetailsRequest, options: List[Callable] = None) -> pb.DescribeDomainGroupDetailsResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DescribeDomainGroupDetailsResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DescribeDomainGroupDetails', 'DescribeDomainGroupDetails')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
    def AddMediasToDomainGroups(self, ctx: context.Context, request: pb.AddMediasToDomainGroupsRequest, options: List[Callable] = None) -> pb.AddMediasToDomainGroupsResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.AddMediasToDomainGroupsResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/AddMediasToDomainGroups', 'AddMediasToDomainGroups')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncAddMediasToDomainGroups(self, ctx: context.Context, request: pb.AddMediasToDomainGroupsRequest, options: List[Callable] = None) -> pb.AddMediasToDomainGroupsResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.AddMediasToDomainGroupsResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/AddMediasToDomainGroups', 'AddMediasToDomainGroups')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
    def RemoveMediasFromDomainGroups(self, ctx: context.Context, request: pb.RemoveMediasFromDomainGroupsRequest, options: List[Callable] = None) -> pb.RemoveMediasFromDomainGroupsResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.RemoveMediasFromDomainGroupsResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/RemoveMediasFromDomainGroups', 'RemoveMediasFromDomainGroups')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncRemoveMediasFromDomainGroups(self, ctx: context.Context, request: pb.RemoveMediasFromDomainGroupsRequest, options: List[Callable] = None) -> pb.RemoveMediasFromDomainGroupsResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.RemoveMediasFromDomainGroupsResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/RemoveMediasFromDomainGroups', 'RemoveMediasFromDomainGroups')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
    def DeleteDomainGroups(self, ctx: context.Context, request: pb.DeleteDomainGroupsRequest, options: List[Callable] = None) -> pb.DeleteDomainGroupsResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DeleteDomainGroupsResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DeleteDomainGroups', 'DeleteDomainGroups')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncDeleteDomainGroups(self, ctx: context.Context, request: pb.DeleteDomainGroupsRequest, options: List[Callable] = None) -> pb.DeleteDomainGroupsResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.DeleteDomainGroupsResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/DeleteDomainGroups', 'DeleteDomainGroups')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    
    def ModifyDomainGroup(self, ctx: context.Context, request: pb.ModifyDomainGroupRequest, options: List[Callable] = None) -> pb.ModifyDomainGroupResponse:
        """Client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.ModifyDomainGroupResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/ModifyDomainGroup', 'ModifyDomainGroup')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncModifyDomainGroup(self, ctx: context.Context, request: pb.ModifyDomainGroupRequest, options: List[Callable] = None) -> pb.ModifyDomainGroupResponse:
        """Async client rpc method implementation
        :param ctx: context of data processing.
        :param request: object of pb.
        :param options: list of setting functions
        :return: object of pb
        """
        rsp_cls = pb.ModifyDomainGroupResponse
        options = options or []

        ctx, msg = self._clone_client_message(ctx, '/ModifyDomainGroup', 'ModifyDomainGroup')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp
    