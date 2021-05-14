from dataclasses import dataclass
from notion.Client import Method
from typing import Literal
from notion.api_types import Database, PaginatedList, PaginationParameters


@dataclass
class DatabasesListPathParameters:
    pass


@dataclass
class DatabasesListQueryParameters(PaginationParameters):
    pass


@dataclass
class DatabasesListBodyParameters:
    pass


@dataclass
class DatabasesListParameters(
    DatabasesListPathParameters,
    DatabasesListQueryParameters,
    DatabasesListBodyParameters,
):
    pass


@dataclass
class DatabasesListResponse(PaginatedList[Database]):
    pass


@dataclass
class DatabasesList:
    method = Method.GET.value
    pathParams = []
    queryParams = ["start_cursor", "page_size"]
    bodyParams = []
    path = "databases"
