from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.film_search_by_filters_response import FilmSearchByFiltersResponse
from ...models.get_api_v22_films_order import GetApiV22FilmsOrder
from ...models.get_api_v22_films_type import GetApiV22FilmsType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    countries: Union[Unset, List[int]] = UNSET,
    genres: Union[Unset, List[int]] = UNSET,
    order: Union[Unset, GetApiV22FilmsOrder] = GetApiV22FilmsOrder.RATING,
    type: Union[Unset, GetApiV22FilmsType] = GetApiV22FilmsType.ALL,
    rating_from: Union[Unset, float] = 0.0,
    rating_to: Union[Unset, float] = 10.0,
    year_from: Union[Unset, int] = 1000,
    year_to: Union[Unset, int] = 3000,
    imdb_id: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_countries: Union[Unset, List[int]] = UNSET
    if not isinstance(countries, Unset):
        json_countries = countries

    params["countries"] = json_countries

    json_genres: Union[Unset, List[int]] = UNSET
    if not isinstance(genres, Unset):
        json_genres = genres

    params["genres"] = json_genres

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    json_type: Union[Unset, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value

    params["type"] = json_type

    params["ratingFrom"] = rating_from

    params["ratingTo"] = rating_to

    params["yearFrom"] = year_from

    params["yearTo"] = year_to

    params["imdbId"] = imdb_id

    params["keyword"] = keyword

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.2/films",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, FilmSearchByFiltersResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FilmSearchByFiltersResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.PAYMENT_REQUIRED:
        response_402 = cast(Any, None)
        return response_402
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, FilmSearchByFiltersResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    countries: Union[Unset, List[int]] = UNSET,
    genres: Union[Unset, List[int]] = UNSET,
    order: Union[Unset, GetApiV22FilmsOrder] = GetApiV22FilmsOrder.RATING,
    type: Union[Unset, GetApiV22FilmsType] = GetApiV22FilmsType.ALL,
    rating_from: Union[Unset, float] = 0.0,
    rating_to: Union[Unset, float] = 10.0,
    year_from: Union[Unset, int] = 1000,
    year_to: Union[Unset, int] = 3000,
    imdb_id: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
) -> Response[Union[Any, FilmSearchByFiltersResponse]]:
    """получить список фильмов по различным фильтрам

     Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов. Данный
    эндпоинт не возращает более 400 фильмов. <i>Используй /api/v2.2/films/filters чтобы получить id
    стран и жанров.</i>

    Args:
        countries (Union[Unset, List[int]]):
        genres (Union[Unset, List[int]]):
        order (Union[Unset, GetApiV22FilmsOrder]):  Default: GetApiV22FilmsOrder.RATING.
        type (Union[Unset, GetApiV22FilmsType]):  Default: GetApiV22FilmsType.ALL.
        rating_from (Union[Unset, float]):  Default: 0.0.
        rating_to (Union[Unset, float]):  Default: 10.0.
        year_from (Union[Unset, int]):  Default: 1000.
        year_to (Union[Unset, int]):  Default: 3000.
        imdb_id (Union[Unset, str]):
        keyword (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FilmSearchByFiltersResponse]]
    """

    kwargs = _get_kwargs(
        countries=countries,
        genres=genres,
        order=order,
        type=type,
        rating_from=rating_from,
        rating_to=rating_to,
        year_from=year_from,
        year_to=year_to,
        imdb_id=imdb_id,
        keyword=keyword,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    countries: Union[Unset, List[int]] = UNSET,
    genres: Union[Unset, List[int]] = UNSET,
    order: Union[Unset, GetApiV22FilmsOrder] = GetApiV22FilmsOrder.RATING,
    type: Union[Unset, GetApiV22FilmsType] = GetApiV22FilmsType.ALL,
    rating_from: Union[Unset, float] = 0.0,
    rating_to: Union[Unset, float] = 10.0,
    year_from: Union[Unset, int] = 1000,
    year_to: Union[Unset, int] = 3000,
    imdb_id: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
) -> Optional[Union[Any, FilmSearchByFiltersResponse]]:
    """получить список фильмов по различным фильтрам

     Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов. Данный
    эндпоинт не возращает более 400 фильмов. <i>Используй /api/v2.2/films/filters чтобы получить id
    стран и жанров.</i>

    Args:
        countries (Union[Unset, List[int]]):
        genres (Union[Unset, List[int]]):
        order (Union[Unset, GetApiV22FilmsOrder]):  Default: GetApiV22FilmsOrder.RATING.
        type (Union[Unset, GetApiV22FilmsType]):  Default: GetApiV22FilmsType.ALL.
        rating_from (Union[Unset, float]):  Default: 0.0.
        rating_to (Union[Unset, float]):  Default: 10.0.
        year_from (Union[Unset, int]):  Default: 1000.
        year_to (Union[Unset, int]):  Default: 3000.
        imdb_id (Union[Unset, str]):
        keyword (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FilmSearchByFiltersResponse]
    """

    return sync_detailed(
        client=client,
        countries=countries,
        genres=genres,
        order=order,
        type=type,
        rating_from=rating_from,
        rating_to=rating_to,
        year_from=year_from,
        year_to=year_to,
        imdb_id=imdb_id,
        keyword=keyword,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    countries: Union[Unset, List[int]] = UNSET,
    genres: Union[Unset, List[int]] = UNSET,
    order: Union[Unset, GetApiV22FilmsOrder] = GetApiV22FilmsOrder.RATING,
    type: Union[Unset, GetApiV22FilmsType] = GetApiV22FilmsType.ALL,
    rating_from: Union[Unset, float] = 0.0,
    rating_to: Union[Unset, float] = 10.0,
    year_from: Union[Unset, int] = 1000,
    year_to: Union[Unset, int] = 3000,
    imdb_id: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
) -> Response[Union[Any, FilmSearchByFiltersResponse]]:
    """получить список фильмов по различным фильтрам

     Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов. Данный
    эндпоинт не возращает более 400 фильмов. <i>Используй /api/v2.2/films/filters чтобы получить id
    стран и жанров.</i>

    Args:
        countries (Union[Unset, List[int]]):
        genres (Union[Unset, List[int]]):
        order (Union[Unset, GetApiV22FilmsOrder]):  Default: GetApiV22FilmsOrder.RATING.
        type (Union[Unset, GetApiV22FilmsType]):  Default: GetApiV22FilmsType.ALL.
        rating_from (Union[Unset, float]):  Default: 0.0.
        rating_to (Union[Unset, float]):  Default: 10.0.
        year_from (Union[Unset, int]):  Default: 1000.
        year_to (Union[Unset, int]):  Default: 3000.
        imdb_id (Union[Unset, str]):
        keyword (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FilmSearchByFiltersResponse]]
    """

    kwargs = _get_kwargs(
        countries=countries,
        genres=genres,
        order=order,
        type=type,
        rating_from=rating_from,
        rating_to=rating_to,
        year_from=year_from,
        year_to=year_to,
        imdb_id=imdb_id,
        keyword=keyword,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    countries: Union[Unset, List[int]] = UNSET,
    genres: Union[Unset, List[int]] = UNSET,
    order: Union[Unset, GetApiV22FilmsOrder] = GetApiV22FilmsOrder.RATING,
    type: Union[Unset, GetApiV22FilmsType] = GetApiV22FilmsType.ALL,
    rating_from: Union[Unset, float] = 0.0,
    rating_to: Union[Unset, float] = 10.0,
    year_from: Union[Unset, int] = 1000,
    year_to: Union[Unset, int] = 3000,
    imdb_id: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
) -> Optional[Union[Any, FilmSearchByFiltersResponse]]:
    """получить список фильмов по различным фильтрам

     Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов. Данный
    эндпоинт не возращает более 400 фильмов. <i>Используй /api/v2.2/films/filters чтобы получить id
    стран и жанров.</i>

    Args:
        countries (Union[Unset, List[int]]):
        genres (Union[Unset, List[int]]):
        order (Union[Unset, GetApiV22FilmsOrder]):  Default: GetApiV22FilmsOrder.RATING.
        type (Union[Unset, GetApiV22FilmsType]):  Default: GetApiV22FilmsType.ALL.
        rating_from (Union[Unset, float]):  Default: 0.0.
        rating_to (Union[Unset, float]):  Default: 10.0.
        year_from (Union[Unset, int]):  Default: 1000.
        year_to (Union[Unset, int]):  Default: 3000.
        imdb_id (Union[Unset, str]):
        keyword (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FilmSearchByFiltersResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            countries=countries,
            genres=genres,
            order=order,
            type=type,
            rating_from=rating_from,
            rating_to=rating_to,
            year_from=year_from,
            year_to=year_to,
            imdb_id=imdb_id,
            keyword=keyword,
            page=page,
        )
    ).parsed
