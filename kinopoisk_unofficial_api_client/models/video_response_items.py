from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.video_response_items_site import VideoResponseItemsSite
from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoResponseItems")


@_attrs_define
class VideoResponseItems:
    """
    Attributes:
        url (Union[Unset, str]):  Example: https://www.youtube.com/watch?v=gbcVZgO4n4E.
        name (Union[Unset, str]):  Example: Мстители: Финал – официальный трейлер (16+).
        site (Union[Unset, VideoResponseItemsSite]):  Example: YOUTUBE.
    """

    url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    site: Union[Unset, VideoResponseItemsSite] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        name = self.name

        site: Union[Unset, str] = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if name is not UNSET:
            field_dict["name"] = name
        if site is not UNSET:
            field_dict["site"] = site

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        name = d.pop("name", UNSET)

        _site = d.pop("site", UNSET)
        site: Union[Unset, VideoResponseItemsSite]
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = VideoResponseItemsSite(_site)

        video_response_items = cls(
            url=url,
            name=name,
            site=site,
        )

        video_response_items.additional_properties = d
        return video_response_items

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
