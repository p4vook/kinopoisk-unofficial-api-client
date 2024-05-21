from enum import Enum


class PersonResponseSexType2Type1(str, Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"

    def __str__(self) -> str:
        return str(self.value)
