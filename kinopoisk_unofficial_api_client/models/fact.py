from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fact_type import FactType

T = TypeVar("T", bound="Fact")


@_attrs_define
class Fact:
    """
    Attributes:
        text (str):  Example: В эпизоде, где Тринити и Нео в поисках Морфиуса оказываются на крыше....
        type (FactType):  Example: BLOOPER.
        spoiler (bool):
    """

    text: str
    type: FactType
    spoiler: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        type = self.type.value

        spoiler = self.spoiler

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "type": type,
                "spoiler": spoiler,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        type = FactType(d.pop("type"))

        spoiler = d.pop("spoiler")

        fact = cls(
            text=text,
            type=type,
            spoiler=spoiler,
        )

        fact.additional_properties = d
        return fact

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
