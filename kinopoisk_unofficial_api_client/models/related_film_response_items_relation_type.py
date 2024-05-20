from enum import Enum


class RelatedFilmResponseItemsRelationType(str, Enum):
    SIMILAR = "SIMILAR"

    def __str__(self) -> str:
        return str(self.value)
