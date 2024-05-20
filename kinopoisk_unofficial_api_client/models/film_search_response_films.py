from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.film_search_response_films_type import FilmSearchResponseFilmsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.country import Country
    from ..models.genre import Genre


T = TypeVar("T", bound="FilmSearchResponseFilms")


@_attrs_define
class FilmSearchResponseFilms:
    """
    Attributes:
        film_id (Union[Unset, int]):  Example: 263531.
        name_ru (Union[Unset, str]):  Example: Мстители.
        name_en (Union[Unset, str]):  Example: The Avengers.
        type (Union[Unset, FilmSearchResponseFilmsType]):  Example: FILM.
        year (Union[Unset, str]):  Example: 2012.
        description (Union[Unset, str]):  Example: США, Джосс Уидон(фантастика).
        film_length (Union[Unset, str]):  Example: 2:17.
        countries (Union[Unset, List['Country']]):
        genres (Union[Unset, List['Genre']]):
        rating (Union[Unset, str]):  Example: NOTE!!! 7.9 for released film or 99% if film have not released yet.
        rating_vote_count (Union[Unset, int]):  Example: 284245.
        poster_url (Union[Unset, str]):  Example: http://kinopoiskapiunofficial.tech/images/posters/kp/263531.jpg.
        poster_url_preview (Union[Unset, str]):  Example:
            https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg.
    """

    film_id: Union[Unset, int] = UNSET
    name_ru: Union[Unset, str] = UNSET
    name_en: Union[Unset, str] = UNSET
    type: Union[Unset, FilmSearchResponseFilmsType] = UNSET
    year: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    film_length: Union[Unset, str] = UNSET
    countries: Union[Unset, List["Country"]] = UNSET
    genres: Union[Unset, List["Genre"]] = UNSET
    rating: Union[Unset, str] = UNSET
    rating_vote_count: Union[Unset, int] = UNSET
    poster_url: Union[Unset, str] = UNSET
    poster_url_preview: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        film_id = self.film_id

        name_ru = self.name_ru

        name_en = self.name_en

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        year = self.year

        description = self.description

        film_length = self.film_length

        countries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.countries, Unset):
            countries = []
            for countries_item_data in self.countries:
                countries_item = countries_item_data.to_dict()
                countries.append(countries_item)

        genres: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.genres, Unset):
            genres = []
            for genres_item_data in self.genres:
                genres_item = genres_item_data.to_dict()
                genres.append(genres_item)

        rating = self.rating

        rating_vote_count = self.rating_vote_count

        poster_url = self.poster_url

        poster_url_preview = self.poster_url_preview

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if film_id is not UNSET:
            field_dict["filmId"] = film_id
        if name_ru is not UNSET:
            field_dict["nameRu"] = name_ru
        if name_en is not UNSET:
            field_dict["nameEn"] = name_en
        if type is not UNSET:
            field_dict["type"] = type
        if year is not UNSET:
            field_dict["year"] = year
        if description is not UNSET:
            field_dict["description"] = description
        if film_length is not UNSET:
            field_dict["filmLength"] = film_length
        if countries is not UNSET:
            field_dict["countries"] = countries
        if genres is not UNSET:
            field_dict["genres"] = genres
        if rating is not UNSET:
            field_dict["rating"] = rating
        if rating_vote_count is not UNSET:
            field_dict["ratingVoteCount"] = rating_vote_count
        if poster_url is not UNSET:
            field_dict["posterUrl"] = poster_url
        if poster_url_preview is not UNSET:
            field_dict["posterUrlPreview"] = poster_url_preview

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.country import Country
        from ..models.genre import Genre

        d = src_dict.copy()
        film_id = d.pop("filmId", UNSET)

        name_ru = d.pop("nameRu", UNSET)

        name_en = d.pop("nameEn", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, FilmSearchResponseFilmsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FilmSearchResponseFilmsType(_type)

        year = d.pop("year", UNSET)

        description = d.pop("description", UNSET)

        film_length = d.pop("filmLength", UNSET)

        countries = []
        _countries = d.pop("countries", UNSET)
        for countries_item_data in _countries or []:
            countries_item = Country.from_dict(countries_item_data)

            countries.append(countries_item)

        genres = []
        _genres = d.pop("genres", UNSET)
        for genres_item_data in _genres or []:
            genres_item = Genre.from_dict(genres_item_data)

            genres.append(genres_item)

        rating = d.pop("rating", UNSET)

        rating_vote_count = d.pop("ratingVoteCount", UNSET)

        poster_url = d.pop("posterUrl", UNSET)

        poster_url_preview = d.pop("posterUrlPreview", UNSET)

        film_search_response_films = cls(
            film_id=film_id,
            name_ru=name_ru,
            name_en=name_en,
            type=type,
            year=year,
            description=description,
            film_length=film_length,
            countries=countries,
            genres=genres,
            rating=rating,
            rating_vote_count=rating_vote_count,
            poster_url=poster_url,
            poster_url_preview=poster_url_preview,
        )

        film_search_response_films.additional_properties = d
        return film_search_response_films

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
