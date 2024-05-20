from enum import Enum


class GetApiV22FilmsPremieresMonth(str, Enum):
    APRIL = "APRIL"
    AUGUST = "AUGUST"
    DECEMBER = "DECEMBER"
    FEBRUARY = "FEBRUARY"
    JANUARY = "JANUARY"
    JULY = "JULY"
    JUNE = "JUNE"
    MARCH = "MARCH"
    MAY = "MAY"
    NOVEMBER = "NOVEMBER"
    OCTOBER = "OCTOBER"
    SEPTEMBER = "SEPTEMBER"

    def __str__(self) -> str:
        return str(self.value)
