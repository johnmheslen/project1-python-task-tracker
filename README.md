# Task Tracker

A simple command-line task tracker application written in Python. This tool provides a menu-driven interface for managing daily tasks, with data persisted to a JSON file.

## Features

- **Add Tasks**: Add new tasks with a description, priority (low, medium, high), and an optional due date.
- **View Tasks**: View all tasks, or filter by "completed" or "pending" status.
- **Mark as Complete**: Mark tasks as completed, which records the completion timestamp.
- **Delete Tasks**: Remove tasks from the list.
- **Data Persistence**: Tasks are saved to a `tasks.json` file, so your data is not lost when you close the application.
- **Due Dates**: Optionally add a due date to your tasks. The application will validate that the date is in the correct format (YYYY-MM-DD) and is not in the past.

## How to Run

To run the application, you need Python 3.x. No external libraries are required.

```bash
python3 task_tracker.py
```

## Data Format

Tasks are stored in `tasks.json` as an array of JSON objects. Each task has the following structure:

```json
[
    {
        "id": 1,
        "description": "This is an example task.",
        "completed": false,
        "created_at": "2025-07-30 12:00:00",
        "priority": "high",
        "due_date": "2025-08-15",
        "completed_at": null
    }
]
```

## Key Components

- `load_tasks()`: Loads tasks from `tasks.json`. Handles cases where the file doesn't exist or is corrupted.
- `save_tasks()`: Saves the current list of tasks to `tasks.json`.
- `add_task()`: Prompts the user for task details (description, priority, due date) and adds a new task.
- `view_tasks()`: Displays tasks. Prompts the user to view all, completed, or pending tasks.
- `mark_complete()`: Marks a specific task as complete and records the completion time.
- `delete_task()`: Deletes a task and re-assigns task IDs to maintain a consistent sequence.
- `main()`: The main function that runs the application's main loop and presents the user with the menu.
