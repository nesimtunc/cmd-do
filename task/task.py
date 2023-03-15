from task.status import Status


class Task:
    """A task with a title and status."""
    def __init__(self, id: int, title: str, status: Status = Status.TODO):
        self.id = int(id)
        self.title = title
        self.status = status
