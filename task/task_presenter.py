from task import Status, TaskManager


class TaskPresenter:
    def print(self):
        """Print all tasks with their status and id."""
        tasks = TaskManager().get_tasks()
        if len(tasks) == 0:
            print("No tasks")
            return

        for task in tasks:
            task_status = "[ ]"
            if task.status == Status.DONE:
                task_status = "✅"
            print(f"{task_status} - {task.id} - {task.title}")
