from enum import Enum


class DistributionSubType(str, Enum):
    BLURAY = "BLURAY"
    CINEMA = "CINEMA"
    DIGITAL = "DIGITAL"
    DVD = "DVD"

    def __str__(self) -> str:
        return str(self.value)
