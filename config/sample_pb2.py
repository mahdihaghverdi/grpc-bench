# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name="sample.proto",
    package="github",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0csample.proto\x12\x06github"0\n\x11RepositoryRequest\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t"7\n\x12RepositoryResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t2Y\n\rGitHubService\x12H\n\rGetRepository\x12\x19.github.RepositoryRequest\x1a\x1a.github.RepositoryResponse"\x00\x62\x06proto3',
)

_REPOSITORYREQUEST = _descriptor.Descriptor(
    name="RepositoryRequest",
    full_name="github.RepositoryRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="owner",
            full_name="github.RepositoryRequest.owner",
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
        _descriptor.FieldDescriptor(
            name="name",
            full_name="github.RepositoryRequest.name",
            index=1,
            number=2,
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
    serialized_start=24,
    serialized_end=72,
)

_REPOSITORYRESPONSE = _descriptor.Descriptor(
    name="RepositoryResponse",
    full_name="github.RepositoryResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="github.RepositoryResponse.name",
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
        _descriptor.FieldDescriptor(
            name="description",
            full_name="github.RepositoryResponse.description",
            index=1,
            number=2,
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
    serialized_start=74,
    serialized_end=129,
)

DESCRIPTOR.message_types_by_name["RepositoryRequest"] = _REPOSITORYREQUEST
DESCRIPTOR.message_types_by_name["RepositoryResponse"] = _REPOSITORYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RepositoryRequest = _reflection.GeneratedProtocolMessageType(
    "RepositoryRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _REPOSITORYREQUEST,
        "__module__": "sample_pb2"
        # @@protoc_insertion_point(class_scope:github.RepositoryRequest)
    },
)
_sym_db.RegisterMessage(RepositoryRequest)

RepositoryResponse = _reflection.GeneratedProtocolMessageType(
    "RepositoryResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _REPOSITORYRESPONSE,
        "__module__": "sample_pb2"
        # @@protoc_insertion_point(class_scope:github.RepositoryResponse)
    },
)
_sym_db.RegisterMessage(RepositoryResponse)

_GITHUBSERVICE = _descriptor.ServiceDescriptor(
    name="GitHubService",
    full_name="github.GitHubService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=131,
    serialized_end=220,
    methods=[
        _descriptor.MethodDescriptor(
            name="GetRepository",
            full_name="github.GitHubService.GetRepository",
            index=0,
            containing_service=None,
            input_type=_REPOSITORYREQUEST,
            output_type=_REPOSITORYRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_GITHUBSERVICE)

DESCRIPTOR.services_by_name["GitHubService"] = _GITHUBSERVICE

# @@protoc_insertion_point(module_scope)
