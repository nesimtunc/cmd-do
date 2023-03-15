import unittest
import tempfile
import os

# Import Task and TaskManager from the task package
from task import TaskManager, Status


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
            assert lines[0] == f"1,\"test task\",{Status.TODO.value}\n"


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

        tasks = self.taskManager.get_tasks()
        assert len(tasks) == 2
        assert tasks[0].id == 1
        assert tasks[0].title == "test task"
        assert tasks[0].status == Status.DONE

    def test_can_list_tasks(self):
        self.taskManager.create("test task")
        self.taskManager.create("test task 2")

        tasks = self.taskManager.get_tasks()
        self.assertEqual(len(tasks), 2)

        self.assertEqual(tasks[0].id, 1)
        self.assertEqual(tasks[0].title, "test task")
        self.assertEqual(tasks[0].status, Status.TODO)

        self.assertEqual(tasks[1].id, 2)
        self.assertEqual(tasks[1].title, "test task 2")
        self.assertEqual(tasks[1].status, Status.TODO)
