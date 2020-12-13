# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import metalmetrics.flow.flow_pb2 as flow__pb2


class FlowProtoStub(object):
    """The service definition."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendFlow = channel.unary_unary(
            "/flow.FlowProto/SendFlow",
            request_serializer=flow__pb2.FlowRequest.SerializeToString,
            response_deserializer=flow__pb2.FlowReply.FromString,
        )


class FlowProtoServicer(object):
    """The service definition."""

    def SendFlow(self, request, context):
        """Sends flow"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_FlowProtoServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SendFlow": grpc.unary_unary_rpc_method_handler(
            servicer.SendFlow,
            request_deserializer=flow__pb2.FlowRequest.FromString,
            response_serializer=flow__pb2.FlowReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flow.FlowProto", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class FlowProto(object):
    """The service definition."""

    @staticmethod
    def SendFlow(
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
            "/flow.FlowProto/SendFlow",
            flow__pb2.FlowRequest.SerializeToString,
            flow__pb2.FlowReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
