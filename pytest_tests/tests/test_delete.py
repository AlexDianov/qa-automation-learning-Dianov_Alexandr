import pytest


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