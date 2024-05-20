from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FiltersResponseGenres")


@_attrs_define
class FiltersResponseGenres:
    """
    Attributes:
        id (Union[Unset, int]):  Example: 1.
        genre (Union[Unset, str]):  Example: боевик.
    """

    id: Union[Unset, int] = UNSET
    genre: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        genre = self.genre

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if genre is not UNSET:
            field_dict["genre"] = genre

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        genre = d.pop("genre", UNSET)

        filters_response_genres = cls(
            id=id,
            genre=genre,
        )

        filters_response_genres.additional_properties = d
        return filters_response_genres

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
