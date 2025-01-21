from idnorm_ddx.google.api import annotations_pb2 as _annotations_pb2
from idnorm_ddx.validate import idnorm_ddx.validate_pb2 as _idnorm_ddx.validate_pb2
from idnorm_ddx.proto.ddx.v1 import countries_enum_pb2 as _countries_enum_pb2
from idnorm_ddx.proto.ddx.v1 import document_types_enum_pb2 as _document_types_enum_pb2
from idnorm_ddx.proto.ddx.v1 import territory_enum_pb2 as _territory_enum_pb2
from idnorm_ddx.proto.ddx.v1 import mrz_pb2 as _mrz_pb2
from idnorm_ddx.proto.ddx.v1 import barcode_pb2 as _barcode_pb2
from idnorm_ddx.proto.ddx.v1 import fields_pb2 as _fields_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DocumentClass(_message.Message):
    __slots__ = ("type", "country", "territory")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_FIELD_NUMBER: _ClassVar[int]
    type: _document_types_enum_pb2.DocumentType
    country: _countries_enum_pb2.Country
    territory: _territory_enum_pb2.Territory
    def __init__(self, type: _Optional[_Union[_document_types_enum_pb2.DocumentType, str]] = ..., country: _Optional[_Union[_countries_enum_pb2.Country, str]] = ..., territory: _Optional[_Union[_territory_enum_pb2.Territory, str]] = ...) -> None: ...

class ScanConfig(_message.Message):
    __slots__ = ("returnDocumentImage", "returnTextFieldImages", "returnVisualFields", "returnDateFieldImages", "returnSexFieldImages", "skipDocumentDetection")
    class ImgResolution(_message.Message):
        __slots__ = ("width", "height")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    class ReturnImage(_message.Message):
        __slots__ = ("targetResolution", "jpegImageQuality")
        TARGETRESOLUTION_FIELD_NUMBER: _ClassVar[int]
        JPEGIMAGEQUALITY_FIELD_NUMBER: _ClassVar[int]
        targetResolution: ScanConfig.ImgResolution
        jpegImageQuality: int
        def __init__(self, targetResolution: _Optional[_Union[ScanConfig.ImgResolution, _Mapping]] = ..., jpegImageQuality: _Optional[int] = ...) -> None: ...
    class ReturnTextFieldImages(_message.Message):
        __slots__ = ("typeFilter", "jpegImageQuality")
        TYPEFILTER_FIELD_NUMBER: _ClassVar[int]
        JPEGIMAGEQUALITY_FIELD_NUMBER: _ClassVar[int]
        typeFilter: _containers.RepeatedScalarFieldContainer[_fields_pb2.TextField.Type]
        jpegImageQuality: int
        def __init__(self, typeFilter: _Optional[_Iterable[_Union[_fields_pb2.TextField.Type, str]]] = ..., jpegImageQuality: _Optional[int] = ...) -> None: ...
    class ReturnDateFieldImages(_message.Message):
        __slots__ = ("typeFilter", "jpegImageQuality")
        TYPEFILTER_FIELD_NUMBER: _ClassVar[int]
        JPEGIMAGEQUALITY_FIELD_NUMBER: _ClassVar[int]
        typeFilter: _containers.RepeatedScalarFieldContainer[_fields_pb2.DateField.Type]
        jpegImageQuality: int
        def __init__(self, typeFilter: _Optional[_Iterable[_Union[_fields_pb2.DateField.Type, str]]] = ..., jpegImageQuality: _Optional[int] = ...) -> None: ...
    class ReturnVisualFields(_message.Message):
        __slots__ = ("typeFilter", "jpegImageQuality")
        TYPEFILTER_FIELD_NUMBER: _ClassVar[int]
        JPEGIMAGEQUALITY_FIELD_NUMBER: _ClassVar[int]
        typeFilter: _containers.RepeatedScalarFieldContainer[_fields_pb2.VisualField.Type]
        jpegImageQuality: int
        def __init__(self, typeFilter: _Optional[_Iterable[_Union[_fields_pb2.VisualField.Type, str]]] = ..., jpegImageQuality: _Optional[int] = ...) -> None: ...
    class ReturnSexFieldImages(_message.Message):
        __slots__ = ("jpegImageQuality",)
        JPEGIMAGEQUALITY_FIELD_NUMBER: _ClassVar[int]
        jpegImageQuality: int
        def __init__(self, jpegImageQuality: _Optional[int] = ...) -> None: ...
    RETURNDOCUMENTIMAGE_FIELD_NUMBER: _ClassVar[int]
    RETURNTEXTFIELDIMAGES_FIELD_NUMBER: _ClassVar[int]
    RETURNVISUALFIELDS_FIELD_NUMBER: _ClassVar[int]
    RETURNDATEFIELDIMAGES_FIELD_NUMBER: _ClassVar[int]
    RETURNSEXFIELDIMAGES_FIELD_NUMBER: _ClassVar[int]
    SKIPDOCUMENTDETECTION_FIELD_NUMBER: _ClassVar[int]
    returnDocumentImage: ScanConfig.ReturnImage
    returnTextFieldImages: ScanConfig.ReturnTextFieldImages
    returnVisualFields: ScanConfig.ReturnVisualFields
    returnDateFieldImages: ScanConfig.ReturnDateFieldImages
    returnSexFieldImages: ScanConfig.ReturnSexFieldImages
    skipDocumentDetection: bool
    def __init__(self, returnDocumentImage: _Optional[_Union[ScanConfig.ReturnImage, _Mapping]] = ..., returnTextFieldImages: _Optional[_Union[ScanConfig.ReturnTextFieldImages, _Mapping]] = ..., returnVisualFields: _Optional[_Union[ScanConfig.ReturnVisualFields, _Mapping]] = ..., returnDateFieldImages: _Optional[_Union[ScanConfig.ReturnDateFieldImages, _Mapping]] = ..., returnSexFieldImages: _Optional[_Union[ScanConfig.ReturnSexFieldImages, _Mapping]] = ..., skipDocumentDetection: bool = ...) -> None: ...

