from enum import Enum


class PersonResponseSexType1(str, Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"

    def __str__(self) -> str:
        return str(self.value)
