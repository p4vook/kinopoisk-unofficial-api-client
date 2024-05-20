from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.external_source_response import ExternalSourceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    page: Union[Unset, int] = 1,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.2/films/{id}/external_sources",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ExternalSourceResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ExternalSourceResponse.from_dict(response.json())

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
) -> Response[Union[Any, ExternalSourceResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
) -> Response[Union[Any, ExternalSourceResponse]]:
    """получить список сайтов, где можно посмотреть фильм по kinopoisk film id

     Возвращает список сайтов с пагинацией. Каждая страница содержит не более чем 20 рецензий.

    Args:
        id (int):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExternalSourceResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
) -> Optional[Union[Any, ExternalSourceResponse]]:
    """получить список сайтов, где можно посмотреть фильм по kinopoisk film id

     Возвращает список сайтов с пагинацией. Каждая страница содержит не более чем 20 рецензий.

    Args:
        id (int):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExternalSourceResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        page=page,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
) -> Response[Union[Any, ExternalSourceResponse]]:
    """получить список сайтов, где можно посмотреть фильм по kinopoisk film id

     Возвращает список сайтов с пагинацией. Каждая страница содержит не более чем 20 рецензий.

    Args:
        id (int):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExternalSourceResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
) -> Optional[Union[Any, ExternalSourceResponse]]:
    """получить список сайтов, где можно посмотреть фильм по kinopoisk film id

     Возвращает список сайтов с пагинацией. Каждая страница содержит не более чем 20 рецензий.

    Args:
        id (int):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExternalSourceResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            page=page,
        )
    ).parsed
