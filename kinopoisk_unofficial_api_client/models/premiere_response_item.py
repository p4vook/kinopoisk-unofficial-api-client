from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.country import Country
    from ..models.genre import Genre


T = TypeVar("T", bound="PremiereResponseItem")


@_attrs_define
class PremiereResponseItem:
    """
    Attributes:
        kinopoisk_id (int):  Example: 301.
        name_ru (Union[None, str]):  Example: Дитя погоды.
        name_en (Union[None, str]):  Example: Tenki no ko.
        year (int):  Example: 2019.
        poster_url (str):  Example: http://kinopoiskapiunofficial.tech/images/posters/kp/1219417.jpg.
        poster_url_preview (str):  Example: https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg.
        countries (List['Country']):
        genres (List['Genre']):
        duration (Union[None, int]):  Example: 112.
        premiere_ru (str):  Example: 2020-06-01.
    """

    kinopoisk_id: int
    name_ru: Union[None, str]
    name_en: Union[None, str]
    year: int
    poster_url: str
    poster_url_preview: str
    countries: List["Country"]
    genres: List["Genre"]
    duration: Union[None, int]
    premiere_ru: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kinopoisk_id = self.kinopoisk_id

        name_ru: Union[None, str]
        name_ru = self.name_ru

        name_en: Union[None, str]
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

        duration: Union[None, int]
        duration = self.duration

        premiere_ru = self.premiere_ru

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kinopoiskId": kinopoisk_id,
                "nameRu": name_ru,
                "nameEn": name_en,
                "year": year,
                "posterUrl": poster_url,
                "posterUrlPreview": poster_url_preview,
                "countries": countries,
                "genres": genres,
                "duration": duration,
                "premiereRu": premiere_ru,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.country import Country
        from ..models.genre import Genre

        d = src_dict.copy()
        kinopoisk_id = d.pop("kinopoiskId")

        def _parse_name_ru(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        name_ru = _parse_name_ru(d.pop("nameRu"))

        def _parse_name_en(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        name_en = _parse_name_en(d.pop("nameEn"))

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

        def _parse_duration(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        duration = _parse_duration(d.pop("duration"))

        premiere_ru = d.pop("premiereRu")

        premiere_response_item = cls(
            kinopoisk_id=kinopoisk_id,
            name_ru=name_ru,
            name_en=name_en,
            year=year,
            poster_url=poster_url,
            poster_url_preview=poster_url_preview,
            countries=countries,
            genres=genres,
            duration=duration,
            premiere_ru=premiere_ru,
        )

        premiere_response_item.additional_properties = d
        return premiere_response_item

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
