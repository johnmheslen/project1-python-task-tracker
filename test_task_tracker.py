
import unittest
import os
import json
from unittest.mock import patch, mock_open
from datetime import datetime

# This is a bit of a hack to make sure we can import the task_tracker module
# since it's not installed as a package.
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import task_tracker

class TestTaskTracker(unittest.TestCase):

    def setUp(self):
        """Set up a fresh tasks list for each test."""
        self.tasks = []

    def test_add_task(self):
        """Test adding a new task."""
        with patch('builtins.input', side_effect=['Test task', 'high', 'n']), \
             patch('task_tracker.save_tasks', return_value=True):
            task_tracker.add_task(self.tasks)
            self.assertEqual(len(self.tasks), 1)
            self.assertEqual(self.tasks[0]['description'], 'Test task')
            self.assertEqual(self.tasks[0]['priority'], 'high')
            self.assertFalse(self.tasks[0]['completed'])

    def test_add_task_with_due_date(self):
        """Test adding a new task with a due date."""
        future_date = datetime.now().strftime("%Y-%m-%d")
        with patch('builtins.input', side_effect=['Test task with due date', 'medium', 'y', future_date]), \
             patch('task_tracker.save_tasks', return_value=True):
            task_tracker.add_task(self.tasks)
            self.assertEqual(len(self.tasks), 1)
            self.assertEqual(self.tasks[0]['due_date'], future_date)

    def test_mark_complete(self):
        """Test marking a task as complete."""
        self.tasks = [{'id': 1, 'description': 'Test task', 'completed': False, 'priority': 'low', 'created_at': '2025-07-31 12:00:00'}]
        with patch('builtins.input', return_value='1'), \
             patch('task_tracker.save_tasks', return_value=True), \
             patch('task_tracker.view_pending_tasks'): # Mock view_pending_tasks to avoid printing during tests
            task_tracker.mark_complete(self.tasks)
            self.assertTrue(self.tasks[0]['completed'])
            self.assertIn('completed_at', self.tasks[0])

    def test_delete_task(self):
        """Test deleting a task."""
        self.tasks = [{'id': 1, 'description': 'Test task', 'completed': False, 'priority': 'low', 'created_at': '2025-07-31 12:00:00'}]
        with patch('builtins.input', side_effect=['1', 'y']), \
             patch('task_tracker.save_tasks', return_value=True), \
             patch('task_tracker.view_tasks'): # Mock view_tasks to avoid printing during tests
            task_tracker.delete_task(self.tasks)
            self.assertEqual(len(self.tasks), 0)

    def test_search_tasks(self):
        """Test searching for a task."""
        self.tasks = [
            {'id': 1, 'description': 'First test task', 'completed': False, 'priority': 'low', 'created_at': '2025-07-31 12:00:00', 'due_date': None},
            {'id': 2, 'description': 'Second test task', 'completed': False, 'priority': 'medium', 'created_at': '2025-07-31 12:01:00', 'due_date': None},
            {'id': 3, 'description': 'Another item', 'completed': False, 'priority': 'high', 'created_at': '2025-07-31 12:02:00', 'due_date': None}
        ]
        with patch('builtins.input', return_value='test'), \
             patch('builtins.print') as mock_print:
            task_tracker.search_tasks(self.tasks)
            # Check that the correct number of "found" messages are printed
            self.assertEqual(mock_print.call_count, 11)


    def test_load_tasks_file_not_found(self):
        """Test loading tasks when the file does not exist."""
        with patch('os.path.exists', return_value=False):
            tasks = task_tracker.load_tasks()
            self.assertEqual(tasks, [])

    def test_load_tasks_file_corrupted(self):
        """Test loading tasks from a corrupted JSON file."""
        with patch('os.path.exists', return_value=True), \
             patch('builtins.open', mock_open(read_data='invalid json')), \
             patch('builtins.print') as mock_print:
            tasks = task_tracker.load_tasks()
            self.assertEqual(tasks, [])
            mock_print.assert_called_with("Error: Tasks file is corrupted. Starting with empty task list.")

    def test_save_tasks(self):
        """Test saving tasks to a file."""
        m = mock_open()
        with patch('builtins.open', m):
            task_tracker.save_tasks(self.tasks)
            m.assert_called_once_with(task_tracker.TASKS_FILE, 'w')
            handle = m()
            handle.write.assert_called_once_with(json.dumps(self.tasks, indent=4))

if __name__ == '__main__':
    unittest.main()
