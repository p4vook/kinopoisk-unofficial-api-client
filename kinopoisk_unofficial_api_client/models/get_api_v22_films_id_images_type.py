from enum import Enum


class GetApiV22FilmsIdImagesType(str, Enum):
    CONCEPT = "CONCEPT"
    COVER = "COVER"
    FAN_ART = "FAN_ART"
    POSTER = "POSTER"
    PROMO = "PROMO"
    SCREENSHOT = "SCREENSHOT"
    SHOOTING = "SHOOTING"
    STILL = "STILL"
    WALLPAPER = "WALLPAPER"

    def __str__(self) -> str:
        return str(self.value)
