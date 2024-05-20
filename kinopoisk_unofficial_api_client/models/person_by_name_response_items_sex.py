from enum import Enum


class PersonByNameResponseItemsSex(str, Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
