from inspira.decorators.http_methods import get, post, delete, put
from inspira.decorators.path import path
from inspira.responses import TemplateResponse
from inspira.requests import Request
from src.service.todo_service import TodoService


@path("/todos")
class TodoController:

    def __init__(self, todo_service: TodoService):
        self._todo_service = todo_service

    @get()
    async def index(self, request: Request):
        todos = self._todo_service.get_all_todos()

        context = {
            "todos": todos,
        }

        return TemplateResponse("index.html", context)

    @post("/create")
    async def create_todo(self, request: Request):
        body = await request.form()
        title = body['title']
        self._todo_service.create_todo(title)

        todos = self._todo_service.get_all_todos()

        context = {
            "todos": todos
        }
        return TemplateResponse("todo-list.html", context)


    @delete("/{id}")
    async def delete_todo(self, request: Request, id: int):
        self._todo_service.delete_todo_by_id(id)
        todos = self._todo_service.get_all_todos()

        context = {
            "todos": todos
        }
        return TemplateResponse("todo-list.html", context)

    @put("/{id}")
    async def mark_complete(self, request: Request, id: int):
        self._todo_service.mark_complete(id)
        todos = self._todo_service.get_all_todos()

        context = {
            "todos": todos
        }
        return TemplateResponse("todo-list.html", context)