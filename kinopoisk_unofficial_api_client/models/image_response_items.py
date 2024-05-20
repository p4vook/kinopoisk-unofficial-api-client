from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageResponseItems")


@_attrs_define
class ImageResponseItems:
    """
    Attributes:
        image_url (Union[Unset, str]):  Example: https://avatars.mds.yandex.net/get-kinopoisk-
            image/4303601/2924f6c4-4ea0-4a1d-9a48-f29577172b27/orig.
        preview_url (Union[Unset, str]):  Example: https://avatars.mds.yandex.net/get-kinopoisk-
            image/4303601/2924f6c4-4ea0-4a1d-9a48-f29577172b27/300x.
    """

    image_url: Union[Unset, str] = UNSET
    preview_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image_url = self.image_url

        preview_url = self.preview_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if preview_url is not UNSET:
            field_dict["previewUrl"] = preview_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        image_url = d.pop("imageUrl", UNSET)

        preview_url = d.pop("previewUrl", UNSET)

        image_response_items = cls(
            image_url=image_url,
            preview_url=preview_url,
        )

        image_response_items.additional_properties = d
        return image_response_items

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
