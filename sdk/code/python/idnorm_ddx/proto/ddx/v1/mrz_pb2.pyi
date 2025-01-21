from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MrzFields(_message.Message):
    __slots__ = ("document_type", "country_code", "document_number", "birthdate", "sex", "expiry_date", "nationality", "final_check_digit", "name", "surname", "given_name", "optional_data1", "optional_data2", "is_visa")
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BIRTHDATE_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_DATE_FIELD_NUMBER: _ClassVar[int]
    NATIONALITY_FIELD_NUMBER: _ClassVar[int]
    FINAL_CHECK_DIGIT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SURNAME_FIELD_NUMBER: _ClassVar[int]
    GIVEN_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_DATA1_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_DATA2_FIELD_NUMBER: _ClassVar[int]
    IS_VISA_FIELD_NUMBER: _ClassVar[int]
    document_type: str
    country_code: str
    document_number: str
    birthdate: str
    sex: str
    expiry_date: str
    nationality: str
    final_check_digit: str
    name: str
    surname: str
    given_name: str
    optional_data1: str
    optional_data2: str
    is_visa: bool
    def __init__(self, document_type: _Optional[str] = ..., country_code: _Optional[str] = ..., document_number: _Optional[str] = ..., birthdate: _Optional[str] = ..., sex: _Optional[str] = ..., expiry_date: _Optional[str] = ..., nationality: _Optional[str] = ..., final_check_digit: _Optional[str] = ..., name: _Optional[str] = ..., surname: _Optional[str] = ..., given_name: _Optional[str] = ..., optional_data1: _Optional[str] = ..., optional_data2: _Optional[str] = ..., is_visa: bool = ...) -> None: ...
