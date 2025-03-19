from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Alphabet(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALPHABET_LATIN: _ClassVar[Alphabet]
    ALPHABET_CYRILLIC: _ClassVar[Alphabet]
    ALPHABET_ARABIC: _ClassVar[Alphabet]
ALPHABET_LATIN: Alphabet
ALPHABET_CYRILLIC: Alphabet
ALPHABET_ARABIC: Alphabet

class Polygon(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: _containers.RepeatedScalarFieldContainer[float]
    y: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, x: _Optional[_Iterable[float]] = ..., y: _Optional[_Iterable[float]] = ...) -> None: ...

class Box(_message.Message):
    __slots__ = ("x", "y", "width", "height")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    width: float
    height: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ("detection_on_input_image", "position_on_detected_document")
    DETECTION_ON_INPUT_IMAGE_FIELD_NUMBER: _ClassVar[int]
    POSITION_ON_DETECTED_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    detection_on_input_image: Polygon
    position_on_detected_document: Box
    def __init__(self, detection_on_input_image: _Optional[_Union[Polygon, _Mapping]] = ..., position_on_detected_document: _Optional[_Union[Box, _Mapping]] = ...) -> None: ...

class TextField(_message.Message):
    __slots__ = ("type", "value", "alphabet", "image", "location")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_FIRST_NAME: _ClassVar[TextField.Type]
        TYPE_LAST_NAME: _ClassVar[TextField.Type]
        TYPE_NATIONALITY: _ClassVar[TextField.Type]
        TYPE_DOCUMENT_IDENTITY_NUMBER: _ClassVar[TextField.Type]
        TYPE_ISSUING_AUTHORITY: _ClassVar[TextField.Type]
        TYPE_ADDRESS: _ClassVar[TextField.Type]
        TYPE_PERSONAL_IDENTITY_NUMBER: _ClassVar[TextField.Type]
        TYPE_MARITAL_STATUS: _ClassVar[TextField.Type]
        TYPE_EXTENDED_ADDRESS: _ClassVar[TextField.Type]
        TYPE_EXTENDED_ADDRESS_SPECIFICS: _ClassVar[TextField.Type]
        TYPE_CLASS: _ClassVar[TextField.Type]
        TYPE_CONDITIONS: _ClassVar[TextField.Type]
        TYPE_ENDORSEMENTS: _ClassVar[TextField.Type]
        TYPE_DRIVERS_LICENSE_TYPE: _ClassVar[TextField.Type]
        TYPE_FULL_NAME: _ClassVar[TextField.Type]
        TYPE_PLACE_OF_BIRTH: _ClassVar[TextField.Type]
        TYPE_PROFESSION: _ClassVar[TextField.Type]
        TYPE_EMPLOYER: _ClassVar[TextField.Type]
        TYPE_EXTENDED_NAME: _ClassVar[TextField.Type]
        TYPE_FATHERS_NAME: _ClassVar[TextField.Type]
        TYPE_MOTHERS_NAME: _ClassVar[TextField.Type]
        TYPE_RACE: _ClassVar[TextField.Type]
        TYPE_RESIDENTIAL_TYPE: _ClassVar[TextField.Type]
        TYPE_RESTRICTIONS: _ClassVar[TextField.Type]
        TYPE_BLOOD_TYPE: _ClassVar[TextField.Type]
        TYPE_NUMBER: _ClassVar[TextField.Type]
    TYPE_FIRST_NAME: TextField.Type
    TYPE_LAST_NAME: TextField.Type
    TYPE_NATIONALITY: TextField.Type
    TYPE_DOCUMENT_IDENTITY_NUMBER: TextField.Type
    TYPE_ISSUING_AUTHORITY: TextField.Type
    TYPE_ADDRESS: TextField.Type
    TYPE_PERSONAL_IDENTITY_NUMBER: TextField.Type
    TYPE_MARITAL_STATUS: TextField.Type
    TYPE_EXTENDED_ADDRESS: TextField.Type
    TYPE_EXTENDED_ADDRESS_SPECIFICS: TextField.Type
    TYPE_CLASS: TextField.Type
    TYPE_CONDITIONS: TextField.Type
    TYPE_ENDORSEMENTS: TextField.Type
    TYPE_DRIVERS_LICENSE_TYPE: TextField.Type
    TYPE_FULL_NAME: TextField.Type
    TYPE_PLACE_OF_BIRTH: TextField.Type
    TYPE_PROFESSION: TextField.Type
    TYPE_EMPLOYER: TextField.Type
    TYPE_EXTENDED_NAME: TextField.Type
    TYPE_FATHERS_NAME: TextField.Type
    TYPE_MOTHERS_NAME: TextField.Type
    TYPE_RACE: TextField.Type
    TYPE_RESIDENTIAL_TYPE: TextField.Type
    TYPE_RESTRICTIONS: TextField.Type
    TYPE_BLOOD_TYPE: TextField.Type
    TYPE_NUMBER: TextField.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ALPHABET_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    type: TextField.Type
    value: str
    alphabet: Alphabet
    image: bytes
    location: Location
    def __init__(self, type: _Optional[_Union[TextField.Type, str]] = ..., value: _Optional[str] = ..., alphabet: _Optional[_Union[Alphabet, str]] = ..., image: _Optional[bytes] = ..., location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class DateField(_message.Message):
    __slots__ = ("type", "date", "value", "alphabet", "image", "location")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_DATE_OF_BIRTH: _ClassVar[DateField.Type]
        TYPE_ISSUE_DATE: _ClassVar[DateField.Type]
        TYPE_EXPIRY_DATE: _ClassVar[DateField.Type]
        TYPE_CLASS_EFFECTIVE_DATE: _ClassVar[DateField.Type]
        TYPE_CLASS_EXPIRY_DATE: _ClassVar[DateField.Type]
    TYPE_DATE_OF_BIRTH: DateField.Type
    TYPE_ISSUE_DATE: DateField.Type
    TYPE_EXPIRY_DATE: DateField.Type
    TYPE_CLASS_EFFECTIVE_DATE: DateField.Type
    TYPE_CLASS_EXPIRY_DATE: DateField.Type
    class Date(_message.Message):
        __slots__ = ("year", "month", "day")
        YEAR_FIELD_NUMBER: _ClassVar[int]
        MONTH_FIELD_NUMBER: _ClassVar[int]
        DAY_FIELD_NUMBER: _ClassVar[int]
        year: int
        month: int
        day: int
        def __init__(self, year: _Optional[int] = ..., month: _Optional[int] = ..., day: _Optional[int] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ALPHABET_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    type: DateField.Type
    date: DateField.Date
    value: str
    alphabet: Alphabet
    image: bytes
    location: Location
    def __init__(self, type: _Optional[_Union[DateField.Type, str]] = ..., date: _Optional[_Union[DateField.Date, _Mapping]] = ..., value: _Optional[str] = ..., alphabet: _Optional[_Union[Alphabet, str]] = ..., image: _Optional[bytes] = ..., location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class VisualField(_message.Message):
    __slots__ = ("type", "image", "location")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_FACE_PHOTO: _ClassVar[VisualField.Type]
        TYPE_SIGNATURE: _ClassVar[VisualField.Type]
    TYPE_FACE_PHOTO: VisualField.Type
    TYPE_SIGNATURE: VisualField.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    type: VisualField.Type
    image: bytes
    location: Location
    def __init__(self, type: _Optional[_Union[VisualField.Type, str]] = ..., image: _Optional[bytes] = ..., location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class SexField(_message.Message):
    __slots__ = ("sex", "value", "alphabet", "image", "location")
    class Sex(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[SexField.Sex]
        MALE: _ClassVar[SexField.Sex]
        FEMALE: _ClassVar[SexField.Sex]
    UNKNOWN: SexField.Sex
    MALE: SexField.Sex
    FEMALE: SexField.Sex
    SEX_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ALPHABET_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    sex: SexField.Sex
    value: str
    alphabet: Alphabet
    image: bytes
    location: Location
    def __init__(self, sex: _Optional[_Union[SexField.Sex, str]] = ..., value: _Optional[str] = ..., alphabet: _Optional[_Union[Alphabet, str]] = ..., image: _Optional[bytes] = ..., location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...
