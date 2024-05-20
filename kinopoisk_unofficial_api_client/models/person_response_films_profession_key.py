from enum import Enum


class PersonResponseFilmsProfessionKey(str, Enum):
    ACTOR = "ACTOR"
    COMPOSER = "COMPOSER"
    DESIGN = "DESIGN"
    DIRECTOR = "DIRECTOR"
    EDITOR = "EDITOR"
    HERSELF = "HERSELF"
    HIMSELF = "HIMSELF"
    HRONO_TITR_FEMALE = "HRONO_TITR_FEMALE"
    HRONO_TITR_MALE = "HRONO_TITR_MALE"
    OPERATOR = "OPERATOR"
    PRODUCER = "PRODUCER"
    PRODUCER_USSR = "PRODUCER_USSR"
    TRANSLATOR = "TRANSLATOR"
    UNKNOWN = "UNKNOWN"
    VOICE_DIRECTOR = "VOICE_DIRECTOR"
    WRITER = "WRITER"

    def __str__(self) -> str:
        return str(self.value)
