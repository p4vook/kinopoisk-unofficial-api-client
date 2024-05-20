from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.review_response_items_type import ReviewResponseItemsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReviewResponseItems")


@_attrs_define
class ReviewResponseItems:
    """
    Attributes:
        kinopoisk_id (Union[Unset, int]):  Example: 2.
        type (Union[Unset, ReviewResponseItemsType]):
        date (Union[Unset, str]):  Example: 2010-09-05T20:37:00.
        positive_rating (Union[Unset, int]):  Example: 122.
        negative_rating (Union[Unset, int]):  Example: 12.
        author (Union[Unset, str]):  Example: Username.
        title (Union[None, Unset, str]):  Example: Title.
        description (Union[Unset, str]):  Example: text.
    """

    kinopoisk_id: Union[Unset, int] = UNSET
    type: Union[Unset, ReviewResponseItemsType] = UNSET
    date: Union[Unset, str] = UNSET
    positive_rating: Union[Unset, int] = UNSET
    negative_rating: Union[Unset, int] = UNSET
    author: Union[Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kinopoisk_id = self.kinopoisk_id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        date = self.date

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
        if kinopoisk_id is not UNSET:
            field_dict["kinopoiskId"] = kinopoisk_id
        if type is not UNSET:
            field_dict["type"] = type
        if date is not UNSET:
            field_dict["date"] = date
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
        kinopoisk_id = d.pop("kinopoiskId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ReviewResponseItemsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ReviewResponseItemsType(_type)

        date = d.pop("date", UNSET)

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

        review_response_items = cls(
            kinopoisk_id=kinopoisk_id,
            type=type,
            date=date,
            positive_rating=positive_rating,
            negative_rating=negative_rating,
            author=author,
            title=title,
            description=description,
        )

        review_response_items.additional_properties = d
        return review_response_items

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
