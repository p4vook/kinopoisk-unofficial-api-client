from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kinopoisk_user_vote_response_items_type import KinopoiskUserVoteResponseItemsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.country import Country
    from ..models.genre import Genre


T = TypeVar("T", bound="KinopoiskUserVoteResponseItems")


@_attrs_define
class KinopoiskUserVoteResponseItems:
    """
    Attributes:
        kinopoisk_id (Union[Unset, int]):  Example: 263531.
        name_ru (Union[None, Unset, str]):  Example: Мстители.
        name_en (Union[None, Unset, str]):  Example: The Avengers.
        name_original (Union[None, Unset, str]):  Example: The Avengers.
        countries (Union[Unset, List['Country']]):
        genres (Union[Unset, List['Genre']]):
        rating_kinopoisk (Union[None, Unset, float]):  Example: 7.9.
        rating_imbd (Union[None, Unset, float]):  Example: 7.9.
        year (Union[None, Unset, str]):  Example: 2012.
        type (Union[Unset, KinopoiskUserVoteResponseItemsType]):  Example: FILM.
        poster_url (Union[Unset, str]):  Example: http://kinopoiskapiunofficial.tech/images/posters/kp/263531.jpg.
        poster_url_preview (Union[Unset, str]):  Example:
            https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg.
        user_rating (Union[Unset, int]):  Example: 7.
    """

    kinopoisk_id: Union[Unset, int] = UNSET
    name_ru: Union[None, Unset, str] = UNSET
    name_en: Union[None, Unset, str] = UNSET
    name_original: Union[None, Unset, str] = UNSET
    countries: Union[Unset, List["Country"]] = UNSET
    genres: Union[Unset, List["Genre"]] = UNSET
    rating_kinopoisk: Union[None, Unset, float] = UNSET
    rating_imbd: Union[None, Unset, float] = UNSET
    year: Union[None, Unset, str] = UNSET
    type: Union[Unset, KinopoiskUserVoteResponseItemsType] = UNSET
    poster_url: Union[Unset, str] = UNSET
    poster_url_preview: Union[Unset, str] = UNSET
    user_rating: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kinopoisk_id = self.kinopoisk_id

        name_ru: Union[None, Unset, str]
        if isinstance(self.name_ru, Unset):
            name_ru = UNSET
        else:
            name_ru = self.name_ru

        name_en: Union[None, Unset, str]
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_original: Union[None, Unset, str]
        if isinstance(self.name_original, Unset):
            name_original = UNSET
        else:
            name_original = self.name_original

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

        rating_kinopoisk: Union[None, Unset, float]
        if isinstance(self.rating_kinopoisk, Unset):
            rating_kinopoisk = UNSET
        else:
            rating_kinopoisk = self.rating_kinopoisk

        rating_imbd: Union[None, Unset, float]
        if isinstance(self.rating_imbd, Unset):
            rating_imbd = UNSET
        else:
            rating_imbd = self.rating_imbd

        year: Union[None, Unset, str]
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        poster_url = self.poster_url

        poster_url_preview = self.poster_url_preview

        user_rating = self.user_rating

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kinopoisk_id is not UNSET:
            field_dict["kinopoiskId"] = kinopoisk_id
        if name_ru is not UNSET:
            field_dict["nameRu"] = name_ru
        if name_en is not UNSET:
            field_dict["nameEn"] = name_en
        if name_original is not UNSET:
            field_dict["nameOriginal"] = name_original
        if countries is not UNSET:
            field_dict["countries"] = countries
        if genres is not UNSET:
            field_dict["genres"] = genres
        if rating_kinopoisk is not UNSET:
            field_dict["ratingKinopoisk"] = rating_kinopoisk
        if rating_imbd is not UNSET:
            field_dict["ratingImbd"] = rating_imbd
        if year is not UNSET:
            field_dict["year"] = year
        if type is not UNSET:
            field_dict["type"] = type
        if poster_url is not UNSET:
            field_dict["posterUrl"] = poster_url
        if poster_url_preview is not UNSET:
            field_dict["posterUrlPreview"] = poster_url_preview
        if user_rating is not UNSET:
            field_dict["userRating"] = user_rating

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.country import Country
        from ..models.genre import Genre

        d = src_dict.copy()
        kinopoisk_id = d.pop("kinopoiskId", UNSET)

        def _parse_name_ru(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_ru = _parse_name_ru(d.pop("nameRu", UNSET))

        def _parse_name_en(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_en = _parse_name_en(d.pop("nameEn", UNSET))

        def _parse_name_original(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_original = _parse_name_original(d.pop("nameOriginal", UNSET))

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

        def _parse_rating_kinopoisk(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        rating_kinopoisk = _parse_rating_kinopoisk(d.pop("ratingKinopoisk", UNSET))

        def _parse_rating_imbd(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        rating_imbd = _parse_rating_imbd(d.pop("ratingImbd", UNSET))

        def _parse_year(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        year = _parse_year(d.pop("year", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, KinopoiskUserVoteResponseItemsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = KinopoiskUserVoteResponseItemsType(_type)

        poster_url = d.pop("posterUrl", UNSET)

        poster_url_preview = d.pop("posterUrlPreview", UNSET)

        user_rating = d.pop("userRating", UNSET)

        kinopoisk_user_vote_response_items = cls(
            kinopoisk_id=kinopoisk_id,
            name_ru=name_ru,
            name_en=name_en,
            name_original=name_original,
            countries=countries,
            genres=genres,
            rating_kinopoisk=rating_kinopoisk,
            rating_imbd=rating_imbd,
            year=year,
            type=type,
            poster_url=poster_url,
            poster_url_preview=poster_url_preview,
            user_rating=user_rating,
        )

        kinopoisk_user_vote_response_items.additional_properties = d
        return kinopoisk_user_vote_response_items

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
