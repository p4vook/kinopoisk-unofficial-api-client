from enum import Enum


class FactType(str, Enum):
    BLOOPER = "BLOOPER"
    FACT = "FACT"

    def __str__(self) -> str:
        return str(self.value)
