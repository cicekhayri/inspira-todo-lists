from inspira.logging import log
from sqlalchemy.exc import SQLAlchemyError

from database import db_session
from src.model.todo import Todo


class TodoRepository:

    def get_all_todos(self):
        return db_session.query(Todo).all()

    def get_todo_by_id(self, id: int):
        return db_session.query(Todo).filter_by(id=id).first()

    def delete_todo_by_id(self, id: int):
        try:
            todo = self.get_todo_by_id(id)
            db_session.delete(todo)
            db_session.commit()
            return True
        except SQLAlchemyError as e:
            db_session.rollback()
            log.error(f"Error deleting todo: {e}")
            return False

    def mark_complete(self, id: int):
        try:
            todo = self.get_todo_by_id(id)
            todo.completed = True

            db_session.commit()
            return True
        except SQLAlchemyError as e:
            db_session.rollback()
            log.error(f"Error marking todo completed: {e}")
            return False

    def create_todo(self, todo: Todo):
        try:
            db_session.add(todo)
            db_session.commit()
            return True
        except SQLAlchemyError as e:
            db_session.rollback()
            log.error(f"Error creating todo: {e}")
            return False
