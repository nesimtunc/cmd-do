import os

from .task import Task, Status


class TaskManager:
    """A class to manage tasks in a simple task management system."""

    def __init__(self, filename="tasks.txt"):
        self._filename = filename
        self._maybe_create_file()

    def _maybe_create_file(self):
        """Create a file if it doesn't exist."""
        if not os.path.exists(self._filename):
            with open(self._filename, "w") as f:
                f.close()

    def create(self, title):
        """Create a new task with a title."""
        last_id = self._get_last_id()
        new_id = last_id + 1
        with open(self._filename, "a") as f:
            f.write(self._format_task_for_file(
                Task(new_id, title)))

    def get_tasks(self):
        """Return a list of tasks."""
        tasks = []
        with open(self._filename) as f:
            for line in f.readlines():
                id, title, status = line.strip().split(',')
                title = title.replace('"', '').strip()
                tasks.append(Task(id, title, Status(int(status)))) 
        return tasks

    def complete(self, task_id):
        tasks = self.get_tasks()
        found = False
        for task in tasks:
            if task.id == task_id:
                task.status = Status.DONE
                found = True
                break

        if found:
            self._write_tasks_to_file(tasks)
        else:
            return None

    def get_task_by_id(self, id):
        """Return a task with a given id or None if not found."""
        tasks = self.get_tasks()
        for task in tasks:
            if task.id == id:
                return task

        return None

    def _write_tasks_to_file(self, tasks):
        """Write a list of tasks to the file."""
        with open(self._filename, "w") as f:
            for task in tasks:
                f.write(self._format_task_for_file(task))

    def _format_task_for_file(self, task):
        """Format a task for writing to a file."""
        return f"{task.id},\"{task.title}\",{task.status.value}\n"

    def _get_last_id(self):
        """Return the last id in the file or 0 if the file is empty."""
        with open(self._filename, "r") as f:
            lines = f.readlines()
            if len(lines) == 0:
                return 0

            last_line = lines[-1]
            last_id = last_line.split(',')[0]

            return int(last_id)
