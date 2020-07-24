from typing import Callable, List, Type

from pydantic import BaseModel  # pylint: disable=no-name-in-module

from .dispatcher import BaseDispatcher
from .event import BaseEvent
from .namespace import Namespace
from .decorater import Decorater


class Listener(BaseModel):
    callable: Callable
    namespace: Namespace
    inline_dispatchers: List[BaseDispatcher] = []
    headless_decoraters: List[Decorater] = []
    priority: int = 0
    listening_events: List[Type[BaseEvent]]

    class Config:
        arbitrary_types_allowed = True
