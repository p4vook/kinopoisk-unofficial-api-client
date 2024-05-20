from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.award_person import AwardPerson


T = TypeVar("T", bound="Award")


@_attrs_define
class Award:
    """
    Attributes:
        name (str):  Example: Оскар.
        win (bool):  Example: True.
        image_url (Union[None, str]):  Example: https://avatars.mds.yandex.net/get-kinopoisk-
            image/1600647/09035193-2458-4de7-a7df-ad8f85b73798/orig.
        nomination_name (str):  Example: Лучший звук.
        year (int):  Example: 2000.
        persons (Union[Unset, List['AwardPerson']]):
    """

    name: str
    win: bool
    image_url: Union[None, str]
    nomination_name: str
    year: int
    persons: Union[Unset, List["AwardPerson"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        win = self.win

        image_url: Union[None, str]
        image_url = self.image_url

        nomination_name = self.nomination_name

        year = self.year

        persons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.persons, Unset):
            persons = []
            for persons_item_data in self.persons:
                persons_item = persons_item_data.to_dict()
                persons.append(persons_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "win": win,
                "imageUrl": image_url,
                "nominationName": nomination_name,
                "year": year,
            }
        )
        if persons is not UNSET:
            field_dict["persons"] = persons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.award_person import AwardPerson

        d = src_dict.copy()
        name = d.pop("name")

        win = d.pop("win")

        def _parse_image_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        image_url = _parse_image_url(d.pop("imageUrl"))

        nomination_name = d.pop("nominationName")

        year = d.pop("year")

        persons = []
        _persons = d.pop("persons", UNSET)
        for persons_item_data in _persons or []:
            persons_item = AwardPerson.from_dict(persons_item_data)

            persons.append(persons_item)

        award = cls(
            name=name,
            win=win,
            image_url=image_url,
            nomination_name=nomination_name,
            year=year,
            persons=persons,
        )

        award.additional_properties = d
        return award

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
