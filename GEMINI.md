# GEMINI.md

This file provides guidance and context for the Gemini CLI agent when working with this repository. It outlines project structure, key commands, and development workflows to ensure efficient and consistent collaboration.

## Project Overview

This is a simple command-line task tracker application written in Python. It uses a menu-driven interface to manage tasks and persists them to a `tasks.json` file. The application is self-contained in `task_tracker.py` and uses only the Python standard library.

## Core Commands

- **Run the application**: `python3 task_tracker.py`
- **Check for tracked files**: `git status`
- **Review recent changes**: `git log -n 5 --oneline`
- **List project files**: `ls -F`

*Note: This project does not currently have an automated test suite, linter, or code formatter. Verification should be done by running the application and manually testing the functionality.*

## Development Workflow

When asked to modify the codebase (e.g., add a feature, fix a bug), the following workflow should be used:

1.  **Understand**: Use `read_file` on `task_tracker.py` and `todo.md` to understand the current implementation and the desired changes. Use `git log` to understand recent changes.
2.  **Plan**: Formulate a clear, step-by-step plan. For example: "1. Add a new function to handle searching. 2. Add a new menu option in `show_menu()`. 3. Update the `main()` loop to call the new function."
3.  **Implement**: Use the `replace` or `write_file` tools to modify `task_tracker.py`. Ensure changes are consistent with the existing code style.
4.  **Verify**: Run `python3 task_tracker.py` and manually test the new functionality to confirm it works as expected and has not introduced any regressions.

## Key Files & Components

- **`task_tracker.py`**: The single source file containing all application logic.
    - `main()`: The main application loop and entry point.
    - `show_menu()`: Displays the main menu.
    - `load_tasks()` / `save_tasks()`: Handles reading from and writing to `tasks.json`.
    - `add_task()`, `view_tasks()`, `mark_complete()`, `delete_task()`: Core task management functions.
- **`tasks.json`**: The data store for all tasks. This file is created and managed by the application.
- **`README.md`**: High-level documentation for human users.
- **`todo.md`**: A list of planned features and improvements. This should be consulted for new feature ideas.
- **`CLAUDE.md`**: Instructions for a different AI model. Can be used for context but `GEMINI.md` takes precedence.

## Committing Changes

When asked to commit changes:

1.  Use `git status` to identify all modified and untracked files.
2.  Use `git add .` to stage all relevant changes.
3.  Review the recent commit style with `git log -n 3`.
4.  Propose a commit message that is concise and follows the established pattern (e.g., "feat: Add search functionality" or "fix: Corrected due date validation").
