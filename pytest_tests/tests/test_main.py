import pytest
from todolist import Task, TodoList


@pytest.fixture
def empty_todo():
    return TodoList()


@pytest.fixture
def todo_with_tasks():
    todo = TodoList()
    todo.add_task("Купить хлеб")
    todo.add_task("Сделать ДЗ")
    return todo


def test_task_str_not_done():
    task = Task("Тестовая задача")
    assert str(task) == "[ ] Тестовая задача"


def test_task_str_done():
    task = Task("Тестовая задача", done=True)
    assert str(task) == "[x] Тестовая задача"


def test_add_task_success(empty_todo, capsys):
    empty_todo.add_task("  Новая задача  ")
    captured = capsys.readouterr()

    assert len(empty_todo.tasks) == 1
    assert empty_todo.tasks[0].title == "Новая задача"
    assert empty_todo.tasks[0].done is False
    assert "Задача добавлена" in captured.out

#Негатив
@pytest.mark.parametrize("title", ["", "   ", "\n", "\t"])
def test_add_task_empty_title_negative(empty_todo, capsys, title):
    empty_todo.add_task(title)
    captured = capsys.readouterr()

    assert len(empty_todo.tasks) == 0
    assert "Нельзя добавить пустую задачу!" in captured.out


def test_complete_task_success(todo_with_tasks, capsys):
    todo_with_tasks.complete_task(1)
    captured = capsys.readouterr()

    assert todo_with_tasks.tasks[0].done is True
    assert "отмечена как выполненная" in captured.out

#Негатив
@pytest.mark.parametrize("index", [0, 3, -1])
def test_complete_task_invalid_index_negative(todo_with_tasks, capsys, index):
    todo_with_tasks.complete_task(index)
    captured = capsys.readouterr()

    assert todo_with_tasks.tasks[0].done is False
    assert todo_with_tasks.tasks[1].done is False
    assert "Нет задачи с номером" in captured.out

#Негатив
@pytest.mark.parametrize("index", [0, 5, -2])
def test_delete_task_invalid_index_negative(todo_with_tasks, capsys, index):
    todo_with_tasks.delete_task(index)
    captured = capsys.readouterr()

    assert len(todo_with_tasks.tasks) == 2
    assert "Нет задачи с номером" in captured.out


def test_delete_task_success(todo_with_tasks, capsys):
    todo_with_tasks.delete_task(1)
    captured = capsys.readouterr()

    assert len(todo_with_tasks.tasks) == 1
    assert todo_with_tasks.tasks[0].title == "Сделать ДЗ"
    assert "удалена" in captured.out