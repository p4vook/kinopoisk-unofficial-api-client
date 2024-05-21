from enum import Enum


class DistributionTypeType1(str, Enum):
    ALL = "ALL"
    COUNTRY_SPECIFIC = "COUNTRY_SPECIFIC"
    LOCAL = "LOCAL"
    PREMIERE = "PREMIERE"
    WORLD_PREMIER = "WORLD_PREMIER"

    def __str__(self) -> str:
        return str(self.value)
