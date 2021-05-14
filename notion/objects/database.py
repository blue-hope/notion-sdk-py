from typing import Dict, Literal, TypedDict
from notion.objects.property import PropertyObject
from notion.objects.richtext import RichTextObject


class DatabaseObject(object):
    object: Literal["database"]
    id: str
    created_time: str
    last_edited_time: str
    title: list[RichTextObject]
    properties: Dict[str, PropertyObject]
