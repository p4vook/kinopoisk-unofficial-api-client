from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v22_films_id_images_type import GetApiV22FilmsIdImagesType
from ...models.image_response import ImageResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    type: Union[Unset, GetApiV22FilmsIdImagesType] = GetApiV22FilmsIdImagesType.STILL,
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
        "url": f"/api/v2.2/films/{id}/images",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ImageResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ImageResponse.from_dict(response.json())

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
) -> Response[Union[Any, ImageResponse]]:
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
    type: Union[Unset, GetApiV22FilmsIdImagesType] = GetApiV22FilmsIdImagesType.STILL,
    page: Union[Unset, int] = 1,
) -> Response[Union[Any, ImageResponse]]:
    """получить изображения(кадры, постеры, фан-арты, обои и т.д.) связанные с фильмом по kinopoisk film id

     Данный эндпоинт возвращает изображения связанные с фильмом с пагинацией. Каждая страница содержит
    <b>не более чем 20 фильмов</b>.</br> Доступные изображения:</br> <ul> <li>STILL - кадры</li>
    <li>SHOOTING - изображения со съемок</li> <li>POSTER - постеры</li> <li>FAN_ART - фан-арты</li>
    <li>PROMO - промо</li> <li>CONCEPT - концепт-арты</li> <li>WALLPAPER - обои</li> <li>COVER -
    обложки</li> <li>SCREENSHOT - скриншоты</li> </ul>

    Args:
        id (int):
        type (Union[Unset, GetApiV22FilmsIdImagesType]):  Default:
            GetApiV22FilmsIdImagesType.STILL.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImageResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        type=type,
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
    type: Union[Unset, GetApiV22FilmsIdImagesType] = GetApiV22FilmsIdImagesType.STILL,
    page: Union[Unset, int] = 1,
) -> Optional[Union[Any, ImageResponse]]:
    """получить изображения(кадры, постеры, фан-арты, обои и т.д.) связанные с фильмом по kinopoisk film id

     Данный эндпоинт возвращает изображения связанные с фильмом с пагинацией. Каждая страница содержит
    <b>не более чем 20 фильмов</b>.</br> Доступные изображения:</br> <ul> <li>STILL - кадры</li>
    <li>SHOOTING - изображения со съемок</li> <li>POSTER - постеры</li> <li>FAN_ART - фан-арты</li>
    <li>PROMO - промо</li> <li>CONCEPT - концепт-арты</li> <li>WALLPAPER - обои</li> <li>COVER -
    обложки</li> <li>SCREENSHOT - скриншоты</li> </ul>

    Args:
        id (int):
        type (Union[Unset, GetApiV22FilmsIdImagesType]):  Default:
            GetApiV22FilmsIdImagesType.STILL.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ImageResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        type=type,
        page=page,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, GetApiV22FilmsIdImagesType] = GetApiV22FilmsIdImagesType.STILL,
    page: Union[Unset, int] = 1,
) -> Response[Union[Any, ImageResponse]]:
    """получить изображения(кадры, постеры, фан-арты, обои и т.д.) связанные с фильмом по kinopoisk film id

     Данный эндпоинт возвращает изображения связанные с фильмом с пагинацией. Каждая страница содержит
    <b>не более чем 20 фильмов</b>.</br> Доступные изображения:</br> <ul> <li>STILL - кадры</li>
    <li>SHOOTING - изображения со съемок</li> <li>POSTER - постеры</li> <li>FAN_ART - фан-арты</li>
    <li>PROMO - промо</li> <li>CONCEPT - концепт-арты</li> <li>WALLPAPER - обои</li> <li>COVER -
    обложки</li> <li>SCREENSHOT - скриншоты</li> </ul>

    Args:
        id (int):
        type (Union[Unset, GetApiV22FilmsIdImagesType]):  Default:
            GetApiV22FilmsIdImagesType.STILL.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImageResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        type=type,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, GetApiV22FilmsIdImagesType] = GetApiV22FilmsIdImagesType.STILL,
    page: Union[Unset, int] = 1,
) -> Optional[Union[Any, ImageResponse]]:
    """получить изображения(кадры, постеры, фан-арты, обои и т.д.) связанные с фильмом по kinopoisk film id

     Данный эндпоинт возвращает изображения связанные с фильмом с пагинацией. Каждая страница содержит
    <b>не более чем 20 фильмов</b>.</br> Доступные изображения:</br> <ul> <li>STILL - кадры</li>
    <li>SHOOTING - изображения со съемок</li> <li>POSTER - постеры</li> <li>FAN_ART - фан-арты</li>
    <li>PROMO - промо</li> <li>CONCEPT - концепт-арты</li> <li>WALLPAPER - обои</li> <li>COVER -
    обложки</li> <li>SCREENSHOT - скриншоты</li> </ul>

    Args:
        id (int):
        type (Union[Unset, GetApiV22FilmsIdImagesType]):  Default:
            GetApiV22FilmsIdImagesType.STILL.
        page (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ImageResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            type=type,
            page=page,
        )
    ).parsed
