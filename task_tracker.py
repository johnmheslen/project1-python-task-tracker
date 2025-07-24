#!/usr/bin/env python3
"""
Simple Task Tracker Application
A command-line tool to manage your daily tasks
"""

import json
import os
from datetime import datetime

# Define the filename where tasks will be stored
TASKS_FILE = "tasks.json"

def load_tasks():
    """
    Load tasks from the JSON file.
    If the file doesn't exist, return an empty list.
    
    This demonstrates:
    - File I/O (reading)
    - Exception handling
    - JSON parsing
    """
    try:
        # Check if file exists
        if os.path.exists(TASKS_FILE):
            # Open and read the file
            with open(TASKS_FILE, 'r') as file:
                tasks = json.load(file)
                return tasks
        else:
            # If file doesn't exist, return empty list
            return []
    except json.JSONDecodeError:
        # Handle case where file exists but contains invalid JSON
        print("Error: Tasks file is corrupted. Starting with empty task list.")
        return []
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    """
    Save tasks to the JSON file.
    
    This demonstrates:
    - File I/O (writing)
    - JSON serialization
    - Exception handling
    """
    try:
        # Open file in write mode and save tasks as JSON
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False

def add_task(tasks):
    """
    Add a new task to the list.
    
    This demonstrates:
    - User input
    - Dictionary data structure
    - List manipulation
    """
    # Get task description from user
    description = input("\nEnter task description: ").strip()
    
    # Validate input
    if not description:
        print("Task description cannot be empty!")
        return

    # Get priority from user and validate using while loop
    while True:
        priority = input("Enter a task priority (low, medium, high): ").strip().lower()
        if priority in ['low', 'medium', 'high']:
            break
        else:
            print("Invalid priority! Please enter 'low', 'medium', or 'high'")

    
    # Create a task dictionary with metadata
    task = {
        "id": len(tasks) + 1,  # Simple ID generation
        "description": description,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "priority": priority
    }
    
    # Add task to the list
    tasks.append(task)
    
    # Save to file
    if save_tasks(tasks):
        print(f"✓ Task added successfully!")
    else:
        print("Failed to save task.")

def view_tasks(tasks):
    """
    Display all tasks with their status.
    
    This demonstrates:
    - Iteration over lists
    - String formatting
    - Conditional logic
    """
    if not tasks:
        print("\nNo tasks found. Start by adding a task!")
        return
    
    print("\n" + "="*50)
    print("YOUR TASKS")
    print("="*50)
    
    # Iterate through tasks and display them
    for task in tasks:
        # Use checkbox symbols for visual feedback
        status = "✓" if task["completed"] else "○"
        
        # Format and print task information
        print(f"\n{status} [{task['id']}] {task['description']}")
        print(f"   Created: {task['created_at']}")
        print(f"   Priority: {task['priority'].capitalize()}")
        
        # Show completion time if task is completed
        if task["completed"] and "completed_at" in task:
            print(f"   Completed: {task['completed_at']}")
    
    print("\n" + "="*50)
    
    # Show summary statistics
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed
    
    print(f"Total: {total} | Completed: {completed} | Pending: {pending}")

def mark_complete(tasks):
    """
    Mark a task as completed.
    
    This demonstrates:
    - User input validation
    - List searching
    - Dictionary modification
    """
    if not tasks:
        print("\nNo tasks to mark as complete!")
        return
    
    # Show tasks first
    view_tasks(tasks)
    
    try:
        # Get task ID from user
        task_id = int(input("\nEnter task ID to mark as complete: "))
        
        # Find the task with matching ID
        task_found = False
        for task in tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("This task is already completed!")
                else:
                    # Mark as complete and add completion timestamp
                    task["completed"] = True
                    task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    # Save changes
                    if save_tasks(tasks):
                        print(f"✓ Task {task_id} marked as complete!")
                    else:
                        print("Failed to save changes.")
                
                task_found = True
                break
        
        if not task_found:
            print(f"Task with ID {task_id} not found!")
            
    except ValueError:
        print("Invalid input! Please enter a number.")

def delete_task(tasks):
    """
    Delete a task from the list.
    
    This demonstrates:
    - List manipulation (removal)
    - User confirmation
    - ID reassignment
    """
    if not tasks:
        print("\nNo tasks to delete!")
        return
    
    # Show tasks first
    view_tasks(tasks)
    
    try:
        # Get task ID from user
        task_id = int(input("\nEnter task ID to delete: "))
        
        # Find and remove the task
        task_index = None
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                task_index = i
                break
        
        if task_index is not None:
            # Confirm deletion
            deleted_task = tasks[task_index]
            confirm = input(f"Are you sure you want to delete '{deleted_task['description']}'? (y/n): ")
            
            if confirm.lower() == 'y':
                # Remove the task
                tasks.pop(task_index)
                
                # Reassign IDs to maintain sequence
                for i, task in enumerate(tasks):
                    task["id"] = i + 1
                
                # Save changes
                if save_tasks(tasks):
                    print("✓ Task deleted successfully!")
                else:
                    print("Failed to save changes.")
            else:
                print("Deletion cancelled.")
        else:
            print(f"Task with ID {task_id} not found!")
            
    except ValueError:
        print("Invalid input! Please enter a number.")

def show_menu():
    """
    Display the main menu options.
    """
    print("\n" + "="*50)
    print("TASK TRACKER MENU")
    print("="*50)
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Exit")
    print("="*50)

def main():
    """
    Main program loop.
    
    This demonstrates:
    - Program flow control
    - Menu-driven interface
    - Function calls
    """
    print("Welcome to Task Tracker!")
    print("A simple command-line tool to manage your tasks")
    
    # Load existing tasks
    tasks = load_tasks()
    
    # Main program loop
    while True:
        # Show menu
        show_menu()
        
        # Get user choice
        choice = input("\nEnter your choice (1-5): ").strip()
        
        # Process user choice
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nThank you for using Task Tracker!")
            print("Your tasks have been saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
        
        # Pause before showing menu again (except after viewing tasks)
        if choice not in ['2', '5']:
            input("\nPress Enter to continue...")

# Entry point of the program
if __name__ == "__main__":
    main()

