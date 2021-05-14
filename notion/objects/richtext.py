from enum import Enum
from notion.objects.user import UserObject
from typing import Optional


class RichTextObject(object):
    class RichTextType(Enum):
        TEXT = "text"
        MENTION = "mention"
        EQUATION = "equation"

    class Annotations(object):
        class AnnotationsColor(Enum):
            DEFAULT = "default"
            GRAY = "gray"
            BROWN = "brown"
            ORANGE = "orange"
            YELLOW = "yellow"
            GREEN = "green"
            BLUE = "blue"
            PURPLE = "purple"
            PINK = "pink"
            RED = "red"
            GRAY_BACKGROUND = "gray_background"
            BROWN_BACKGROUND = "brown_background"
            ORANGE_BACKGROUND = "orange_background"
            YELLOW_BACKGROUND = "yellow_background"
            GREEN_BACKGROUND = "green_background"
            BLUE_BACKGROUND = "blue_background"
            PURPLE_BACKGROUND = "purple_background"
            PINK_BACKGROUND = "pink_background"
            RED_BACKGROUND = "red_background"

        bold: bool
        italic: bool
        strikethrough: bool
        underline: bool
        code: bool
        color: AnnotationsColor

    class TextObject(object):
        class Link(object):
            type: str = "url"
            url: str

        content: str
        link: Optional[Link]

    class MentionObject(object):
        class MentionType(Enum):
            USER = "user"
            PAGE = "page"
            DATABASE = "database"
            DATE = "date"

        type: MentionType
        user: UserObject
        page: str  # FIXME
        database: str  # FIXME
        date: str  # FIXME

    class EquationObject(object):
        expression: str

    type: RichTextType
    annotations: Annotations
    href: Optional[str]
    plain_text: str
    text: TextObject
    mention: MentionObject
    equation: EquationObject