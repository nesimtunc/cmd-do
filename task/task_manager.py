import os

from .task import Task

class TaskManager:
    
    def __init__(self, filename="tasks.txt"):
        self._filename = filename
        self._maybe_create_file()

    def _maybe_create_file(self):
        if not os.path.exists(self._filename):
            open(self._filename, "w").close()

    def create(self, title):
        last_id = self._get_last_id()
        new_id = last_id + 1
        with open(self._filename, "a") as f:
            f.write(f"{new_id},\"{title}\",0\n") # 0 means incomplete

    def list(self):
        tasks = []
        with open(self._filename) as f:
            for line in f.readlines():
                id, title, status = line.strip().split(',')
                title = title.replace('"', '')
                tasks.append(Task(id, title.strip(), status))

        return tasks
    
    def print(self):
        tasks = self.list()
        if len(tasks) == 0:
            print("No tasks")
            return     
        
        for task in tasks:
                task_status = "[ ]"
                if task.status.strip() == "1":
                    task_status = "✅"
                
                print(f"{task_status} - {task.id} - {task.title}")

    def complete(self, task_id):
        tasks = self.list()
        found = False
        for task in tasks:
            if task.id == task_id:
                task.status = "1"
                found = True
                break

        if found:
            self._write_tasks_to_file(tasks)
        else:
            return None

    def get_task_by_id(self, id):
        tasks = self.list()
        for task in tasks:
            if task.id == id: 
                return task
            
        return None

    def _write_tasks_to_file(self, tasks):
        with open(self._filename, "w") as f:
            for task in tasks:
                f.write(f"{task.id},{task.title},{task.status}\n")

    def _get_last_id(self):
        with open(self._filename, "r") as f:
            lines = f.readlines()
            if len(lines) == 0:
                return 0

            last_line = lines[-1]
            last_id = last_line.split(',')[0]

            return int(last_id)
    