from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.related_film_response_items_relation_type import RelatedFilmResponseItemsRelationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RelatedFilmResponseItems")


@_attrs_define
class RelatedFilmResponseItems:
    """
    Attributes:
        film_id (Union[Unset, int]):  Example: 301.
        name_ru (Union[None, Unset, str]):  Example: Матрица.
        name_en (Union[None, Unset, str]):  Example: The Matrix.
        name_original (Union[None, Unset, str]):  Example: The Matrix.
        poster_url (Union[Unset, str]):  Example: https://kinopoiskapiunofficial.tech/images/posters/kp/301.jpg.
        poster_url_preview (Union[Unset, str]):  Example:
            https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg.
        relation_type (Union[Unset, RelatedFilmResponseItemsRelationType]):  Example: SIMILAR.
    """

    film_id: Union[Unset, int] = UNSET
    name_ru: Union[None, Unset, str] = UNSET
    name_en: Union[None, Unset, str] = UNSET
    name_original: Union[None, Unset, str] = UNSET
    poster_url: Union[Unset, str] = UNSET
    poster_url_preview: Union[Unset, str] = UNSET
    relation_type: Union[Unset, RelatedFilmResponseItemsRelationType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        film_id = self.film_id

        name_ru: Union[None, Unset, str]
        if isinstance(self.name_ru, Unset):
            name_ru = UNSET
        else:
            name_ru = self.name_ru

        name_en: Union[None, Unset, str]
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_original: Union[None, Unset, str]
        if isinstance(self.name_original, Unset):
            name_original = UNSET
        else:
            name_original = self.name_original

        poster_url = self.poster_url

        poster_url_preview = self.poster_url_preview

        relation_type: Union[Unset, str] = UNSET
        if not isinstance(self.relation_type, Unset):
            relation_type = self.relation_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if film_id is not UNSET:
            field_dict["filmId"] = film_id
        if name_ru is not UNSET:
            field_dict["nameRu"] = name_ru
        if name_en is not UNSET:
            field_dict["nameEn"] = name_en
        if name_original is not UNSET:
            field_dict["nameOriginal"] = name_original
        if poster_url is not UNSET:
            field_dict["posterUrl"] = poster_url
        if poster_url_preview is not UNSET:
            field_dict["posterUrlPreview"] = poster_url_preview
        if relation_type is not UNSET:
            field_dict["relationType"] = relation_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        film_id = d.pop("filmId", UNSET)

        def _parse_name_ru(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_ru = _parse_name_ru(d.pop("nameRu", UNSET))

        def _parse_name_en(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_en = _parse_name_en(d.pop("nameEn", UNSET))

        def _parse_name_original(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_original = _parse_name_original(d.pop("nameOriginal", UNSET))

        poster_url = d.pop("posterUrl", UNSET)

        poster_url_preview = d.pop("posterUrlPreview", UNSET)

        _relation_type = d.pop("relationType", UNSET)
        relation_type: Union[Unset, RelatedFilmResponseItemsRelationType]
        if isinstance(_relation_type, Unset):
            relation_type = UNSET
        else:
            relation_type = RelatedFilmResponseItemsRelationType(_relation_type)

        related_film_response_items = cls(
            film_id=film_id,
            name_ru=name_ru,
            name_en=name_en,
            name_original=name_original,
            poster_url=poster_url,
            poster_url_preview=poster_url_preview,
            relation_type=relation_type,
        )

        related_film_response_items.additional_properties = d
        return related_film_response_items

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
