import pytest


def test_add_task_success(empty_todo, capsys):
    empty_todo.add_task("  Новая задача  ")
    captured = capsys.readouterr()

    assert len(empty_todo.tasks) == 1
    assert empty_todo.tasks[0].title == "Новая задача"
    assert empty_todo.tasks[0].done is False
    assert "Задача добавлена" in captured.out


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


@pytest.mark.parametrize("index", [0, 3, -1])
def test_complete_task_invalid_index_negative(todo_with_tasks, capsys, index):
    todo_with_tasks.complete_task(index)
    captured = capsys.readouterr()

    assert todo_with_tasks.tasks[0].done is False
    assert todo_with_tasks.tasks[1].done is False
    assert "Нет задачи с номером" in captured.out