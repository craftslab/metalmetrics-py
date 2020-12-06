# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import service_pb2 as service__pb2


class ServiceProtoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendBare = channel.unary_unary(
            "/service.ServiceProto/SendBare",
            request_serializer=service__pb2.BareRequest.SerializeToString,
            response_deserializer=service__pb2.BareReply.FromString,
        )
        self.SendContainer = channel.unary_unary(
            "/service.ServiceProto/SendContainer",
            request_serializer=service__pb2.ContainerRequest.SerializeToString,
            response_deserializer=service__pb2.ContainerReply.FromString,
        )
        self.SendKubernetes = channel.unary_unary(
            "/service.ServiceProto/SendKubernetes",
            request_serializer=service__pb2.KubernetesRequest.SerializeToString,
            response_deserializer=service__pb2.KubernetesReply.FromString,
        )


class ServiceProtoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendBare(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SendContainer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SendKubernetes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ServiceProtoServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SendBare": grpc.unary_unary_rpc_method_handler(
            servicer.SendBare,
            request_deserializer=service__pb2.BareRequest.FromString,
            response_serializer=service__pb2.BareReply.SerializeToString,
        ),
        "SendContainer": grpc.unary_unary_rpc_method_handler(
            servicer.SendContainer,
            request_deserializer=service__pb2.ContainerRequest.FromString,
            response_serializer=service__pb2.ContainerReply.SerializeToString,
        ),
        "SendKubernetes": grpc.unary_unary_rpc_method_handler(
            servicer.SendKubernetes,
            request_deserializer=service__pb2.KubernetesRequest.FromString,
            response_serializer=service__pb2.KubernetesReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "service.ServiceProto", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ServiceProto(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendBare(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/service.ServiceProto/SendBare",
            service__pb2.BareRequest.SerializeToString,
            service__pb2.BareReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SendContainer(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/service.ServiceProto/SendContainer",
            service__pb2.ContainerRequest.SerializeToString,
            service__pb2.ContainerReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SendKubernetes(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/service.ServiceProto/SendKubernetes",
            service__pb2.KubernetesRequest.SerializeToString,
            service__pb2.KubernetesReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
