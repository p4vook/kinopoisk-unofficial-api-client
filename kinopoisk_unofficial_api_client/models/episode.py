from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Episode")


@_attrs_define
class Episode:
    """
    Attributes:
        season_number (int):  Example: 1.
        episode_number (int):  Example: 1.
        name_ru (Union[None, str]):
        name_en (Union[None, str]):  Example: Chapter One: The Vanishing of Will Byers.
        synopsis (Union[None, str]):  Example: The Vanishing of Will Byers....
        release_date (Union[None, str]):  Example: 2016-07-15.
    """

    season_number: int
    episode_number: int
    name_ru: Union[None, str]
    name_en: Union[None, str]
    synopsis: Union[None, str]
    release_date: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        season_number = self.season_number

        episode_number = self.episode_number

        name_ru: Union[None, str]
        name_ru = self.name_ru

        name_en: Union[None, str]
        name_en = self.name_en

        synopsis: Union[None, str]
        synopsis = self.synopsis

        release_date: Union[None, str]
        release_date = self.release_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seasonNumber": season_number,
                "episodeNumber": episode_number,
                "nameRu": name_ru,
                "nameEn": name_en,
                "synopsis": synopsis,
                "releaseDate": release_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        season_number = d.pop("seasonNumber")

        episode_number = d.pop("episodeNumber")

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

        def _parse_synopsis(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        synopsis = _parse_synopsis(d.pop("synopsis"))

        def _parse_release_date(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        release_date = _parse_release_date(d.pop("releaseDate"))

        episode = cls(
            season_number=season_number,
            episode_number=episode_number,
            name_ru=name_ru,
            name_en=name_en,
            synopsis=synopsis,
            release_date=release_date,
        )

        episode.additional_properties = d
        return episode

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
