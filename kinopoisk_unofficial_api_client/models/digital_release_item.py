from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.country import Country
    from ..models.genre import Genre


T = TypeVar("T", bound="DigitalReleaseItem")


@_attrs_define
class DigitalReleaseItem:
    """
    Attributes:
        film_id (int):  Example: 301.
        name_ru (str):  Example: Дитя погоды.
        name_en (str):  Example: Tenki no ko.
        year (int):  Example: 2019.
        poster_url (str):  Example: http://kinopoiskapiunofficial.tech/images/posters/kp/1219417.jpg.
        poster_url_preview (str):  Example: https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg.
        countries (List['Country']):
        genres (List['Genre']):
        rating (float):  Example: 7.962.
        rating_vote_count (int):  Example: 14502.
        expectations_rating (float):  Example: 99.13.
        expectations_rating_vote_count (int):  Example: 1123.
        duration (int):  Example: 112.
        release_date (str):  Example: 2020-06-01.
    """

    film_id: int
    name_ru: str
    name_en: str
    year: int
    poster_url: str
    poster_url_preview: str
    countries: List["Country"]
    genres: List["Genre"]
    rating: float
    rating_vote_count: int
    expectations_rating: float
    expectations_rating_vote_count: int
    duration: int
    release_date: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        film_id = self.film_id

        name_ru = self.name_ru

        name_en = self.name_en

        year = self.year

        poster_url = self.poster_url

        poster_url_preview = self.poster_url_preview

        countries = []
        for countries_item_data in self.countries:
            countries_item = countries_item_data.to_dict()
            countries.append(countries_item)

        genres = []
        for genres_item_data in self.genres:
            genres_item = genres_item_data.to_dict()
            genres.append(genres_item)

        rating = self.rating

        rating_vote_count = self.rating_vote_count

        expectations_rating = self.expectations_rating

        expectations_rating_vote_count = self.expectations_rating_vote_count

        duration = self.duration

        release_date = self.release_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filmId": film_id,
                "nameRu": name_ru,
                "nameEn": name_en,
                "year": year,
                "posterUrl": poster_url,
                "posterUrlPreview": poster_url_preview,
                "countries": countries,
                "genres": genres,
                "rating": rating,
                "ratingVoteCount": rating_vote_count,
                "expectationsRating": expectations_rating,
                "expectationsRatingVoteCount": expectations_rating_vote_count,
                "duration": duration,
                "releaseDate": release_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.country import Country
        from ..models.genre import Genre

        d = src_dict.copy()
        film_id = d.pop("filmId")

        name_ru = d.pop("nameRu")

        name_en = d.pop("nameEn")

        year = d.pop("year")

        poster_url = d.pop("posterUrl")

        poster_url_preview = d.pop("posterUrlPreview")

        countries = []
        _countries = d.pop("countries")
        for countries_item_data in _countries:
            countries_item = Country.from_dict(countries_item_data)

            countries.append(countries_item)

        genres = []
        _genres = d.pop("genres")
        for genres_item_data in _genres:
            genres_item = Genre.from_dict(genres_item_data)

            genres.append(genres_item)

        rating = d.pop("rating")

        rating_vote_count = d.pop("ratingVoteCount")

        expectations_rating = d.pop("expectationsRating")

        expectations_rating_vote_count = d.pop("expectationsRatingVoteCount")

        duration = d.pop("duration")

        release_date = d.pop("releaseDate")

        digital_release_item = cls(
            film_id=film_id,
            name_ru=name_ru,
            name_en=name_en,
            year=year,
            poster_url=poster_url,
            poster_url_preview=poster_url_preview,
            countries=countries,
            genres=genres,
            rating=rating,
            rating_vote_count=rating_vote_count,
            expectations_rating=expectations_rating,
            expectations_rating_vote_count=expectations_rating_vote_count,
            duration=duration,
            release_date=release_date,
        )

        digital_release_item.additional_properties = d
        return digital_release_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
