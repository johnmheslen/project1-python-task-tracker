# Task Tracker - TODO

## Features to Add

- [ ] **Task Filtering System**: Add ability to filter tasks by completion status
  - Add new menu option "View filtered tasks" 
  - Allow user to choose: All tasks, Completed only, or Pending only
  - Modify view_tasks() function to accept filter parameter
  - Update display headers to reflect current filter (e.g., "COMPLETED TASKS", "PENDING TASKS")
  - Show appropriate summary stats for filtered view
  - Handle empty filter results gracefully

- [ ] **Search Functionality**: Add ability to search tasks by keyword
  - Add new menu option "Search tasks"
  - Prompt user to enter search keyword/phrase
  - Search through task descriptions (case-insensitive)
  - Display matching tasks with search term highlighted or marked
  - Show "No tasks found matching '[keyword]'" if no results
  - Consider searching other fields like priority or due date
  - Allow partial word matching for better user experience

- [ ] **Export to Text Function**: Export tasks to a readable text file
  - Add new menu option "Export tasks to file"
  - Prompt user for filename (default: tasks_export_YYYY-MM-DD.txt)
  - Create human-readable format with clear sections
  - Include task status, priority, creation date, due date, completion date
  - Separate completed and pending tasks into different sections
  - Add export timestamp and summary statistics at top
  - Handle file writing errors gracefully
  - Confirm successful export with file location


## Improvements

- [ ] Add option to set due dates for existing tasks (or set them to null)
- [ ] Migration utility for existing tasks without due dates 

## Bug Fixes

- [ ] 

## Ideas

- [ ] 

---

*Add your project ideas and feature requests here. You can reference this file when asking Claude to implement new functionality.*