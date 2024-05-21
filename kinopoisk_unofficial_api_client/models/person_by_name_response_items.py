from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_by_name_response_items_sex_type_1 import PersonByNameResponseItemsSexType1
from ..models.person_by_name_response_items_sex_type_2_type_1 import PersonByNameResponseItemsSexType2Type1
from ..models.person_by_name_response_items_sex_type_3_type_1 import PersonByNameResponseItemsSexType3Type1
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
        sex (Union[None, PersonByNameResponseItemsSexType1, PersonByNameResponseItemsSexType2Type1,
            PersonByNameResponseItemsSexType3Type1, Unset]):  Example: MALE.
        poster_url (Union[Unset, str]):  Example: https://kinopoiskapiunofficial.tech/images/actor_posters/kp/10096.jpg.
    """

    kinopoisk_id: Union[Unset, int] = UNSET
    web_url: Union[Unset, str] = UNSET
    name_ru: Union[None, Unset, str] = UNSET
    name_en: Union[None, Unset, str] = UNSET
    sex: Union[
        None,
        PersonByNameResponseItemsSexType1,
        PersonByNameResponseItemsSexType2Type1,
        PersonByNameResponseItemsSexType3Type1,
        Unset,
    ] = UNSET
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

        sex: Union[None, Unset, str]
        if isinstance(self.sex, Unset):
            sex = UNSET
        elif isinstance(self.sex, PersonByNameResponseItemsSexType1):
            sex = self.sex.value
        elif isinstance(self.sex, PersonByNameResponseItemsSexType2Type1):
            sex = self.sex.value
        elif isinstance(self.sex, PersonByNameResponseItemsSexType3Type1):
            sex = self.sex.value
        else:
            sex = self.sex

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

        def _parse_sex(
            data: object,
        ) -> Union[
            None,
            PersonByNameResponseItemsSexType1,
            PersonByNameResponseItemsSexType2Type1,
            PersonByNameResponseItemsSexType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sex_type_1 = PersonByNameResponseItemsSexType1(data)

                return sex_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sex_type_2_type_1 = PersonByNameResponseItemsSexType2Type1(data)

                return sex_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sex_type_3_type_1 = PersonByNameResponseItemsSexType3Type1(data)

                return sex_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PersonByNameResponseItemsSexType1,
                    PersonByNameResponseItemsSexType2Type1,
                    PersonByNameResponseItemsSexType3Type1,
                    Unset,
                ],
                data,
            )

        sex = _parse_sex(d.pop("sex", UNSET))

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
