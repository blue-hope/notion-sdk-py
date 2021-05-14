from dataclasses import dataclass
from typing import Any, Generic, Literal, TypeVar, Union

T = TypeVar("T")


@dataclass
class PaginationParameters:
    start_cursor: str
    page_size: int


@dataclass
class Database:
    id: str
    created_time: str
    last_edited_time: str
    title: list[Any]
    properties: dict[str, Any]
    object: Literal["database"]


@dataclass
class PaginatedList(Generic[T]):
    object: Literal["list"]
    results: list[T]
    has_more: bool
    next_cursor: Union[str, None]
