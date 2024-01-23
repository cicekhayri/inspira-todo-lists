from src.model.todo import Todo
from src.repository.todo_repository import TodoRepository


class TodoService:
    def __init__(self, todo_repository: TodoRepository):
        self._todo_repository = todo_repository

    def get_all_todos(self):
        return self._todo_repository.get_all_todos()

    def create_todo(self, title: str):
        todo = Todo(title=title)

        return self._todo_repository.create_todo(todo)

    def mark_complete(self, id: int) -> bool:
        return self._todo_repository.mark_complete(id)

    def delete_todo_by_id(self, id: int) -> bool:
        return self._todo_repository.delete_todo_by_id(id)
