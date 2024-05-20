from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.film_collection_response import FilmCollectionResponse
from ...models.get_api_v22_films_collections_type import GetApiV22FilmsCollectionsType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type: Union[Unset, GetApiV22FilmsCollectionsType] = GetApiV22FilmsCollectionsType.TOP_POPULAR_ALL,
    page: Union[Unset, int] = 1,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_type: Union[Unset, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value

    params["type"] = json_type

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.2/films/collections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, FilmCollectionResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FilmCollectionResponse.from_dict(response.json())

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
) -> Response[Union[Any, FilmCollectionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, GetApiV22FilmsCollectionsType] = GetApiV22FilmsCollectionsType.TOP_POPULAR_ALL,
    page: Union[Unset, int] = 1,
) -> Response[Union[Any, FilmCollectionResponse]]:
    """получить список фильмов из различных топов или коллекций. Например
    https://www.kinopoisk.ru/top/lists/58/

     Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.

    Args:
        type (Union[Unset, GetApiV22FilmsCollectionsType]):  Default:
            GetApiV22FilmsCollectionsType.TOP_POPULAR_ALL.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FilmCollectionResponse]]
    """

    kwargs = _get_kwargs(
        type=type,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, GetApiV22FilmsCollectionsType] = GetApiV22FilmsCollectionsType.TOP_POPULAR_ALL,
    page: Union[Unset, int] = 1,
) -> Optional[Union[Any, FilmCollectionResponse]]:
    """получить список фильмов из различных топов или коллекций. Например
    https://www.kinopoisk.ru/top/lists/58/

     Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.

    Args:
        type (Union[Unset, GetApiV22FilmsCollectionsType]):  Default:
            GetApiV22FilmsCollectionsType.TOP_POPULAR_ALL.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FilmCollectionResponse]
    """

    return sync_detailed(
        client=client,
        type=type,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, GetApiV22FilmsCollectionsType] = GetApiV22FilmsCollectionsType.TOP_POPULAR_ALL,
    page: Union[Unset, int] = 1,
) -> Response[Union[Any, FilmCollectionResponse]]:
    """получить список фильмов из различных топов или коллекций. Например
    https://www.kinopoisk.ru/top/lists/58/

     Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.

    Args:
        type (Union[Unset, GetApiV22FilmsCollectionsType]):  Default:
            GetApiV22FilmsCollectionsType.TOP_POPULAR_ALL.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FilmCollectionResponse]]
    """

    kwargs = _get_kwargs(
        type=type,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, GetApiV22FilmsCollectionsType] = GetApiV22FilmsCollectionsType.TOP_POPULAR_ALL,
    page: Union[Unset, int] = 1,
) -> Optional[Union[Any, FilmCollectionResponse]]:
    """получить список фильмов из различных топов или коллекций. Например
    https://www.kinopoisk.ru/top/lists/58/

     Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.

    Args:
        type (Union[Unset, GetApiV22FilmsCollectionsType]):  Default:
            GetApiV22FilmsCollectionsType.TOP_POPULAR_ALL.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FilmCollectionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            type=type,
            page=page,
        )
    ).parsed
