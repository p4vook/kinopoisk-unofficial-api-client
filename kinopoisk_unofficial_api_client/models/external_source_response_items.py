from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalSourceResponseItems")


@_attrs_define
class ExternalSourceResponseItems:
    """
    Attributes:
        url (Union[Unset, str]):  Example:
            https://okko.tv/movie/equilibrium?utm_medium=referral&utm_source=yandex_search&utm_campaign=new_search_feed.
        platform (Union[Unset, str]):  Example: Okko.
        logo_url (Union[Unset, str]):  Example: https://avatars.mds.yandex.net/get-
            ott/239697/7713e586-17d1-42d1-ac62-53e9ef1e70c3/orig.
        positive_rating (Union[Unset, int]):  Example: 122.
        negative_rating (Union[Unset, int]):  Example: 12.
        author (Union[Unset, str]):  Example: Username.
        title (Union[None, Unset, str]):  Example: Title.
        description (Union[Unset, str]):  Example: text.
    """

    url: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    positive_rating: Union[Unset, int] = UNSET
    negative_rating: Union[Unset, int] = UNSET
    author: Union[Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        platform = self.platform

        logo_url = self.logo_url

        positive_rating = self.positive_rating

        negative_rating = self.negative_rating

        author = self.author

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if platform is not UNSET:
            field_dict["platform"] = platform
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if positive_rating is not UNSET:
            field_dict["positiveRating"] = positive_rating
        if negative_rating is not UNSET:
            field_dict["negativeRating"] = negative_rating
        if author is not UNSET:
            field_dict["author"] = author
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        platform = d.pop("platform", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        positive_rating = d.pop("positiveRating", UNSET)

        negative_rating = d.pop("negativeRating", UNSET)

        author = d.pop("author", UNSET)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        description = d.pop("description", UNSET)

        external_source_response_items = cls(
            url=url,
            platform=platform,
            logo_url=logo_url,
            positive_rating=positive_rating,
            negative_rating=negative_rating,
            author=author,
            title=title,
            description=description,
        )

        external_source_response_items.additional_properties = d
        return external_source_response_items

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
