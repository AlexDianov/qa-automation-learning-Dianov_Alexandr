from todolist import Task


def test_task_str_not_done():
    task = Task("Тестовая задача")
    assert str(task) == "[ ] Тестовая задача"


def test_task_str_done():
    task = Task("Тестовая задача", done=True)
    assert str(task) == "[x] Тестовая задача"
