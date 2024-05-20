from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.digital_release_response import DigitalReleaseResponse
from ...models.get_api_v21_films_releases_month import GetApiV21FilmsReleasesMonth
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    year: int,
    month: GetApiV21FilmsReleasesMonth,
    page: Union[Unset, int] = 1,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["year"] = year

    json_month = month.value
    params["month"] = json_month

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.1/films/releases",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DigitalReleaseResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DigitalReleaseResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.PAYMENT_REQUIRED:
        response_402 = cast(Any, None)
        return response_402
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DigitalReleaseResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    year: int,
    month: GetApiV21FilmsReleasesMonth,
    page: Union[Unset, int] = 1,
) -> Response[Union[Any, DigitalReleaseResponse]]:
    """получить список цифровых релизов

     Данный эндпоинт возвращает список цифровых релизов. Например
    https://www.kinopoisk.ru/comingsoon/digital/

    Args:
        year (int):
        month (GetApiV21FilmsReleasesMonth):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DigitalReleaseResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        month=month,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    year: int,
    month: GetApiV21FilmsReleasesMonth,
    page: Union[Unset, int] = 1,
) -> Optional[Union[Any, DigitalReleaseResponse]]:
    """получить список цифровых релизов

     Данный эндпоинт возвращает список цифровых релизов. Например
    https://www.kinopoisk.ru/comingsoon/digital/

    Args:
        year (int):
        month (GetApiV21FilmsReleasesMonth):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DigitalReleaseResponse]
    """

    return sync_detailed(
        client=client,
        year=year,
        month=month,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    year: int,
    month: GetApiV21FilmsReleasesMonth,
    page: Union[Unset, int] = 1,
) -> Response[Union[Any, DigitalReleaseResponse]]:
    """получить список цифровых релизов

     Данный эндпоинт возвращает список цифровых релизов. Например
    https://www.kinopoisk.ru/comingsoon/digital/

    Args:
        year (int):
        month (GetApiV21FilmsReleasesMonth):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DigitalReleaseResponse]]
    """

    kwargs = _get_kwargs(
        year=year,
        month=month,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    year: int,
    month: GetApiV21FilmsReleasesMonth,
    page: Union[Unset, int] = 1,
) -> Optional[Union[Any, DigitalReleaseResponse]]:
    """получить список цифровых релизов

     Данный эндпоинт возвращает список цифровых релизов. Например
    https://www.kinopoisk.ru/comingsoon/digital/

    Args:
        year (int):
        month (GetApiV21FilmsReleasesMonth):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DigitalReleaseResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            year=year,
            month=month,
            page=page,
        )
    ).parsed
