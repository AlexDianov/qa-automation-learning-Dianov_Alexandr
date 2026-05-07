import pytest
from todolist import TodoList


@pytest.fixture
def empty_todo():
    return TodoList()


@pytest.fixture
def todo_with_tasks():
    todo = TodoList()
    todo.add_task("Купить хлеб")
    todo.add_task("Сделать ДЗ")
    return todo