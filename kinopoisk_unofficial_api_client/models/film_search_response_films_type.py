from enum import Enum


class FilmSearchResponseFilmsType(str, Enum):
    FILM = "FILM"
    TV_SHOW = "TV_SHOW"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
