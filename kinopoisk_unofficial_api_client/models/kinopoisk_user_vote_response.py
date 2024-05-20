from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.kinopoisk_user_vote_response_items import KinopoiskUserVoteResponseItems


T = TypeVar("T", bound="KinopoiskUserVoteResponse")


@_attrs_define
class KinopoiskUserVoteResponse:
    """
    Attributes:
        total (int):  Example: 200.
        total_pages (int):  Example: 7.
        items (List['KinopoiskUserVoteResponseItems']):
    """

    total: int
    total_pages: int
    items: List["KinopoiskUserVoteResponseItems"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total

        total_pages = self.total_pages

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "totalPages": total_pages,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.kinopoisk_user_vote_response_items import KinopoiskUserVoteResponseItems

        d = src_dict.copy()
        total = d.pop("total")

        total_pages = d.pop("totalPages")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = KinopoiskUserVoteResponseItems.from_dict(items_item_data)

            items.append(items_item)

        kinopoisk_user_vote_response = cls(
            total=total,
            total_pages=total_pages,
            items=items,
        )

        kinopoisk_user_vote_response.additional_properties = d
        return kinopoisk_user_vote_response

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
