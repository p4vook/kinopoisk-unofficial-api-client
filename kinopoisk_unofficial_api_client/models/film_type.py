from enum import Enum


class FilmType(str, Enum):
    FILM = "FILM"
    MINI_SERIES = "MINI_SERIES"
    TV_SERIES = "TV_SERIES"
    TV_SHOW = "TV_SHOW"
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
