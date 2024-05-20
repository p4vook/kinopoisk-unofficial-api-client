from enum import Enum


class VideoResponseItemsSite(str, Enum):
    KINOPOISK_WIDGET = "KINOPOISK_WIDGET"
    UNKNOWN = "UNKNOWN"
    YANDEX_DISK = "YANDEX_DISK"
    YOUTUBE = "YOUTUBE"

    def __str__(self) -> str:
        return str(self.value)
