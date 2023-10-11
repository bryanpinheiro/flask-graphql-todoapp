# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)


def handle_session(func):
    def wrapper(self, *args, **kwargs):
        session = DBSession()
        try:
            result = func(self, session, *args, **kwargs)
            session.commit()
            return result
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    return wrapper
