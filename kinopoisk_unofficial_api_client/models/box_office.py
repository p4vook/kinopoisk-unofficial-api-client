from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BoxOffice")


@_attrs_define
class BoxOffice:
    """
    Attributes:
        type (str):  Example: BUDGET.
        amount (int):  Example: 63000000.
        currency_code (str):  Example: USD.
        name (str):  Example: US Dollar.
        symbol (str):  Example: $.
    """

    type: str
    amount: int
    currency_code: str
    name: str
    symbol: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        amount = self.amount

        currency_code = self.currency_code

        name = self.name

        symbol = self.symbol

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "amount": amount,
                "currencyCode": currency_code,
                "name": name,
                "symbol": symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        amount = d.pop("amount")

        currency_code = d.pop("currencyCode")

        name = d.pop("name")

        symbol = d.pop("symbol")

        box_office = cls(
            type=type,
            amount=amount,
            currency_code=currency_code,
            name=name,
            symbol=symbol,
        )

        box_office.additional_properties = d
        return box_office

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
