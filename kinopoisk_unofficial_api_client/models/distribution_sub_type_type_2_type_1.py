from enum import Enum


class DistributionSubTypeType2Type1(str, Enum):
    BLURAY = "BLURAY"
    CINEMA = "CINEMA"
    DIGITAL = "DIGITAL"
    DVD = "DVD"

    def __str__(self) -> str:
        return str(self.value)
