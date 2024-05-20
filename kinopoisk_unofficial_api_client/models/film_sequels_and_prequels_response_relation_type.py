from enum import Enum


class FilmSequelsAndPrequelsResponseRelationType(str, Enum):
    PREQUEL = "PREQUEL"
    REMAKE = "REMAKE"
    SEQUEL = "SEQUEL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
