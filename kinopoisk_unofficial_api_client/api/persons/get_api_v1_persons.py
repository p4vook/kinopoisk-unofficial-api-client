from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.person_by_name_response import PersonByNameResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: str,
    page: Union[Unset, int] = 1,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["name"] = name

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/persons",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PersonByNameResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PersonByNameResponse.from_dict(response.json())

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
) -> Response[Union[Any, PersonByNameResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    name: str,
    page: Union[Unset, int] = 1,
) -> Response[Union[Any, PersonByNameResponse]]:
    """поиск актеров, режиссеров и т.д. по имени

     Одна страница может содержать до 50 элементов в items.

    Args:
        name (str):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PersonByNameResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    name: str,
    page: Union[Unset, int] = 1,
) -> Optional[Union[Any, PersonByNameResponse]]:
    """поиск актеров, режиссеров и т.д. по имени

     Одна страница может содержать до 50 элементов в items.

    Args:
        name (str):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PersonByNameResponse]
    """

    return sync_detailed(
        client=client,
        name=name,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    name: str,
    page: Union[Unset, int] = 1,
) -> Response[Union[Any, PersonByNameResponse]]:
    """поиск актеров, режиссеров и т.д. по имени

     Одна страница может содержать до 50 элементов в items.

    Args:
        name (str):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PersonByNameResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    name: str,
    page: Union[Unset, int] = 1,
) -> Optional[Union[Any, PersonByNameResponse]]:
    """поиск актеров, режиссеров и т.д. по имени

     Одна страница может содержать до 50 элементов в items.

    Args:
        name (str):
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PersonByNameResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            page=page,
        )
    ).parsed