class ScanDocumentRequest(_message.Message):
    __slots__ = ("imageJpeg", "config")
    IMAGEJPEG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    imageJpeg: bytes
    config: ScanConfig
    def __init__(self, imageJpeg: _Optional[bytes] = ..., config: _Optional[_Union[ScanConfig, _Mapping]] = ...) -> None: ...

class Quad(_message.Message):
    __slots__ = ("x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4")
    X1_FIELD_NUMBER: _ClassVar[int]
    Y1_FIELD_NUMBER: _ClassVar[int]
    X2_FIELD_NUMBER: _ClassVar[int]
    Y2_FIELD_NUMBER: _ClassVar[int]
    X3_FIELD_NUMBER: _ClassVar[int]
    Y3_FIELD_NUMBER: _ClassVar[int]
    X4_FIELD_NUMBER: _ClassVar[int]
    Y4_FIELD_NUMBER: _ClassVar[int]
    x1: float
    y1: float
    x2: float
    y2: float
    x3: float
    y3: float
    x4: float
    y4: float
    def __init__(self, x1: _Optional[float] = ..., y1: _Optional[float] = ..., x2: _Optional[float] = ..., y2: _Optional[float] = ..., x3: _Optional[float] = ..., y3: _Optional[float] = ..., x4: _Optional[float] = ..., y4: _Optional[float] = ...) -> None: ...

class Mrz(_message.Message):
    __slots__ = ("status", "fields", "mrz_code")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_OK: _ClassVar[Mrz.Status]
        STATUS_INVALID_FORMAT: _ClassVar[Mrz.Status]
        STATUS_CHECK_DIGIT_INVALID: _ClassVar[Mrz.Status]
    STATUS_OK: Mrz.Status
    STATUS_INVALID_FORMAT: Mrz.Status
    STATUS_CHECK_DIGIT_INVALID: Mrz.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    MRZ_CODE_FIELD_NUMBER: _ClassVar[int]
    status: Mrz.Status
    fields: _mrz_pb2.MrzFields
    mrz_code: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, status: _Optional[_Union[Mrz.Status, str]] = ..., fields: _Optional[_Union[_mrz_pb2.MrzFields, _Mapping]] = ..., mrz_code: _Optional[_Iterable[str]] = ...) -> None: ...

class ScanDocumentResponse(_message.Message):
    __slots__ = ("status", "detection", "classification", "data", "documentImage")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_OK: _ClassVar[ScanDocumentResponse.Status]
        STATUS_DOCUMENT_NOT_FOUND: _ClassVar[ScanDocumentResponse.Status]
        STATUS_DOCUMENT_NOT_SUPPORTED: _ClassVar[ScanDocumentResponse.Status]
        STATUS_DOCUMENT_BACK_SIDE: _ClassVar[ScanDocumentResponse.Status]
    STATUS_OK: ScanDocumentResponse.Status
    STATUS_DOCUMENT_NOT_FOUND: ScanDocumentResponse.Status
    STATUS_DOCUMENT_NOT_SUPPORTED: ScanDocumentResponse.Status
    STATUS_DOCUMENT_BACK_SIDE: ScanDocumentResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETECTION_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTIMAGE_FIELD_NUMBER: _ClassVar[int]
    status: ScanDocumentResponse.Status
    detection: Quad
    classification: DocumentClass
    data: DocumentData
    documentImage: bytes
    def __init__(self, status: _Optional[_Union[ScanDocumentResponse.Status, str]] = ..., detection: _Optional[_Union[Quad, _Mapping]] = ..., classification: _Optional[_Union[DocumentClass, _Mapping]] = ..., data: _Optional[_Union[DocumentData, _Mapping]] = ..., documentImage: _Optional[bytes] = ...) -> None: ...

