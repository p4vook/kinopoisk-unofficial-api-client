from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.staff_response_profession_key import StaffResponseProfessionKey

T = TypeVar("T", bound="StaffResponse")


@_attrs_define
class StaffResponse:
    """
    Attributes:
        staff_id (int):  Example: 66539.
        name_ru (Union[None, str]):  Example: Винс Гиллиган.
        name_en (Union[None, str]):  Example: Vince Gilligan.
        description (Union[None, str]):  Example: Neo.
        poster_url (str):  Example: https://st.kp.yandex.net/images/actor/66539.jpg.
        profession_text (str):  Example: Режиссеры.
        profession_key (StaffResponseProfessionKey):  Example: DIRECTOR.
    """

    staff_id: int
    name_ru: Union[None, str]
    name_en: Union[None, str]
    description: Union[None, str]
    poster_url: str
    profession_text: str
    profession_key: StaffResponseProfessionKey
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        staff_id = self.staff_id

        name_ru: Union[None, str]
        name_ru = self.name_ru

        name_en: Union[None, str]
        name_en = self.name_en

        description: Union[None, str]
        description = self.description

        poster_url = self.poster_url

        profession_text = self.profession_text

        profession_key = self.profession_key.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "staffId": staff_id,
                "nameRu": name_ru,
                "nameEn": name_en,
                "description": description,
                "posterUrl": poster_url,
                "professionText": profession_text,
                "professionKey": profession_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        staff_id = d.pop("staffId")

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

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        poster_url = d.pop("posterUrl")

        profession_text = d.pop("professionText")

        profession_key = StaffResponseProfessionKey(d.pop("professionKey"))

        staff_response = cls(
            staff_id=staff_id,
            name_ru=name_ru,
            name_en=name_en,
            description=description,
            poster_url=poster_url,
            profession_text=profession_text,
            profession_key=profession_key,
        )

        staff_response.additional_properties = d
        return staff_response

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
