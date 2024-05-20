from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.external_source_response_items import ExternalSourceResponseItems


T = TypeVar("T", bound="ExternalSourceResponse")


@_attrs_define
class ExternalSourceResponse:
    """
    Attributes:
        total (int): Суммарное кол-во сайтов Example: 12.
        items (List['ExternalSourceResponseItems']):
    """

    total: int
    items: List["ExternalSourceResponseItems"]
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
        from ..models.external_source_response_items import ExternalSourceResponseItems

        d = src_dict.copy()
        total = d.pop("total")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ExternalSourceResponseItems.from_dict(items_item_data)

            items.append(items_item)

        external_source_response = cls(
            total=total,
            items=items,
        )

        external_source_response.additional_properties = d
        return external_source_response

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
