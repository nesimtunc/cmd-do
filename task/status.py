from enum import IntEnum, auto


class Status(IntEnum):
    """Status of a task."""
    TODO = auto()
    DOING = auto()
    DONE = auto()
