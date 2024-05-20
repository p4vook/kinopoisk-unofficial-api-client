from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_by_name_response_items_sex import PersonByNameResponseItemsSex
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonByNameResponseItems")


@_attrs_define
class PersonByNameResponseItems:
    """
    Attributes:
        kinopoisk_id (Union[Unset, int]):  Example: 66539.
        web_url (Union[Unset, str]):  Example: 10096.
        name_ru (Union[None, Unset, str]):  Example: Винс Гиллиган.
        name_en (Union[None, Unset, str]):  Example: Vince Gilligan.
        sex (Union[Unset, PersonByNameResponseItemsSex]):  Example: MALE.
        poster_url (Union[Unset, str]):  Example: https://kinopoiskapiunofficial.tech/images/actor_posters/kp/10096.jpg.
    """

    kinopoisk_id: Union[Unset, int] = UNSET
    web_url: Union[Unset, str] = UNSET
    name_ru: Union[None, Unset, str] = UNSET
    name_en: Union[None, Unset, str] = UNSET
    sex: Union[Unset, PersonByNameResponseItemsSex] = UNSET
    poster_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kinopoisk_id = self.kinopoisk_id

        web_url = self.web_url

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

        sex: Union[Unset, str] = UNSET
        if not isinstance(self.sex, Unset):
            sex = self.sex.value

        poster_url = self.poster_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kinopoisk_id is not UNSET:
            field_dict["kinopoiskId"] = kinopoisk_id
        if web_url is not UNSET:
            field_dict["webUrl"] = web_url
        if name_ru is not UNSET:
            field_dict["nameRu"] = name_ru
        if name_en is not UNSET:
            field_dict["nameEn"] = name_en
        if sex is not UNSET:
            field_dict["sex"] = sex
        if poster_url is not UNSET:
            field_dict["posterUrl"] = poster_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kinopoisk_id = d.pop("kinopoiskId", UNSET)

        web_url = d.pop("webUrl", UNSET)

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

        _sex = d.pop("sex", UNSET)
        sex: Union[Unset, PersonByNameResponseItemsSex]
        if isinstance(_sex, Unset):
            sex = UNSET
        else:
            sex = PersonByNameResponseItemsSex(_sex)

        poster_url = d.pop("posterUrl", UNSET)

        person_by_name_response_items = cls(
            kinopoisk_id=kinopoisk_id,
            web_url=web_url,
            name_ru=name_ru,
            name_en=name_en,
            sex=sex,
            poster_url=poster_url,
        )

        person_by_name_response_items.additional_properties = d
        return person_by_name_response_items

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
