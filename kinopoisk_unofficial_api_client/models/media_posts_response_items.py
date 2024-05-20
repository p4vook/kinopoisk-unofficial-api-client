from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaPostsResponseItems")


@_attrs_define
class MediaPostsResponseItems:
    """
    Attributes:
        kinopoisk_id (Union[Unset, int]):  Example: 4008943.
        image_url (Union[Unset, str]):  Example: https://avatars.mds.yandex.net/get-kinopoisk-post-
            thumb/1348084/a879121a01ae7416afac04e2061521d5/orig.
        title (Union[Unset, str]):  Example: «Общество снега»: кино о голодающих в Андах регбистах, которое претендует
            на «Оскар».
        description (Union[Unset, str]):  Example: «Общество снега» на Netflix — драма выживания, претендующая на
            «Оскар». Это история уругвайских регбистов, попавших в авиакатастрофу и оказавшихся в заснеженных горах.
            Рассказываем, чем же они там питались..
        url (Union[Unset, str]):  Example: https://www.kinopoisk.ru/api/webview/post/4008943.
        published_at (Union[Unset, str]):  Example: 2024-01-09T12:35:22.
    """

    kinopoisk_id: Union[Unset, int] = UNSET
    image_url: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    published_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kinopoisk_id = self.kinopoisk_id

        image_url = self.image_url

        title = self.title

        description = self.description

        url = self.url

        published_at = self.published_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kinopoisk_id is not UNSET:
            field_dict["kinopoiskId"] = kinopoisk_id
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if url is not UNSET:
            field_dict["url"] = url
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kinopoisk_id = d.pop("kinopoiskId", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        url = d.pop("url", UNSET)

        published_at = d.pop("publishedAt", UNSET)

        media_posts_response_items = cls(
            kinopoisk_id=kinopoisk_id,
            image_url=image_url,
            title=title,
            description=description,
            url=url,
            published_at=published_at,
        )

        media_posts_response_items.additional_properties = d
        return media_posts_response_items

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
