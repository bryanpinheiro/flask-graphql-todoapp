# todo_dao.py
from custom_exceptions import NotFoundException
from database import handle_session
from models import Todo
from todo_dto import TodoDTO
from sqlalchemy.orm.session import Session
from typing import List, Union


class TodoDAO:
    def __init__(self):
        pass  # No need to initialize the session here

    @handle_session
    def get_all_todos(self, session: Session) -> List[TodoDTO]:
        todos = session.query(Todo).all()

        for todo in todos:
            session.expunge(todo)

        todo_list = [TodoDTO(todo) for todo in todos]
        return todo_list

    @handle_session
    def create_todo(self, session: Session, title: str) -> None:
        new_todo = Todo(title=title, completed=False)
        session.add(new_todo)

    @handle_session
    def get_todo_by_id(self, session, todo_id) -> TodoDTO:
        raw_todo = session.query(Todo).filter_by(id=todo_id).first()

        if raw_todo is None:
            raise NotFoundException()

        session.expunge(raw_todo)
        todo = TodoDTO(raw_todo)
        return todo

    @handle_session
    def update_todo(self, session, todo_id, data) -> None:
        todo = session.query(Todo).filter_by(id=todo_id).first()

        if todo is None:
            raise NotFoundException()

        for key, value in data.items():
            setattr(todo, key, value)

    @handle_session
    def delete_todo(self, session, todo_id) -> None:
        todo = session.query(Todo).filter_by(id=todo_id).first()

        if todo is None:
            raise NotFoundException()

        session.delete(todo)
