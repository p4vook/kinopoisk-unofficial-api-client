from enum import Enum


class ReviewResponseItemsType(str, Enum):
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"
    POSITIVE = "POSITIVE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
