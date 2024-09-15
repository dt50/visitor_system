from enum import Enum, EnumMeta


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return [x.value for x in cls]


class DirectValueMeta(EnumMeta):
    "Metaclass that allows for directly getting an enum attribute"

    def __getattribute__(cls, name):
        value = super().__getattribute__(name)
        if isinstance(value, cls):
            value = value.value
        return value
