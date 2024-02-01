# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import mediasdk.grpc_mock as grpc

from . import task_pb2 as task__pb2


class TaskStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DescribeSupportedMediaTypes = channel.unary_unary(
                '/trpc.media.task.Task/DescribeSupportedMediaTypes',
                request_serializer=task__pb2.DescribeSupportedMediaTypesRequest.SerializeToString,
                response_deserializer=task__pb2.DescribeSupportedMediaTypesResponse.FromString,
                )
        self.CreateTask = channel.unary_unary(
                '/trpc.media.task.Task/CreateTask',
                request_serializer=task__pb2.CreateTaskRequest.SerializeToString,
                response_deserializer=task__pb2.CreateTaskResponse.FromString,
                )
        self.DescribeTask = channel.unary_unary(
                '/trpc.media.task.Task/DescribeTask',
                request_serializer=task__pb2.DescribeTaskRequest.SerializeToString,
                response_deserializer=task__pb2.DescribeTaskResponse.FromString,
                )
        self.DescribeTasks = channel.unary_unary(
                '/trpc.media.task.Task/DescribeTasks',
                request_serializer=task__pb2.DescribeTasksRequest.SerializeToString,
                response_deserializer=task__pb2.DescribeTasksResponse.FromString,
                )
        self.StartTask = channel.unary_unary(
                '/trpc.media.task.Task/StartTask',
                request_serializer=task__pb2.StartTaskRequest.SerializeToString,
                response_deserializer=task__pb2.StartTaskResponse.FromString,
                )
        self.StartTasks = channel.unary_unary(
                '/trpc.media.task.Task/StartTasks',
                request_serializer=task__pb2.StartTasksRequest.SerializeToString,
                response_deserializer=task__pb2.StartTasksResponse.FromString,
                )
        self.StopTask = channel.unary_unary(
                '/trpc.media.task.Task/StopTask',
                request_serializer=task__pb2.StopTaskRequest.SerializeToString,
                response_deserializer=task__pb2.StopTaskResponse.FromString,
                )
        self.StopTasks = channel.unary_unary(
                '/trpc.media.task.Task/StopTasks',
                request_serializer=task__pb2.StopTasksRequest.SerializeToString,
                response_deserializer=task__pb2.StopTasksResponse.FromString,
                )
        self.DeleteTask = channel.unary_unary(
                '/trpc.media.task.Task/DeleteTask',
                request_serializer=task__pb2.DeleteTaskRequest.SerializeToString,
                response_deserializer=task__pb2.DeleteTaskResponse.FromString,
                )
        self.TopTask = channel.unary_unary(
                '/trpc.media.task.Task/TopTask',
                request_serializer=task__pb2.TopTaskRequest.SerializeToString,
                response_deserializer=task__pb2.TopTaskResponse.FromString,
                )
        self.DescribeTaskDetail = channel.unary_unary(
                '/trpc.media.task.Task/DescribeTaskDetail',
                request_serializer=task__pb2.DescribeTaskDetailRequest.SerializeToString,
                response_deserializer=task__pb2.DescribeTaskDetailResponse.FromString,
                )
        self.ModifyTaskData = channel.unary_unary(
                '/trpc.media.task.Task/ModifyTaskData',
                request_serializer=task__pb2.ModifyTaskDataRequest.SerializeToString,
                response_deserializer=task__pb2.ModifyTaskDataResponse.FromString,
                )
        self.DescribeTaskListFile = channel.unary_unary(
                '/trpc.media.task.Task/DescribeTaskListFile',
                request_serializer=task__pb2.DescribeTaskListFileRequest.SerializeToString,
                response_deserializer=task__pb2.DescribeTaskListFileResponse.FromString,
                )
        self.DescribeStatistics = channel.unary_unary(
                '/trpc.media.task.Task/DescribeStatistics',
                request_serializer=task__pb2.DescribeStatisticsRequest.SerializeToString,
                response_deserializer=task__pb2.DescribeStatisticsResponse.FromString,
                )
        self.DescribeWorkflowProgress = channel.unary_unary(
                '/trpc.media.task.Task/DescribeWorkflowProgress',
                request_serializer=task__pb2.DescribeWorkflowProgressRequest.SerializeToString,
                response_deserializer=task__pb2.DescribeWorkflowProgressResponse.FromString,
                )
        self.StopTasksInner = channel.unary_unary(
                '/trpc.media.task.Task/StopTasksInner',
                request_serializer=task__pb2.StopTasksRequest.SerializeToString,
                response_deserializer=task__pb2.StopTasksResponse.FromString,
                )
        self.CheckWorkflowTemplate = channel.unary_unary(
                '/trpc.media.task.Task/CheckWorkflowTemplate',
                request_serializer=task__pb2.CheckWorkflowTemplateRequest.SerializeToString,
                response_deserializer=task__pb2.CheckWorkflowTemplateResponse.FromString,
                )
        self.DescribeTagAnalyseInput = channel.unary_unary(
                '/trpc.media.task.Task/DescribeTagAnalyseInput',
                request_serializer=task__pb2.DescribeTagAnalyseInputRequest.SerializeToString,
                response_deserializer=task__pb2.DescribeTagAnalyseInputResponse.FromString,
                )


class TaskServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DescribeSupportedMediaTypes(self, request, context):
        """任务管理
        @alias=/DescribeSupportedMediaTypes
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTask(self, request, context):
        """@alias=/CreateTask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeTask(self, request, context):
        """@alias=/DescribeTask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeTasks(self, request, context):
        """@alias=/DescribeTasks
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartTask(self, request, context):
        """@alias=/StartTask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartTasks(self, request, context):
        """@alias=/StartTasks
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopTask(self, request, context):
        """@alias=/StopTask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopTasks(self, request, context):
        """@alias=/StopTasks
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTask(self, request, context):
        """@alias=/DeleteTask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TopTask(self, request, context):
        """@alias=/TopTask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeTaskDetail(self, request, context):
        """@alias=/DescribeTaskDetail
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModifyTaskData(self, request, context):
        """标签修改
        @alias=/ModifyTaskData
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeTaskListFile(self, request, context):
        """数据统计相关
        @alias=/DescribeTaskListFile
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeStatistics(self, request, context):
        """@alias=/DescribeStatistics
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeWorkflowProgress(self, request, context):
        """workflow
        @alias=/DescribeWorkflowProgress
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopTasksInner(self, request, context):
        """内部使用接口
        @alias=/StopTasksInner
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckWorkflowTemplate(self, request, context):
        """@alias=/CheckWorkflowTemplate
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeTagAnalyseInput(self, request, context):
        """标签分析任务输入太大，不适合作为 ppl 参数传入，采用拉取方式
        @alias=/DescribeTagAnalyseInput
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DescribeSupportedMediaTypes': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeSupportedMediaTypes,
                    request_deserializer=task__pb2.DescribeSupportedMediaTypesRequest.FromString,
                    response_serializer=task__pb2.DescribeSupportedMediaTypesResponse.SerializeToString,
            ),
            'CreateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTask,
                    request_deserializer=task__pb2.CreateTaskRequest.FromString,
                    response_serializer=task__pb2.CreateTaskResponse.SerializeToString,
            ),
            'DescribeTask': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeTask,
                    request_deserializer=task__pb2.DescribeTaskRequest.FromString,
                    response_serializer=task__pb2.DescribeTaskResponse.SerializeToString,
            ),
            'DescribeTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeTasks,
                    request_deserializer=task__pb2.DescribeTasksRequest.FromString,
                    response_serializer=task__pb2.DescribeTasksResponse.SerializeToString,
            ),
            'StartTask': grpc.unary_unary_rpc_method_handler(
                    servicer.StartTask,
                    request_deserializer=task__pb2.StartTaskRequest.FromString,
                    response_serializer=task__pb2.StartTaskResponse.SerializeToString,
            ),
            'StartTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.StartTasks,
                    request_deserializer=task__pb2.StartTasksRequest.FromString,
                    response_serializer=task__pb2.StartTasksResponse.SerializeToString,
            ),
            'StopTask': grpc.unary_unary_rpc_method_handler(
                    servicer.StopTask,
                    request_deserializer=task__pb2.StopTaskRequest.FromString,
                    response_serializer=task__pb2.StopTaskResponse.SerializeToString,
            ),
            'StopTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.StopTasks,
                    request_deserializer=task__pb2.StopTasksRequest.FromString,
                    response_serializer=task__pb2.StopTasksResponse.SerializeToString,
            ),
            'DeleteTask': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTask,
                    request_deserializer=task__pb2.DeleteTaskRequest.FromString,
                    response_serializer=task__pb2.DeleteTaskResponse.SerializeToString,
            ),
            'TopTask': grpc.unary_unary_rpc_method_handler(
                    servicer.TopTask,
                    request_deserializer=task__pb2.TopTaskRequest.FromString,
                    response_serializer=task__pb2.TopTaskResponse.SerializeToString,
            ),
            'DescribeTaskDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeTaskDetail,
                    request_deserializer=task__pb2.DescribeTaskDetailRequest.FromString,
                    response_serializer=task__pb2.DescribeTaskDetailResponse.SerializeToString,
            ),
            'ModifyTaskData': grpc.unary_unary_rpc_method_handler(
                    servicer.ModifyTaskData,
                    request_deserializer=task__pb2.ModifyTaskDataRequest.FromString,
                    response_serializer=task__pb2.ModifyTaskDataResponse.SerializeToString,
            ),
            'DescribeTaskListFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeTaskListFile,
                    request_deserializer=task__pb2.DescribeTaskListFileRequest.FromString,
                    response_serializer=task__pb2.DescribeTaskListFileResponse.SerializeToString,
            ),
            'DescribeStatistics': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeStatistics,
                    request_deserializer=task__pb2.DescribeStatisticsRequest.FromString,
                    response_serializer=task__pb2.DescribeStatisticsResponse.SerializeToString,
            ),
            'DescribeWorkflowProgress': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeWorkflowProgress,
                    request_deserializer=task__pb2.DescribeWorkflowProgressRequest.FromString,
                    response_serializer=task__pb2.DescribeWorkflowProgressResponse.SerializeToString,
            ),
            'StopTasksInner': grpc.unary_unary_rpc_method_handler(
                    servicer.StopTasksInner,
                    request_deserializer=task__pb2.StopTasksRequest.FromString,
                    response_serializer=task__pb2.StopTasksResponse.SerializeToString,
            ),
            'CheckWorkflowTemplate': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckWorkflowTemplate,
                    request_deserializer=task__pb2.CheckWorkflowTemplateRequest.FromString,
                    response_serializer=task__pb2.CheckWorkflowTemplateResponse.SerializeToString,
            ),
            'DescribeTagAnalyseInput': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeTagAnalyseInput,
                    request_deserializer=task__pb2.DescribeTagAnalyseInputRequest.FromString,
                    response_serializer=task__pb2.DescribeTagAnalyseInputResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trpc.media.task.Task', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Task(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DescribeSupportedMediaTypes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/DescribeSupportedMediaTypes',
            task__pb2.DescribeSupportedMediaTypesRequest.SerializeToString,
            task__pb2.DescribeSupportedMediaTypesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/CreateTask',
            task__pb2.CreateTaskRequest.SerializeToString,
            task__pb2.CreateTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/DescribeTask',
            task__pb2.DescribeTaskRequest.SerializeToString,
            task__pb2.DescribeTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/DescribeTasks',
            task__pb2.DescribeTasksRequest.SerializeToString,
            task__pb2.DescribeTasksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/StartTask',
            task__pb2.StartTaskRequest.SerializeToString,
            task__pb2.StartTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/StartTasks',
            task__pb2.StartTasksRequest.SerializeToString,
            task__pb2.StartTasksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/StopTask',
            task__pb2.StopTaskRequest.SerializeToString,
            task__pb2.StopTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/StopTasks',
            task__pb2.StopTasksRequest.SerializeToString,
            task__pb2.StopTasksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/DeleteTask',
            task__pb2.DeleteTaskRequest.SerializeToString,
            task__pb2.DeleteTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TopTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/TopTask',
            task__pb2.TopTaskRequest.SerializeToString,
            task__pb2.TopTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeTaskDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/DescribeTaskDetail',
            task__pb2.DescribeTaskDetailRequest.SerializeToString,
            task__pb2.DescribeTaskDetailResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModifyTaskData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/ModifyTaskData',
            task__pb2.ModifyTaskDataRequest.SerializeToString,
            task__pb2.ModifyTaskDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeTaskListFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/DescribeTaskListFile',
            task__pb2.DescribeTaskListFileRequest.SerializeToString,
            task__pb2.DescribeTaskListFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeStatistics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/DescribeStatistics',
            task__pb2.DescribeStatisticsRequest.SerializeToString,
            task__pb2.DescribeStatisticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeWorkflowProgress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/DescribeWorkflowProgress',
            task__pb2.DescribeWorkflowProgressRequest.SerializeToString,
            task__pb2.DescribeWorkflowProgressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopTasksInner(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/StopTasksInner',
            task__pb2.StopTasksRequest.SerializeToString,
            task__pb2.StopTasksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckWorkflowTemplate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/CheckWorkflowTemplate',
            task__pb2.CheckWorkflowTemplateRequest.SerializeToString,
            task__pb2.CheckWorkflowTemplateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeTagAnalyseInput(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.Task/DescribeTagAnalyseInput',
            task__pb2.DescribeTagAnalyseInputRequest.SerializeToString,
            task__pb2.DescribeTagAnalyseInputResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class TaskCallbackStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FinishedTask = channel.unary_unary(
                '/trpc.media.task.TaskCallback/FinishedTask',
                request_serializer=task__pb2.FinishedTaskRequest.SerializeToString,
                response_deserializer=task__pb2.FinishedTaskResponse.FromString,
                )


class TaskCallbackServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FinishedTask(self, request, context):
        """@alias=/FinishedTask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskCallbackServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FinishedTask': grpc.unary_unary_rpc_method_handler(
                    servicer.FinishedTask,
                    request_deserializer=task__pb2.FinishedTaskRequest.FromString,
                    response_serializer=task__pb2.FinishedTaskResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trpc.media.task.TaskCallback', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TaskCallback(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FinishedTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trpc.media.task.TaskCallback/FinishedTask',
            task__pb2.FinishedTaskRequest.SerializeToString,
            task__pb2.FinishedTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)