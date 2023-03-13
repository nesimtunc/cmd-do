import unittest
import tempfile
import os

from task import Task


class TaskTests(unittest.TestCase):

    def setUp(self):
        self.filename = tempfile.NamedTemporaryFile(delete=False).name
        self.task = Task(self.filename)

    def tearDown(self):
        os.unlink(self.filename)

    def test_task_creates_file_if_not_exists(self):
        self.assertTrue(os.path.exists(self.filename))

    def test_can_create_a_task(self):
        self.task.create("test task")

        with open(self.filename) as f:
            lines = f.readlines()
            assert len(lines) == 1
            assert lines[0] == "1,\"test task\",0"


    def _create_test_file(self, filename):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_file = os.path.join(self.temp_dir.name, filename)

        open(tempfile, "w").close()

