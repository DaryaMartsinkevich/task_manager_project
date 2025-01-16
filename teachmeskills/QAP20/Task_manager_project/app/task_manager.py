class TaskManager:
    def __init__(self):
        """Инициализация менеджера задач с пустым списком."""
        self.tasks = []

    def add_task(self, name, priority="normal"):
        """
        Добавляет задачу в список.

        :param name: Название задачи
        :param priority: Приоритет задачи ('low', 'normal', 'high')
        :return: Словарь с добавленной задачей
        """
        if priority not in ["low", "normal", "high"]:
            raise ValueError("Приоритет должен быть 'low', 'normal' или 'high'")
        task = {"name": name, "priority": priority, "completed": False}
        self.tasks.append(task)
        return task

    def list_tasks(self):
        """Возвращает список всех задач."""
        return self.tasks

    def mark_task_completed(self, name):
        """
        Отмечает задачу как выполненную.

        :param name: Название задачи
        :return: Обновленная задача
        """
        for task in self.tasks:
            if task["name"] == name:
                task["completed"] = True
                return task
        raise ValueError("Задача с таким названием не найдена")

    def remove_task(self, name):
        """
        Удаляет задачу из списка.

        :param name: Название задачи
        :return: Удаленная задача
        """
        for task in self.tasks:
            if task["name"] == name:
                self.tasks.remove(task)
                return task
        raise ValueError("Задача с таким названием не найдена")
