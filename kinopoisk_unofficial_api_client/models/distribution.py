from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.distribution_sub_type_type_1 import DistributionSubTypeType1
from ..models.distribution_sub_type_type_2_type_1 import DistributionSubTypeType2Type1
from ..models.distribution_sub_type_type_3_type_1 import DistributionSubTypeType3Type1
from ..models.distribution_type_type_1 import DistributionTypeType1

if TYPE_CHECKING:
    from ..models.company import Company
    from ..models.distribution_country import DistributionCountry


T = TypeVar("T", bound="Distribution")


@_attrs_define
class Distribution:
    """
    Attributes:
        type (Union[DistributionTypeType1, None]):  Example: PREMIERE.
        sub_type (Union[DistributionSubTypeType1, DistributionSubTypeType2Type1, DistributionSubTypeType3Type1, None]):
            Example: CINEMA.
        date (Union[None, str]):  Example: 1999-05-07.
        re_release (Union[None, bool]):
        country (DistributionCountry):
        companies (List['Company']):
    """

    type: Union[DistributionTypeType1, None]
    sub_type: Union[DistributionSubTypeType1, DistributionSubTypeType2Type1, DistributionSubTypeType3Type1, None]
    date: Union[None, str]
    re_release: Union[None, bool]
    country: "DistributionCountry"
    companies: List["Company"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[None, str]
        if isinstance(self.type, DistributionTypeType1):
            type = self.type.value
        else:
            type = self.type

        sub_type: Union[None, str]
        if isinstance(self.sub_type, DistributionSubTypeType1):
            sub_type = self.sub_type.value
        elif isinstance(self.sub_type, DistributionSubTypeType2Type1):
            sub_type = self.sub_type.value
        elif isinstance(self.sub_type, DistributionSubTypeType3Type1):
            sub_type = self.sub_type.value
        else:
            sub_type = self.sub_type

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

        def _parse_type(data: object) -> Union[DistributionTypeType1, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = DistributionTypeType1(data)

                return type_type_1
            except:  # noqa: E722
                pass
            return cast(Union[DistributionTypeType1, None], data)

        type = _parse_type(d.pop("type"))

        def _parse_sub_type(
            data: object,
        ) -> Union[DistributionSubTypeType1, DistributionSubTypeType2Type1, DistributionSubTypeType3Type1, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sub_type_type_1 = DistributionSubTypeType1(data)

                return sub_type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sub_type_type_2_type_1 = DistributionSubTypeType2Type1(data)

                return sub_type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sub_type_type_3_type_1 = DistributionSubTypeType3Type1(data)

                return sub_type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[DistributionSubTypeType1, DistributionSubTypeType2Type1, DistributionSubTypeType3Type1, None],
                data,
            )

        sub_type = _parse_sub_type(d.pop("subType"))

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
