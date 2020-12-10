# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="service.proto",
    package="service",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\rservice.proto\x12\x07service"\x1b\n\x0b\x42\x61reRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\x1c\n\tBareReply\x12\x0f\n\x07message\x18\x01 \x01(\t" \n\x10\x43ontainerRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"!\n\x0e\x43ontainerReply\x12\x0f\n\x07message\x18\x01 \x01(\t"!\n\x11KubernetesRequest\x12\x0c\n\x04name\x18\x01 \x01(\t""\n\x0fKubernetesReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xd7\x01\n\x0cServiceProto\x12\x36\n\x08SendBare\x12\x14.service.BareRequest\x1a\x12.service.BareReply"\x00\x12\x45\n\rSendContainer\x12\x19.service.ContainerRequest\x1a\x17.service.ContainerReply"\x00\x12H\n\x0eSendKubernetes\x12\x1a.service.KubernetesRequest\x1a\x18.service.KubernetesReply"\x00\x62\x06proto3',
)


_BAREREQUEST = _descriptor.Descriptor(
    name="BareRequest",
    full_name="service.BareRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="service.BareRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=26,
    serialized_end=53,
)


_BAREREPLY = _descriptor.Descriptor(
    name="BareReply",
    full_name="service.BareReply",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="message",
            full_name="service.BareReply.message",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=55,
    serialized_end=83,
)


_CONTAINERREQUEST = _descriptor.Descriptor(
    name="ContainerRequest",
    full_name="service.ContainerRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="service.ContainerRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=85,
    serialized_end=117,
)


_CONTAINERREPLY = _descriptor.Descriptor(
    name="ContainerReply",
    full_name="service.ContainerReply",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="message",
            full_name="service.ContainerReply.message",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=119,
    serialized_end=152,
)


_KUBERNETESREQUEST = _descriptor.Descriptor(
    name="KubernetesRequest",
    full_name="service.KubernetesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="service.KubernetesRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=154,
    serialized_end=187,
)


_KUBERNETESREPLY = _descriptor.Descriptor(
    name="KubernetesReply",
    full_name="service.KubernetesReply",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="message",
            full_name="service.KubernetesReply.message",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=189,
    serialized_end=223,
)

DESCRIPTOR.message_types_by_name["BareRequest"] = _BAREREQUEST
DESCRIPTOR.message_types_by_name["BareReply"] = _BAREREPLY
DESCRIPTOR.message_types_by_name["ContainerRequest"] = _CONTAINERREQUEST
DESCRIPTOR.message_types_by_name["ContainerReply"] = _CONTAINERREPLY
DESCRIPTOR.message_types_by_name["KubernetesRequest"] = _KUBERNETESREQUEST
DESCRIPTOR.message_types_by_name["KubernetesReply"] = _KUBERNETESREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BareRequest = _reflection.GeneratedProtocolMessageType(
    "BareRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _BAREREQUEST,
        "__module__": "service_pb2"
        # @@protoc_insertion_point(class_scope:service.BareRequest)
    },
)
_sym_db.RegisterMessage(BareRequest)

BareReply = _reflection.GeneratedProtocolMessageType(
    "BareReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _BAREREPLY,
        "__module__": "service_pb2"
        # @@protoc_insertion_point(class_scope:service.BareReply)
    },
)
_sym_db.RegisterMessage(BareReply)

ContainerRequest = _reflection.GeneratedProtocolMessageType(
    "ContainerRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONTAINERREQUEST,
        "__module__": "service_pb2"
        # @@protoc_insertion_point(class_scope:service.ContainerRequest)
    },
)
_sym_db.RegisterMessage(ContainerRequest)

ContainerReply = _reflection.GeneratedProtocolMessageType(
    "ContainerReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONTAINERREPLY,
        "__module__": "service_pb2"
        # @@protoc_insertion_point(class_scope:service.ContainerReply)
    },
)
_sym_db.RegisterMessage(ContainerReply)

KubernetesRequest = _reflection.GeneratedProtocolMessageType(
    "KubernetesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _KUBERNETESREQUEST,
        "__module__": "service_pb2"
        # @@protoc_insertion_point(class_scope:service.KubernetesRequest)
    },
)
_sym_db.RegisterMessage(KubernetesRequest)

KubernetesReply = _reflection.GeneratedProtocolMessageType(
    "KubernetesReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _KUBERNETESREPLY,
        "__module__": "service_pb2"
        # @@protoc_insertion_point(class_scope:service.KubernetesReply)
    },
)
_sym_db.RegisterMessage(KubernetesReply)


_SERVICEPROTO = _descriptor.ServiceDescriptor(
    name="ServiceProto",
    full_name="service.ServiceProto",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=226,
    serialized_end=441,
    methods=[
        _descriptor.MethodDescriptor(
            name="SendBare",
            full_name="service.ServiceProto.SendBare",
            index=0,
            containing_service=None,
            input_type=_BAREREQUEST,
            output_type=_BAREREPLY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SendContainer",
            full_name="service.ServiceProto.SendContainer",
            index=1,
            containing_service=None,
            input_type=_CONTAINERREQUEST,
            output_type=_CONTAINERREPLY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SendKubernetes",
            full_name="service.ServiceProto.SendKubernetes",
            index=2,
            containing_service=None,
            input_type=_KUBERNETESREQUEST,
            output_type=_KUBERNETESREPLY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_SERVICEPROTO)

DESCRIPTOR.services_by_name["ServiceProto"] = _SERVICEPROTO

# @@protoc_insertion_point(module_scope)