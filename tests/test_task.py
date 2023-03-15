import unittest
import tempfile
import os

# Import Task and TaskManager from the task package
from task import Task, TaskManager

class TaskTests(unittest.TestCase):

    def setUp(self):
        self.filename = tempfile.NamedTemporaryFile().name
        self.taskManager = TaskManager(self.filename)

    def tearDown(self):
        os.unlink(self.filename)

    def test_task_creates_file_if_not_exists(self):
        self.assertTrue(os.path.exists(self.filename))

    def test_file_formatted_well(self):
        self.taskManager.create("test task")

        with open(self.filename) as f:
            lines = f.readlines()
            assert len(lines) == 1
            assert lines[0] == "1,\"test task\",0\n"

    def test_can_get_last_id(self):
        self.taskManager.create("test task")
        self.taskManager.create("test task 2")

        last_id = self.taskManager._get_last_id()
        assert last_id == 2

    def test_can_get_last_id_when_no_tasks(self):
        last_id = self.taskManager._get_last_id()
        assert last_id == 0

    def test_can_complete_a_task(self):
        self.taskManager.create("test task")
        self.taskManager.create("test task 2")

        self.taskManager.complete(1)

        tasks = self.taskManager.list()
        assert len(tasks) == 2
        assert tasks[0].id == 1
        assert tasks[0].title == "test task"
        assert tasks[0].status == "1"

    def test_can_list_tasks(self):
        self.taskManager.create("test task")
        self.taskManager.create("test task 2")

        tasks = self.taskManager.list()
        assert len(tasks) == 2

        assert tasks[0].id == 1
        assert tasks[0].title == "test task"
        assert tasks[0].status == "0"

        assert tasks[1].id == 2
        assert tasks[1].title == "test task 2"
        assert tasks[1].status == "0"

    def _create_test_file(self, filename):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_file = os.path.join(self.temp_dir.name, filename)

        open(tempfile, "w").close()

