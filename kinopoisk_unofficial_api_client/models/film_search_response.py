from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.film_search_response_films import FilmSearchResponseFilms


T = TypeVar("T", bound="FilmSearchResponse")


@_attrs_define
class FilmSearchResponse:
    """
    Attributes:
        keyword (str):  Example: мстители.
        pages_count (int):  Example: 7.
        search_films_count_result (int):  Example: 134.
        films (List['FilmSearchResponseFilms']):
    """

    keyword: str
    pages_count: int
    search_films_count_result: int
    films: List["FilmSearchResponseFilms"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keyword = self.keyword

        pages_count = self.pages_count

        search_films_count_result = self.search_films_count_result

        films = []
        for films_item_data in self.films:
            films_item = films_item_data.to_dict()
            films.append(films_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keyword": keyword,
                "pagesCount": pages_count,
                "searchFilmsCountResult": search_films_count_result,
                "films": films,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.film_search_response_films import FilmSearchResponseFilms

        d = src_dict.copy()
        keyword = d.pop("keyword")

        pages_count = d.pop("pagesCount")

        search_films_count_result = d.pop("searchFilmsCountResult")

        films = []
        _films = d.pop("films")
        for films_item_data in _films:
            films_item = FilmSearchResponseFilms.from_dict(films_item_data)

            films.append(films_item)

        film_search_response = cls(
            keyword=keyword,
            pages_count=pages_count,
            search_films_count_result=search_films_count_result,
            films=films,
        )

        film_search_response.additional_properties = d
        return film_search_response

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
