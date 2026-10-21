# Python Task Manager

A command-line task management application built with Python that allows users to create, assign, manage, and track tasks.

The project uses file-based data storage and includes user authentication, task management, administrative permissions, and reporting functionality.

## Features

- User login and authentication
- Admin-only user registration
- Create and assign tasks to users
- View all tasks
- View tasks assigned to the logged-in user
- Edit task assignments and due dates
- Mark tasks as complete
- Delete tasks
- Track overdue and incomplete tasks
- Generate task and user statistics
- Generate task and user overview reports
- Admin-specific functionality and permissions

## Technologies Used

- Python
- Python `datetime` module
- Python `pathlib` module
- File I/O
- Functions and modular programming
- Dictionaries and lists
- Exception handling
- Conditional logic and loops

## How It Works

The application stores user credentials in a `user.txt` file and task information in a `tasks.txt` file.

When the program starts, the user is required to log in using valid credentials. The available menu options depend on whether the logged-in user is a standard user or an administrator.

Standard users can create tasks, view tasks, manage their assigned tasks, and mark tasks as complete.

Administrators have additional functionality, including registering users, deleting tasks, viewing completed tasks, generating reports, and viewing task and user statistics.

## Reporting

The application can generate two reports:

### Task Overview

Provides information including:

- Total number of tasks
- Completed tasks
- Incomplete tasks
- Overdue tasks
- Percentage of incomplete tasks
- Percentage of overdue tasks

### User Overview

Provides statistics for each user, including:

- Number of assigned tasks
- Percentage of total tasks assigned
- Percentage of completed tasks
- Percentage of incomplete tasks
- Percentage of overdue tasks

## Running the Project

1. Clone or download this repository.
2. Make sure Python 3 is installed.
3. Ensure `user.txt` and `tasks.txt` are located in the same directory as the Python program.
4. Open a terminal in the project directory.
5. Run:

    python3 task_manager.py

6. Log in using a username and password contained in `user.txt`.

## What I Learned

This project helped me develop my understanding of Python programming fundamentals and apply them to a larger application. In particular, I gained experience with modular programming, file handling, user authentication, data structures, input validation, date handling, and role-based program functionality.

I also gained experience breaking a larger problem into individual functions and using persistent text files to store and update application data.

## Future Improvements

Possible future improvements include:

- Migrating data storage from text files to a SQL database
- Hashing and securely storing user passwords
- Adding a graphical or web-based user interface
- Adding more detailed input validation
- Implementing different user permission levels
- Adding automated tests

## Author

Ally Remas
