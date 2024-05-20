from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_response import ApiKeyResponse
from ...types import Response


def _get_kwargs(
    api_key: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/api_keys/{api_key}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiKeyResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiKeyResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ApiKeyResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    api_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ApiKeyResponse]]:
    """получить данные об api key

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiKeyResponse]]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    api_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ApiKeyResponse]]:
    """получить данные об api key

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiKeyResponse]
    """

    return sync_detailed(
        api_key=api_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    api_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ApiKeyResponse]]:
    """получить данные об api key

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiKeyResponse]]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    api_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ApiKeyResponse]]:
    """получить данные об api key

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiKeyResponse]
    """

    return (
        await asyncio_detailed(
            api_key=api_key,
            client=client,
        )
    ).parsed
