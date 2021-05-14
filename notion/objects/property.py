from enum import Enum
from typing import Dict


class PropertyObject(object):
    class PropertyType(Enum):
        TITLE = "title"
        RICH_TEXT = "rich_text"
        NUMBER = "number"
        SELECT = "select"
        MULTI_SELECT = "multi_select"
        DATE = "date"
        PEOPLE = "people"
        FILE = "file"
        CHECKBOX = "checkbox"
        URL = "url"
        EMAIL = "email"
        PHONE_NUMBER = "phone_number"
        FORMULA = "formula"
        RELATION = "relation"
        ROLLUP = "rollup"
        CREATED_TIME = "created_time"
        CREATED_BY = "created_by"
        LAST_EDITED_TIME = "last_edited_time"
        LAST_EDITED_BY = "last_edited_by"

    class PropertyNumberFormat(Enum):
        NUMBER = "number"
        NUMBER_WITH_COMMAS = "number_with_commas"
        PERCENT = "percent"
        DOLLAR = "dollar"
        EURO = "euro"
        POUND = "pound"
        YEN = "yen"
        RUBLE = "ruble"
        RUPEE = "rupee"
        WON = "won"
        YUAN = "yuan"

    id: str
    type: PropertyType
    title: dict = {}
    rich_text: dict = {}
    number: Dict["format", PropertyNumberFormat]
