from enum import Enum


class GetApiV22FilmsOrder(str, Enum):
    NUM_VOTE = "NUM_VOTE"
    RATING = "RATING"
    YEAR = "YEAR"

    def __str__(self) -> str:
        return str(self.value)
