from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class connectionData(_message.Message):
    __slots__ = ("number", "uri")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    number: str
    uri: str
    def __init__(self, number: _Optional[str] = ..., uri: _Optional[str] = ...) -> None: ...

class disconnectionData(_message.Message):
    __slots__ = ("hash",)
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class connectionReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: bool
    def __init__(self, message: bool = ...) -> None: ...

class disconnectionReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: bool
    def __init__(self, message: bool = ...) -> None: ...
