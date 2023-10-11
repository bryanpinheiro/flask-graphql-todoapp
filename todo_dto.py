# todo_dto.py

from models import Todo
from typing import Dict, Union, Type


class TodoDTO:
    def __init__(self, todo: Type[Todo]):
        self.id = todo.id
        self.title = todo.title
        self.completed = todo.completed

    def as_dict(self) -> Dict[str, Union[int, str, bool]]:
        return self.__dict__
