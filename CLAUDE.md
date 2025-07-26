# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple command-line task tracker application written in Python. The application provides a menu-driven interface for managing daily tasks with persistence to JSON.

## Architecture

- **Single-file application**: `task_tracker.py` contains all functionality
- **Data persistence**: Tasks stored in `tasks.json` using JSON format
- **Task structure**: Each task has id, description, completed status, created_at timestamp, an optional due date timestamp, and an optional completed_at timestamp

## Key Components

- `load_tasks()`: Handles JSON file reading with error handling for corrupted files
- `save_tasks()`: Persists tasks to JSON with proper exception handling
- `add_task()`: Creates new tasks with auto-incrementing IDs and timestamps
- `mark_complete()`: Updates task status and adds completion timestamp
- `delete_task()`: Removes tasks and reassigns IDs to maintain sequence
- `view_tasks()`: Displays tasks with status indicators and summary statistics

## Running the Application

```bash
python3 task_tracker.py
```

The application requires Python 3.x and uses only standard library modules (json, os, datetime).

## Data Format

Tasks are stored in `tasks.json` as an array of objects:
```json
[
    {
        "id": 1,
        "description": "Task description",
        "completed": false,
        "created_at": "2025-07-24 00:51:41",
        "due_date": "
        "completed_at": "2025-07-24 10:30:00"  // only present when completed
    }
]
```

## Testing

The application has no formal test suite. Manual testing through the menu interface is used to verify functionality.