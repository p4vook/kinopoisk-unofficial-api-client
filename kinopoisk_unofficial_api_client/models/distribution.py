from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.distribution_sub_type import DistributionSubType
from ..models.distribution_type import DistributionType

if TYPE_CHECKING:
    from ..models.company import Company
    from ..models.distribution_country import DistributionCountry


T = TypeVar("T", bound="Distribution")


@_attrs_define
class Distribution:
    """
    Attributes:
        type (DistributionType):  Example: PREMIERE.
        sub_type (DistributionSubType):  Example: CINEMA.
        date (Union[None, str]):  Example: 1999-05-07.
        re_release (Union[None, bool]):
        country (DistributionCountry):
        companies (List['Company']):
    """

    type: DistributionType
    sub_type: DistributionSubType
    date: Union[None, str]
    re_release: Union[None, bool]
    country: "DistributionCountry"
    companies: List["Company"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        sub_type = self.sub_type.value

        date: Union[None, str]
        date = self.date

        re_release: Union[None, bool]
        re_release = self.re_release

        country = self.country.to_dict()

        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "subType": sub_type,
                "date": date,
                "reRelease": re_release,
                "country": country,
                "companies": companies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company import Company
        from ..models.distribution_country import DistributionCountry

        d = src_dict.copy()
        type = DistributionType(d.pop("type"))

        sub_type = DistributionSubType(d.pop("subType"))

        def _parse_date(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        date = _parse_date(d.pop("date"))

        def _parse_re_release(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        re_release = _parse_re_release(d.pop("reRelease"))

        country = DistributionCountry.from_dict(d.pop("country"))

        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = Company.from_dict(companies_item_data)

            companies.append(companies_item)

        distribution = cls(
            type=type,
            sub_type=sub_type,
            date=date,
            re_release=re_release,
            country=country,
            companies=companies,
        )

        distribution.additional_properties = d
        return distribution

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
