from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.video_response import VideoResponse
from ...types import Response


def _get_kwargs(
    id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.2/films/{id}/videos",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, VideoResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = VideoResponse.from_dict(response.json())

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
) -> Response[Union[Any, VideoResponse]]:
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
) -> Response[Union[Any, VideoResponse]]:
    """получить трейлеры,тизеры,видео для фильма по kinopoisk film id

     Данный эндпоинт возвращает трейлеры,тизеры,видео для фильма по kinopoisk film id. В данный момент
    доступно три site:  <br/> <ul><li>YOUTUBE - в этом случае <b>url</b> это просто ссылка на youtube
    видео.</li><li>YANDEX_DISK - в этом случае <b>url</b> это ссылка на yandex
    disk.</li><li>KINOPOISK_WIDGET - в этом случае <b>url</b> это ссылка на кинопоиск виджет. Например
    https://widgets.kinopoisk.ru/discovery/trailer/123573?onlyPlayer=1&autoplay=1&cover=1. Если вы
    хотите вставить этот виджет на вашу страницу, вы можете сделать следующее:  <br/><br/>&lt;script
    src=&quot;https://unpkg.com/@ungap/custom-elements-builtin&quot;&gt;&lt;/script&gt;<br/>&lt;script
    type=&quot;module&quot; src=&quot;https://unpkg.com/x-frame-
    bypass&quot;&gt;&lt;/script&gt;<br/>&lt;iframe is=&quot;x-frame-bypass&quot; src=&quot;https://widge
    ts.kinopoisk.ru/discovery/trailer/167560?onlyPlayer=1&amp;autoplay=1&amp;cover=1&quot;
    width=&quot;500&quot; height=&quot;500&quot;&gt;&lt;/iframe&gt;</li></ul>

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VideoResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, VideoResponse]]:
    """получить трейлеры,тизеры,видео для фильма по kinopoisk film id

     Данный эндпоинт возвращает трейлеры,тизеры,видео для фильма по kinopoisk film id. В данный момент
    доступно три site:  <br/> <ul><li>YOUTUBE - в этом случае <b>url</b> это просто ссылка на youtube
    видео.</li><li>YANDEX_DISK - в этом случае <b>url</b> это ссылка на yandex
    disk.</li><li>KINOPOISK_WIDGET - в этом случае <b>url</b> это ссылка на кинопоиск виджет. Например
    https://widgets.kinopoisk.ru/discovery/trailer/123573?onlyPlayer=1&autoplay=1&cover=1. Если вы
    хотите вставить этот виджет на вашу страницу, вы можете сделать следующее:  <br/><br/>&lt;script
    src=&quot;https://unpkg.com/@ungap/custom-elements-builtin&quot;&gt;&lt;/script&gt;<br/>&lt;script
    type=&quot;module&quot; src=&quot;https://unpkg.com/x-frame-
    bypass&quot;&gt;&lt;/script&gt;<br/>&lt;iframe is=&quot;x-frame-bypass&quot; src=&quot;https://widge
    ts.kinopoisk.ru/discovery/trailer/167560?onlyPlayer=1&amp;autoplay=1&amp;cover=1&quot;
    width=&quot;500&quot; height=&quot;500&quot;&gt;&lt;/iframe&gt;</li></ul>

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VideoResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, VideoResponse]]:
    """получить трейлеры,тизеры,видео для фильма по kinopoisk film id

     Данный эндпоинт возвращает трейлеры,тизеры,видео для фильма по kinopoisk film id. В данный момент
    доступно три site:  <br/> <ul><li>YOUTUBE - в этом случае <b>url</b> это просто ссылка на youtube
    видео.</li><li>YANDEX_DISK - в этом случае <b>url</b> это ссылка на yandex
    disk.</li><li>KINOPOISK_WIDGET - в этом случае <b>url</b> это ссылка на кинопоиск виджет. Например
    https://widgets.kinopoisk.ru/discovery/trailer/123573?onlyPlayer=1&autoplay=1&cover=1. Если вы
    хотите вставить этот виджет на вашу страницу, вы можете сделать следующее:  <br/><br/>&lt;script
    src=&quot;https://unpkg.com/@ungap/custom-elements-builtin&quot;&gt;&lt;/script&gt;<br/>&lt;script
    type=&quot;module&quot; src=&quot;https://unpkg.com/x-frame-
    bypass&quot;&gt;&lt;/script&gt;<br/>&lt;iframe is=&quot;x-frame-bypass&quot; src=&quot;https://widge
    ts.kinopoisk.ru/discovery/trailer/167560?onlyPlayer=1&amp;autoplay=1&amp;cover=1&quot;
    width=&quot;500&quot; height=&quot;500&quot;&gt;&lt;/iframe&gt;</li></ul>

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VideoResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, VideoResponse]]:
    """получить трейлеры,тизеры,видео для фильма по kinopoisk film id

     Данный эндпоинт возвращает трейлеры,тизеры,видео для фильма по kinopoisk film id. В данный момент
    доступно три site:  <br/> <ul><li>YOUTUBE - в этом случае <b>url</b> это просто ссылка на youtube
    видео.</li><li>YANDEX_DISK - в этом случае <b>url</b> это ссылка на yandex
    disk.</li><li>KINOPOISK_WIDGET - в этом случае <b>url</b> это ссылка на кинопоиск виджет. Например
    https://widgets.kinopoisk.ru/discovery/trailer/123573?onlyPlayer=1&autoplay=1&cover=1. Если вы
    хотите вставить этот виджет на вашу страницу, вы можете сделать следующее:  <br/><br/>&lt;script
    src=&quot;https://unpkg.com/@ungap/custom-elements-builtin&quot;&gt;&lt;/script&gt;<br/>&lt;script
    type=&quot;module&quot; src=&quot;https://unpkg.com/x-frame-
    bypass&quot;&gt;&lt;/script&gt;<br/>&lt;iframe is=&quot;x-frame-bypass&quot; src=&quot;https://widge
    ts.kinopoisk.ru/discovery/trailer/167560?onlyPlayer=1&amp;autoplay=1&amp;cover=1&quot;
    width=&quot;500&quot; height=&quot;500&quot;&gt;&lt;/iframe&gt;</li></ul>

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VideoResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
