from enum import Enum


class GetApiV22FilmsIdReviewsOrder(str, Enum):
    DATE_ASC = "DATE_ASC"
    DATE_DESC = "DATE_DESC"
    USER_NEGATIVE_RATING_ASC = "USER_NEGATIVE_RATING_ASC"
    USER_NEGATIVE_RATING_DESC = "USER_NEGATIVE_RATING_DESC"
    USER_POSITIVE_RATING_ASC = "USER_POSITIVE_RATING_ASC"
    USER_POSITIVE_RATING_DESC = "USER_POSITIVE_RATING_DESC"

    def __str__(self) -> str:
        return str(self.value)
