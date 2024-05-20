from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_response_films_profession_key import PersonResponseFilmsProfessionKey
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonResponseFilms")


@_attrs_define
class PersonResponseFilms:
    """
    Attributes:
        film_id (Union[Unset, int]):  Example: 32169.
        name_ru (Union[None, Unset, str]):  Example: Солист.
        name_en (Union[None, Unset, str]):  Example: The Soloist.
        rating (Union[None, Unset, str]):  Example: 7.2 or 76% if film has not released yet.
        general (Union[Unset, bool]):
        description (Union[None, Unset, str]):  Example: Steve Lopez.
        profession_key (Union[Unset, PersonResponseFilmsProfessionKey]):  Example: ACTOR.
    """

    film_id: Union[Unset, int] = UNSET
    name_ru: Union[None, Unset, str] = UNSET
    name_en: Union[None, Unset, str] = UNSET
    rating: Union[None, Unset, str] = UNSET
    general: Union[Unset, bool] = UNSET
    description: Union[None, Unset, str] = UNSET
    profession_key: Union[Unset, PersonResponseFilmsProfessionKey] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        film_id = self.film_id

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

        rating: Union[None, Unset, str]
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        general = self.general

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        profession_key: Union[Unset, str] = UNSET
        if not isinstance(self.profession_key, Unset):
            profession_key = self.profession_key.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if film_id is not UNSET:
            field_dict["filmId"] = film_id
        if name_ru is not UNSET:
            field_dict["nameRu"] = name_ru
        if name_en is not UNSET:
            field_dict["nameEn"] = name_en
        if rating is not UNSET:
            field_dict["rating"] = rating
        if general is not UNSET:
            field_dict["general"] = general
        if description is not UNSET:
            field_dict["description"] = description
        if profession_key is not UNSET:
            field_dict["professionKey"] = profession_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        film_id = d.pop("filmId", UNSET)

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

        def _parse_rating(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rating = _parse_rating(d.pop("rating", UNSET))

        general = d.pop("general", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _profession_key = d.pop("professionKey", UNSET)
        profession_key: Union[Unset, PersonResponseFilmsProfessionKey]
        if isinstance(_profession_key, Unset):
            profession_key = UNSET
        else:
            profession_key = PersonResponseFilmsProfessionKey(_profession_key)

        person_response_films = cls(
            film_id=film_id,
            name_ru=name_ru,
            name_en=name_en,
            rating=rating,
            general=general,
            description=description,
            profession_key=profession_key,
        )

        person_response_films.additional_properties = d
        return person_response_films

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
