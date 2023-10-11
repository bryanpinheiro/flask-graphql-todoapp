# todo_dao.py

from custom_exceptions import NotFoundException
from database import handle_session
from models import Todo
from sqlalchemy.orm.session import Session
from typing import List, Optional


class TodoDAO:
    def __init__(self):
        pass  # No need to initialize the session here

    @handle_session
    def get_all_todos(self, session: Session) -> List[Todo]:
        todos = session.query(Todo).all()

        for todo in todos:
            session.expunge(todo)

        return todos

    @handle_session
    def create_todo(self, session: Session, title: str) -> None:
        new_todo = Todo(title=title, completed=False)
        session.add(new_todo)

    @handle_session
    def get_todo_by_id(self, session, todo_id) -> Optional[Todo]:
        todo = session.query(Todo).filter_by(id=todo_id).first()

        if todo:
            session.expunge(todo)
            return todo
        else:
            return None

    @handle_session
    def update_todo(self, session, todo_id, data) -> None:
        todo = session.query(Todo).filter_by(id=todo_id).first()

        for key, value in data.items():
            setattr(todo, key, value)

    @handle_session
    def delete_todo(self, session, todo_id) -> None:
        todo = session.query(Todo).filter_by(id=todo_id).first()

        session.delete(todo)
