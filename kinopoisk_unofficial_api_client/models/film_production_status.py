from enum import Enum


class FilmProductionStatus(str, Enum):
    ANNOUNCED = "ANNOUNCED"
    COMPLETED = "COMPLETED"
    FILMING = "FILMING"
    POST_PRODUCTION = "POST_PRODUCTION"
    PRE_PRODUCTION = "PRE_PRODUCTION"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
