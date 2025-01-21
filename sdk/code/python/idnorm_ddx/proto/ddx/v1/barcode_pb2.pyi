from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Pdf417Barcode(_message.Message):
    __slots__ = ("jurisdiction_specified_vehicle_class", "jurisdiction_specified_restriction_codes", "jurisdiction_specified_endorsement_codes", "document_expiration_date", "customer_family_name", "customer_first_name", "customer_middle_names", "document_issue_date", "date_of_birth", "gender", "eye_color", "height", "address_street1", "address_city", "jurisdiction_code", "postal_code", "customer_id", "document_discriminator", "country_identification", "family_name_truncation", "first_name_truncation", "middle_name_truncation", "optional_fields")
    class OptionalFieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPTIONAL_FIELD_TYPE_ADDRESS_STREET_2: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_HAIR_COLOR: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_PLACE_OF_BIRTH: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_AUDIT_INFORMATION: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_INVENTORY_CONTROL_NUMBER: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_ALIAS_FAMILY_NAME: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_ALIAS_GIVEN_NAME: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_ALIAS_SUFFIX_NAME: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_NAME_SUFFIX: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_PHYSICAL_DESCRIPTION_WEIGHT_RANGE: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_RACE_ETHNICITY: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_STANDARD_VEHICLE_CLASSIFICATION: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_STANDARD_ENDORSEMENT_CODE: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_STANDARD_RESTRICTION_CODE: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_JURISDICTION_SPECIFIC_VEHICLE_CLASSIFICATION_DESCRIPTION: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_JURISDICTION_SPECIFIC_ENDORSEMENT_CODE_DESCRIPTION: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_JURISDICTION_SPECIFIC_RESTRICTION_CODE_DESCRIPTION: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_COMPLIANCE_TYPE: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_CARD_REVISION_DATE: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_HAZMAT_ENDORSEMENT_EXPIRATION_DATE: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_LIMITED_DURATION_DOCUMENT_INDICATOR: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_WEIGHT_POUNDS: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_WEIGHT_KILOGRAMS: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_UNDER_18_UNTIL_DATE: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_UNDER_19_UNTIL_DATE: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_UNDER_21_UNTIL_DATE: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_ORGAN_DONOR_INDICATOR: _ClassVar[Pdf417Barcode.OptionalFieldType]
        OPTIONAL_FIELD_TYPE_VETERAN_INDICATOR: _ClassVar[Pdf417Barcode.OptionalFieldType]
    OPTIONAL_FIELD_TYPE_ADDRESS_STREET_2: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_HAIR_COLOR: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_PLACE_OF_BIRTH: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_AUDIT_INFORMATION: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_INVENTORY_CONTROL_NUMBER: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_ALIAS_FAMILY_NAME: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_ALIAS_GIVEN_NAME: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_ALIAS_SUFFIX_NAME: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_NAME_SUFFIX: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_PHYSICAL_DESCRIPTION_WEIGHT_RANGE: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_RACE_ETHNICITY: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_STANDARD_VEHICLE_CLASSIFICATION: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_STANDARD_ENDORSEMENT_CODE: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_STANDARD_RESTRICTION_CODE: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_JURISDICTION_SPECIFIC_VEHICLE_CLASSIFICATION_DESCRIPTION: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_JURISDICTION_SPECIFIC_ENDORSEMENT_CODE_DESCRIPTION: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_JURISDICTION_SPECIFIC_RESTRICTION_CODE_DESCRIPTION: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_COMPLIANCE_TYPE: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_CARD_REVISION_DATE: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_HAZMAT_ENDORSEMENT_EXPIRATION_DATE: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_LIMITED_DURATION_DOCUMENT_INDICATOR: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_WEIGHT_POUNDS: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_WEIGHT_KILOGRAMS: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_UNDER_18_UNTIL_DATE: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_UNDER_19_UNTIL_DATE: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_UNDER_21_UNTIL_DATE: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_ORGAN_DONOR_INDICATOR: Pdf417Barcode.OptionalFieldType
    OPTIONAL_FIELD_TYPE_VETERAN_INDICATOR: Pdf417Barcode.OptionalFieldType
    class OptionalField(_message.Message):
        __slots__ = ("type", "value")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        type: Pdf417Barcode.OptionalFieldType
        value: str
        def __init__(self, type: _Optional[_Union[Pdf417Barcode.OptionalFieldType, str]] = ..., value: _Optional[str] = ...) -> None: ...
    JURISDICTION_SPECIFIED_VEHICLE_CLASS_FIELD_NUMBER: _ClassVar[int]
    JURISDICTION_SPECIFIED_RESTRICTION_CODES_FIELD_NUMBER: _ClassVar[int]
    JURISDICTION_SPECIFIED_ENDORSEMENT_CODES_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MIDDLE_NAMES_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_ISSUE_DATE_FIELD_NUMBER: _ClassVar[int]
    DATE_OF_BIRTH_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    EYE_COLOR_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_STREET1_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_CITY_FIELD_NUMBER: _ClassVar[int]
    JURISDICTION_CODE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
    FAMILY_NAME_TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELDS_FIELD_NUMBER: _ClassVar[int]
    jurisdiction_specified_vehicle_class: str
    jurisdiction_specified_restriction_codes: str
    jurisdiction_specified_endorsement_codes: str
    document_expiration_date: str
    customer_family_name: str
    customer_first_name: str
    customer_middle_names: str
    document_issue_date: str
    date_of_birth: str
    gender: int
    eye_color: str
    height: str
    address_street1: str
    address_city: str
    jurisdiction_code: str
    postal_code: str
    customer_id: str
    document_discriminator: str
    country_identification: str
    family_name_truncation: str
    first_name_truncation: str
    middle_name_truncation: str
    optional_fields: _containers.RepeatedCompositeFieldContainer[Pdf417Barcode.OptionalField]
    def __init__(self, jurisdiction_specified_vehicle_class: _Optional[str] = ..., jurisdiction_specified_restriction_codes: _Optional[str] = ..., jurisdiction_specified_endorsement_codes: _Optional[str] = ..., document_expiration_date: _Optional[str] = ..., customer_family_name: _Optional[str] = ..., customer_first_name: _Optional[str] = ..., customer_middle_names: _Optional[str] = ..., document_issue_date: _Optional[str] = ..., date_of_birth: _Optional[str] = ..., gender: _Optional[int] = ..., eye_color: _Optional[str] = ..., height: _Optional[str] = ..., address_street1: _Optional[str] = ..., address_city: _Optional[str] = ..., jurisdiction_code: _Optional[str] = ..., postal_code: _Optional[str] = ..., customer_id: _Optional[str] = ..., document_discriminator: _Optional[str] = ..., country_identification: _Optional[str] = ..., family_name_truncation: _Optional[str] = ..., first_name_truncation: _Optional[str] = ..., middle_name_truncation: _Optional[str] = ..., optional_fields: _Optional[_Iterable[_Union[Pdf417Barcode.OptionalField, _Mapping]]] = ...) -> None: ...
