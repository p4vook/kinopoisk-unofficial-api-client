from enum import Enum


class PersonByNameResponseItemsSexType1(str, Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
