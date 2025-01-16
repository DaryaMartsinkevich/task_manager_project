from app.task_manager import TaskManager



def task_manager():
    return TaskManager()


def test_add_task():
    TaskManager = task_manager()
    task = TaskManager.add_task('Task 10', 'high')
    assert task["name"] == 'Task 10'
    assert task['priority'] == 'high'
    assert task['completed'] is False
    assert len(TaskManager.list_tasks()) == 1


def test_add_task_priority():
    TaskManager = task_manager()
    try:
        TaskManager.add_task("Task 10", "invalid")
    except ValueError as i:
        assert str(i) == "Приоритет должен быть 'low', 'normal' или 'high'"
    else:
        raise AssertionError("ValueError не был вызван при недопустимом приоритете")


def test_list_tasks():
    TaskManager = task_manager()
    task = TaskManager.add_task("Task 10", "high")
    task = TaskManager.add_task("Task 20", "low")
    tasks = TaskManager.list_tasks()
    assert len(tasks) == 2
    assert tasks[0]["name"] == "Task 10"
    assert tasks[1]["name"] == "Task 20"


def test_mark_task_completed():
    TaskManager = task_manager()
    TaskManager.add_task('Task 10')
    task = TaskManager.mark_task_completed("Task 10")
    assert task['completed'] is True
    assert task['name'] == 'Task 10'


def test_remove_task():
    """Тест успешного удаления задачи."""
    TaskManager = task_manager()
    TaskManager.add_task("Task 10")
    removed = TaskManager.remove_task("Task 10")
    assert removed["name"] == "Task 10", "Название удалённой задачи некорректно"
    assert removed not in TaskManager.list_tasks(), "Задача не была удалена из списка"
