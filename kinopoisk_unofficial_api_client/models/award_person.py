from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AwardPerson")


@_attrs_define
class AwardPerson:
    """
    Attributes:
        kinopoisk_id (int):  Example: 1937039.
        web_url (str):  Example: https://www.kinopoisk.ru/name/1937039/.
        name_ru (Union[None, str]):  Example: Джон Т. Рейц.
        name_en (Union[None, str]):  Example: John T. Reitz.
        sex (str):  Example: MALE.
        poster_url (str):  Example: https://kinopoiskapiunofficial.tech/images/actor_posters/kp/1937039.jpg.
        growth (Union[None, int]):  Example: 178.
        birthday (Union[None, str]):  Example: 1955-11-02.
        death (Union[None, str]):  Example: 2019-01-06.
        age (Union[None, int]):  Example: 21.
        birthplace (Union[None, str]):  Example: Лос-Анджелес, Калифорния, США.
        deathplace (Union[None, str]):  Example: Лос-Анджелес, Калифорния, США.
        profession (Union[None, str]):  Example: Монтажер, Продюсер.
    """

    kinopoisk_id: int
    web_url: str
    name_ru: Union[None, str]
    name_en: Union[None, str]
    sex: str
    poster_url: str
    growth: Union[None, int]
    birthday: Union[None, str]
    death: Union[None, str]
    age: Union[None, int]
    birthplace: Union[None, str]
    deathplace: Union[None, str]
    profession: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kinopoisk_id = self.kinopoisk_id

        web_url = self.web_url

        name_ru: Union[None, str]
        name_ru = self.name_ru

        name_en: Union[None, str]
        name_en = self.name_en

        sex = self.sex

        poster_url = self.poster_url

        growth: Union[None, int]
        growth = self.growth

        birthday: Union[None, str]
        birthday = self.birthday

        death: Union[None, str]
        death = self.death

        age: Union[None, int]
        age = self.age

        birthplace: Union[None, str]
        birthplace = self.birthplace

        deathplace: Union[None, str]
        deathplace = self.deathplace

        profession: Union[None, str]
        profession = self.profession

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kinopoiskId": kinopoisk_id,
                "webUrl": web_url,
                "nameRu": name_ru,
                "nameEn": name_en,
                "sex": sex,
                "posterUrl": poster_url,
                "growth": growth,
                "birthday": birthday,
                "death": death,
                "age": age,
                "birthplace": birthplace,
                "deathplace": deathplace,
                "profession": profession,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kinopoisk_id = d.pop("kinopoiskId")

        web_url = d.pop("webUrl")

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

        sex = d.pop("sex")

        poster_url = d.pop("posterUrl")

        def _parse_growth(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        growth = _parse_growth(d.pop("growth"))

        def _parse_birthday(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        birthday = _parse_birthday(d.pop("birthday"))

        def _parse_death(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        death = _parse_death(d.pop("death"))

        def _parse_age(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        age = _parse_age(d.pop("age"))

        def _parse_birthplace(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        birthplace = _parse_birthplace(d.pop("birthplace"))

        def _parse_deathplace(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deathplace = _parse_deathplace(d.pop("deathplace"))

        def _parse_profession(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        profession = _parse_profession(d.pop("profession"))

        award_person = cls(
            kinopoisk_id=kinopoisk_id,
            web_url=web_url,
            name_ru=name_ru,
            name_en=name_en,
            sex=sex,
            poster_url=poster_url,
            growth=growth,
            birthday=birthday,
            death=death,
            age=age,
            birthplace=birthplace,
            deathplace=deathplace,
            profession=profession,
        )

        award_person.additional_properties = d
        return award_person

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
