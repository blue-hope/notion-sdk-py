import logging
import httpx
from enum import Enum
from dataclasses import dataclass
from typing import Any
from notion.errors import build_request_error
from notion._logging import LogLevel, make_console_logger


@dataclass
class ClientOptions:
    auth: str = None
    timeout_ms: int = 60_000
    base_url: str = "https://api.notion.com"
    log_level: LogLevel = LogLevel.WARN
    logger: logging.Logger = None
    notion_version: str = None


class Method(Enum):
    GET = "get"
    POST = "post"
    PATCH = "patch"


@dataclass
class RequestParameters:
    path: str
    method: Method
    query: dict
    body: dict
    auth: str = None


class Client:
    DEFAULT_NOTION_VERSION = "2021-05-13"

    def __init__(self, options: ClientOptions):
        self.auth = options.auth
        self.log_level = options.log_level
        self.logger = options.logger or make_console_logger(self.log_level)

        prefix_url = options.base_url + "/v1/"
        timeout = options.timeout_ms
        notion_version = options.notion_version or Client.DEFAULT_NOTION_VERSION

        self.http = httpx.AsyncClient(
            base_url=prefix_url,
            timeout=timeout,
            headers={
                "Notion-Version": notion_version,
                "user-agent": "notion-sdk-py/0.0.1",
            },
        )

    async def close(self):
        await self.http.aclose()

    def _auth_as_header(self, auth: str) -> httpx.Headers:
        headers: httpx.Headers = {}
        auth_header_value = auth or self.auth
        if auth_header_value is not None:
            headers["Authorization"] = f"Bearer {auth_header_value}"
        return headers

    async def request(self, request_parameters: RequestParameters):
        try:
            request = self.http.build_request(
                method=request_parameters.method,
                url=request_parameters.path,
                data=request_parameters.body,
                params=request_parameters.query,
                headers=self._auth_as_header(request_parameters.auth),
            )
            response = await self.http.send(request=request)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            request_error = build_request_error(e)
            if request_error is None:
                raise e

            raise request_error

    def log(self, level: LogLevel, message: str, extra_info: dict[str, Any]):
        if level >= self.log_level:
            self.logger.log(level, message, extra=extra_info)

    @property
    def blocks(self):
        from notion.apis import BlocksClient

        return BlocksClient(self)

    @property
    def databases(self):
        from notion.apis import DatabasesClient

        return DatabasesClient(self)

    @property
    def pages(self):
        from notion.apis import PagesClient

        return PagesClient(self)

    @property
    def users(self):
        from notion.apis import UsersClient

        return UsersClient(self)
