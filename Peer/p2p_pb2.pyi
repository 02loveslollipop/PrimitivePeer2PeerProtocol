from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class fileRequest(_message.Message):
    __slots__ = ("file_path",)
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    def __init__(self, file_path: _Optional[str] = ...) -> None: ...

class fileBytes(_message.Message):
    __slots__ = ("file_bytes",)
    FILE_BYTES_FIELD_NUMBER: _ClassVar[int]
    file_bytes: bytes
    def __init__(self, file_bytes: _Optional[bytes] = ...) -> None: ...