class DocumentData(_message.Message):
    __slots__ = ("textField", "visualField", "dateField", "sexField", "mrz", "pdf417Barcode")
    TEXTFIELD_FIELD_NUMBER: _ClassVar[int]
    VISUALFIELD_FIELD_NUMBER: _ClassVar[int]
    DATEFIELD_FIELD_NUMBER: _ClassVar[int]
    SEXFIELD_FIELD_NUMBER: _ClassVar[int]
    MRZ_FIELD_NUMBER: _ClassVar[int]
    PDF417BARCODE_FIELD_NUMBER: _ClassVar[int]
    textField: _containers.RepeatedCompositeFieldContainer[_fields_pb2.TextField]
    visualField: _containers.RepeatedCompositeFieldContainer[_fields_pb2.VisualField]
    dateField: _containers.RepeatedCompositeFieldContainer[_fields_pb2.DateField]
    sexField: _containers.RepeatedCompositeFieldContainer[_fields_pb2.SexField]
    mrz: Mrz
    pdf417Barcode: _barcode_pb2.Pdf417Barcode
    def __init__(self, textField: _Optional[_Iterable[_Union[_fields_pb2.TextField, _Mapping]]] = ..., visualField: _Optional[_Iterable[_Union[_fields_pb2.VisualField, _Mapping]]] = ..., dateField: _Optional[_Iterable[_Union[_fields_pb2.DateField, _Mapping]]] = ..., sexField: _Optional[_Iterable[_Union[_fields_pb2.SexField, _Mapping]]] = ..., mrz: _Optional[_Union[Mrz, _Mapping]] = ..., pdf417Barcode: _Optional[_Union[_barcode_pb2.Pdf417Barcode, _Mapping]] = ...) -> None: ...

class ScanTwoSidedDocumentRequest(_message.Message):
    __slots__ = ("firstImage", "secondImage", "config")
    FIRSTIMAGE_FIELD_NUMBER: _ClassVar[int]
    SECONDIMAGE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    firstImage: bytes
    secondImage: bytes
    config: ScanConfig
    def __init__(self, firstImage: _Optional[bytes] = ..., secondImage: _Optional[bytes] = ..., config: _Optional[_Union[ScanConfig, _Mapping]] = ...) -> None: ...

class ScanTwoSidedDocumentResponse(_message.Message):
    __slots__ = ("status", "classification", "data", "frontSideDocumentImage", "backSideDocumentImage")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_OK: _ClassVar[ScanTwoSidedDocumentResponse.Status]
        STATUS_FRONT_SIDE_NOT_FOUND: _ClassVar[ScanTwoSidedDocumentResponse.Status]
        STATUS_BACK_SIDE_NOT_FOUND: _ClassVar[ScanTwoSidedDocumentResponse.Status]
        STATUS_NOT_SUPPORTED: _ClassVar[ScanTwoSidedDocumentResponse.Status]
    STATUS_OK: ScanTwoSidedDocumentResponse.Status
    STATUS_FRONT_SIDE_NOT_FOUND: ScanTwoSidedDocumentResponse.Status
    STATUS_BACK_SIDE_NOT_FOUND: ScanTwoSidedDocumentResponse.Status
    STATUS_NOT_SUPPORTED: ScanTwoSidedDocumentResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FRONTSIDEDOCUMENTIMAGE_FIELD_NUMBER: _ClassVar[int]
    BACKSIDEDOCUMENTIMAGE_FIELD_NUMBER: _ClassVar[int]
    status: ScanTwoSidedDocumentResponse.Status
    classification: DocumentClass
    data: DocumentData
    frontSideDocumentImage: bytes
    backSideDocumentImage: bytes
    def __init__(self, status: _Optional[_Union[ScanTwoSidedDocumentResponse.Status, str]] = ..., classification: _Optional[_Union[DocumentClass, _Mapping]] = ..., data: _Optional[_Union[DocumentData, _Mapping]] = ..., frontSideDocumentImage: _Optional[bytes] = ..., backSideDocumentImage: _Optional[bytes] = ...) -> None: ...
