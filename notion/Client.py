from enum import Enum
import logging
from notion.errors import build_request_error
import httpx
from typing import Union
from dataclasses import dataclass
from notion.logging import LogLevel, make_console_logger


@dataclass
class ClientOptions:
    auth: str
    timeout_ms: int
    base_url: str
    log_level: LogLevel
    logger: logging.Logger
    notion_version: str


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
    auth: str


class Client:
    DEFAULT_NOTION_VERSION = "2021-05-13"

    def __init__(self, options: Union[ClientOptions, dict]):
        self.auth = options.auth
        self.logLevel = options.logLevel or LogLevel.WARN
        self.logger = options.logger or make_console_logger(self.logLevel)

        prefix_url = (options.base_url or "https://api.notion.com") + "/v1/"
        timeout = options.timeout_ms or 60_000
        notion_version = options.notion_version or Client.DEFAULT_NOTION_VERSION

        transport = httpx.HTTPTransport(retries=0)
        self.http = httpx.AsyncClient(
            base_url=prefix_url,
            timeout=timeout,
            headers={
                "Notion-Version": notion_version,
                "user-agent": "notion-sdk-py/0.0.1",
            },
            transport=transport,
        )

    def _auth_as_header(self, auth: str) -> httpx.Headers:
        headers: httpx.Headers = {}
        auth_header_value = auth or self.auth
        if auth_header_value is not None:
            headers["Authorization"] = f"Bearer {auth_header_value}"
        return headers

    async def request(self, request_parameters: RequestParameters):
        try:
            response = await self.http.build_request(
                method=request_parameters.method,
                path=request_parameters.path,
                data=request_parameters.body,
                params=request_parameters.query,
                headers=self._auth_as_header(request_parameters.auth),
            )
            response.raise_for_status()
            return response
        except Exception as e:
            request_error = build_request_error(e)
            if request_error is None:
                raise e

            raise request_error

    def prepare_credentials(self):
        self.HEADERS["Authorization"] = f"Bearer {self.auth}"

    def retrieve_database(self, database_id):
        url = f"{self.API_ENDPOINT}/databases/{database_id}"
        req = self.session.get(url)
        return req.json()

    def query_database(self, database_id, data):
        url = f"{self.API_ENDPOINT}/databases/{database_id}/query"
        req = self.session.post(url, data=data)
        return req.json()

    def list_databases(self, params):
        url = f"{self.API_ENDPOINT}/databases"
        req = self.session.get(url, params=params)
        return req.json()

    def retrieve_page(self, page_id):
        url = f"{self.API_ENDPOINT}/pages/{page_id}"
        req = self.session.get(url)
        return req.json()

    def create_page(self, data):
        url = f"{self.API_ENDPOINT}/pages"
        req = self.session.post(url, data=data)
        return req.json()

    def update_page(self, page_id, data):
        url = f"{self.API_ENDPOINT}/pages/{page_id}"
        req = self.session.patch(url, data=data)
        return req.json()

    def retrieve_block(self, block_id, params):
        url = f"{self.API_ENDPOINT}/blocks/{block_id}/children"
        req = self.session.get(url, params=params)
        return req.json()

    def append_block(self, block_id, data):
        url = f"{self.API_ENDPOINT}/blocks/{block_id}/children"
        req = self.session.patch(url, data=data)
        return req.json()

    def retrieve_user(self, user_id):
        url = f"{self.API_ENDPOINT}/users/{user_id}"
        req = self.session.get(url)
        return req.json()

    def list_users(self):
        url = f"{self.API_ENDPOINT}/users"
        req = self.session.get(url)
        return req.json()

    def search(self, data):
        url = f"{self.API_ENDPOINT}/search"
        req = self.session.post(url, data=data)
        return req.json()
