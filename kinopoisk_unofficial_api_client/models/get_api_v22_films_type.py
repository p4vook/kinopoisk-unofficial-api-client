from enum import Enum


class GetApiV22FilmsType(str, Enum):
    ALL = "ALL"
    FILM = "FILM"
    MINI_SERIES = "MINI_SERIES"
    TV_SERIES = "TV_SERIES"
    TV_SHOW = "TV_SHOW"

    def __str__(self) -> str:
        return str(self.value)
