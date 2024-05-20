from enum import Enum


class StaffResponseProfessionKey(str, Enum):
    ACTOR = "ACTOR"
    COMPOSER = "COMPOSER"
    DESIGN = "DESIGN"
    DIRECTOR = "DIRECTOR"
    EDITOR = "EDITOR"
    OPERATOR = "OPERATOR"
    PRODUCER = "PRODUCER"
    PRODUCER_USSR = "PRODUCER_USSR"
    TRANSLATOR = "TRANSLATOR"
    UNKNOWN = "UNKNOWN"
    VOICE_DIRECTOR = "VOICE_DIRECTOR"
    WRITER = "WRITER"

    def __str__(self) -> str:
        return str(self.value)
