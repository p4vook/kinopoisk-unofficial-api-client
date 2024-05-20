from enum import Enum


class ApiKeyResponseAccountType(str, Enum):
    EXTENDED = "EXTENDED"
    FREE = "FREE"
    UNLIMITED = "UNLIMITED"

    def __str__(self) -> str:
        return str(self.value)
