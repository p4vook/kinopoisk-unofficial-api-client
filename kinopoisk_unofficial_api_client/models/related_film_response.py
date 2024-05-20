from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.related_film_response_items import RelatedFilmResponseItems


T = TypeVar("T", bound="RelatedFilmResponse")


@_attrs_define
class RelatedFilmResponse:
    """
    Attributes:
        total (int):  Example: 7.
        items (List['RelatedFilmResponseItems']):
    """

    total: int
    items: List["RelatedFilmResponseItems"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.related_film_response_items import RelatedFilmResponseItems

        d = src_dict.copy()
        total = d.pop("total")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = RelatedFilmResponseItems.from_dict(items_item_data)

            items.append(items_item)

        related_film_response = cls(
            total=total,
            items=items,
        )

        related_film_response.additional_properties = d
        return related_film_response

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
