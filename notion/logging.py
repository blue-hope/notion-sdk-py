import logging
from enum import Enum

class LogLevel(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARN = logging.WARN
    ERROR = logging.ERROR


def makeConsoleLogger(level: LogLevel) -> logging.Logger:
    logger = logging.getLogger()
    logger.setLevel(level)
