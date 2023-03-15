class Task:
    def __init__(self, id, title, status=False):
        self.id = int(id)
        self.title = title
        self.status = status
