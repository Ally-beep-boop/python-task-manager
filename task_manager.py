# ========================
# IMPORTS AND FILE PATHS
# ========================


# External modules
from datetime import datetime
from pathlib import Path

# File paths for user and task data
user_file_path = 'user.txt'
task_file_path = 'tasks.txt'


# ========================
# USER AUTHENTICATION
# ========================


# Ask the user to login with credentials from the user.txt file
# Use a while loop to validate the username and password.
def login():
    # Create a Path object for the user.txt file
    user_file_path = Path('user.txt')

    # Check if the user.txt file exists
    if not user_file_path.is_file():
        print("The user.txt file does not exist. Please create it and add some users.")
        exit()

    # Read the usernames and passwords from the user.txt file
    users = {}
    with open(user_file_path, 'r') as f:
        for line in f:
            username, password = line.strip().split(', ')
            users[username] = password

    # Validate the username and password
    while True:
        username = input("\nEnter your username: ")
        password = input("\nEnter your password: ")

        if username in users and users[username] == password:
            print("\nLogin successful!")
            return username  # Return the logged-in username
        else:
            print("\nInvalid username or password. Please try again.")


logged_in_username = login()  # Call the login function and store the logged-in username


# ========================
# USER MANAGEMENT
# ========================


# Define a function to register a new user to the user.txt file
def reg_user():

    # Get the logged-in username
    if logged_in_username != 'admin':
        print("\nOnly admin users can register new users.")
        return

    # Request input of a new username
    new_username = input("\nEnter a new username: ")

    # Request input of a new password
    new_password = input("\nEnter a new password: ")

    # Request input of password confirmation.
    confirm_password = input("\nConfirm the new password: ")

    # Check if the new password and confirmed password are the same
    if new_password == confirm_password:

        # If they are the same, add them to the user.txt file,
        with open(user_file_path, 'a') as f:
            f.write(f"{new_username}, {new_password}\n")
        print("\nNew user registered successfully!")

    # If the user enters a new username that already exists, print an error
    # message and ask them to choose a different username
    with open(user_file_path, 'r') as f:
        users = [line.split(', ')[0] for line in f]

    if new_username in users:
        print("Username already exists. Please enter a different username.")
        return


# ========================
# TASK MANAGEMENT
# ========================


# Define a function to add a new task to the task.txt file
def add_task():

    # Request the username of the person whom the task is assigned to,
    assigned_to = input("\nEnter the username of the person assigned "
                        "to the task: "
                        )

    # Request the title of the task,
    title = input("\nEnter the title of the task: ")

    # Request the description of the task,
    description = input("\nEnter the description of the task: ")

    # Request the due date of the task.
    due_date = input("\nEnter the due date of the task (DD-MM-YYYY): ")

    # Get the current date.
    current_date = datetime.now().strftime("%d-%m-%Y")

    # Add the data to the file tasks.txt
    with open(task_file_path, 'a') as f:
        f.write(
            f"\n{assigned_to}, {title}, {description}, {current_date}, "
            f"{due_date}, No"
        )

    print("\nTask added successfully!")


# Define a function to view all tasks from the task.txt file
# Display the task in a user friendly way, with a number for each task
def view_all():

    with open(task_file_path, 'r') as f:
        for line in f:
            if not line.strip():
                continue

            (
                assigned_to,
                title,
                description,
                current_date,
                due_date,
                completed
            ) = line.strip().split(', ')

            print(
                    f"\nTask: {title}"
                    f"\nAssigned to: {assigned_to}"
                    f"\nDate Assigned: {current_date}"
                    f"\nDue Date: {due_date}"
                    f"\nTask Complete? {completed}"
                    f"\nTask Description: {description}\n"
                )


# Define a function to view tasks assigned to the logged-in user
def view_mine():
    user_tasks = []
    all_tasks = []

    # Recursive function whenever a user selects a task that does not exist
    def get_valid_task_number():
        try:

            task_number = int(input("Enter the number of the task you want to edit: "))

            if task_number < 1:

                print("Please enter a positive integer.")
                return get_valid_task_number()

            return task_number

        except ValueError:

            print("Invalid input. Please enter a valid task number.")
            return get_valid_task_number()

    # Read all tasks from file
    with open(task_file_path, 'r') as f:
        for line in f:
            if not line.strip():
                continue

            task = line.strip().split(', ')
            all_tasks.append(task)

            if task[0] == logged_in_username:
                user_tasks.append(task)

    # Check if user has tasks
    if not user_tasks:
        print("\nYou have no assigned tasks.")
        return

    # Display tasks with numbers
    print(f"\nTasks assigned to {logged_in_username}:\n")

    for i, task in enumerate(user_tasks, start=1):
        print(
            f"{i}. Task: {task[1]}"
            f"\n   Assigned to: {task[0]}"
            f"\n   Date Assigned: {task[3]}"
            f"\n   Due Date: {task[4]}"
            f"\n   Task Complete? {task[5]}"
            f"\n   Task Description: {task[2]}\n"
        )

    # Ask user to choose a task
    while True:
        choice = input(
            "Enter the task number to select a task, or -1 to return: "
        )

        if choice == '-1':
            return

        if not choice.isdigit():
            print("\nInvalid input. Please enter a valid task number or -1.")
            continue

        choice = int(choice)

        if 1 <= choice <= len(user_tasks):
            selected_task = user_tasks[choice - 1]
            break
        else:
            print("\nInvalid task number. Please try again.")

    # Show options for selected task
    print(f"\nSelected task: {selected_task[1]}")
    action = input(
        "\nEnter 'c' to mark as complete or 'e' to edit the task: "
    ).lower()

    if action == 'c':
        selected_task[5] = 'Yes'
        print("\nTask marked as complete.")

    elif action == 'e':
        # Task can only be edited if it is not completed
        if selected_task[5] == 'Yes':
            print("\nCompleted tasks cannot be edited.")
            return

        new_username = input(
            "\nEnter new username to assign task to "
            "(or press Enter to keep current): "
        )
        new_due_date = input(
            "\nEnter new due date (DD-MM-YYYY) "
            "(or press Enter to keep current): "
        )

        if new_username != '':
            selected_task[0] = new_username

        if new_due_date != '':
            selected_task[4] = new_due_date

        print("\nTask updated successfully.")

    else:
        print("\nInvalid option.")
        return

    # Update the task in all_tasks
    for task in all_tasks:
        if task == user_tasks[choice - 1]:
            task[:] = selected_task
            break

    # Rewrite all tasks back to file
    with open(task_file_path, 'w') as f:
        for task in all_tasks:
            f.write(', '.join(task) + '\n')


# Define a function to view completed tasks that have been deleted (admin only)
def view_completed():
    if logged_in_username != 'admin':
        print("\nOnly admin users can view completed tasks.")
        return

    found_completed = False

    with open(task_file_path, 'r') as f:
        print("\nCompleted Tasks:\n")
        for line in f:
            (
                assigned_to,
                title,
                description,
                current_date,
                due_date,
                completed
            ) = line.strip().split(', ')

            if completed.lower() == 'yes':
                found_completed = True

                print(f"\nTask: {title} "
                      f"\nAssigned to: {assigned_to}"
                      f"\nDate Assigned: {current_date}"
                      f"\nDue Date: {due_date}"
                      f"\nTask Complete? {completed}\n"
                      f"\nTask Description: {description}\n")

    # AFTER loop → only print once if none found
    if not found_completed:
        print("There are no completed tasks to display.")


def delete_task():
    if logged_in_username != 'admin':
        print("Only admin users can delete tasks.")
        return

    # Read all tasks
    with open(task_file_path, 'r') as f:
        tasks = [line.strip() for line in f if line.strip()]

    # Check if there are tasks
    if not tasks:
        print("\nNo tasks available to delete.")
        return

    # Display tasks with numbers
    print("\nSelect a task to delete:\n")

    for i, task in enumerate(tasks, start=1):
        title = task.split(', ')[1]
        print(f"{i}. {title}")

    # Get user choice
    choice = input("\nEnter task number to delete or -1 to cancel: ")

    if choice == '-1':
        print("Deletion cancelled.")
        return

    if not choice.isdigit():
        print("Invalid input.")
        return

    choice = int(choice)

    if 1 <= choice <= len(tasks):
        deleted_task = tasks.pop(choice - 1)

        # Rewrite file without that task
        with open(task_file_path, 'w') as f:
            for task in tasks:
                f.write(task + '\n')

        deleted_title = deleted_task.split(', ')[1]
        print(f"\nTask '{deleted_title}' deleted successfully!")

    else:
        print("Invalid task number.")


# =========================
# REPORTING
# =========================


# Define a function to generate reports
def generate_reports():
    if logged_in_username != 'admin':
        print("Only admin users can generate reports.")
        return

    # Read all tasks into a list
    with open(task_file_path, 'r') as task_file:
        tasks = [line.strip().split(', ') for line in task_file if line.strip()]

    # Read all users into a list
    with open(user_file_path, 'r') as user_file:
        users = [line.strip().split(', ')[0] for line in user_file if line.strip()]

    total_tasks = len(tasks)
    total_users = len(users)

    completed_tasks = 0
    overdue_tasks = 0

    for task in tasks:
        due_date = datetime.strptime(task[4], "%d-%m-%Y")
        completed = task[5].lower()

        if completed == 'yes':
            completed_tasks += 1

        if completed == 'no' and due_date < datetime.now():
            overdue_tasks += 1

    incomplete_tasks = total_tasks - completed_tasks

    # Prevent division by zero
    if total_tasks > 0:
        percent_incomplete = (incomplete_tasks / total_tasks) * 100
        percent_overdue = (overdue_tasks / total_tasks) * 100
    else:
        percent_incomplete = 0
        percent_overdue = 0

    # Write task overview report
    with open('task_overview.txt', 'w') as task_report:
        task_report.write(f"Total number of tasks: {total_tasks}\n")
        task_report.write(f"Total completed tasks: {completed_tasks}\n")
        task_report.write(f"Total incomplete tasks: {incomplete_tasks}\n")
        task_report.write(f"Total overdue tasks: {overdue_tasks}\n")
        task_report.write(
            f"Percentage of incomplete tasks: {percent_incomplete:.2f}%\n"
        )
        task_report.write(
            f"Percentage of overdue tasks: {percent_overdue:.2f}%\n"
        )

    # Write user overview report
    with open('user_overview.txt', 'w') as user_report:
        user_report.write(f"Total number of users: {total_users}\n")
        user_report.write(f"Total number of tasks: {total_tasks}\n\n")

        for user in users:
            user_tasks = [task for task in tasks if task[0] == user]
            total_user_tasks = len(user_tasks)

            completed_user_tasks = 0
            incomplete_user_tasks = 0
            overdue_user_tasks = 0

            for task in user_tasks:
                due_date = datetime.strptime(task[4], "%d-%m-%Y")
                completed = task[5].lower()

                if completed == 'yes':
                    completed_user_tasks += 1
                else:
                    incomplete_user_tasks += 1

                    if due_date < datetime.now():
                        overdue_user_tasks += 1

            # Prevent division by zero
            if total_tasks > 0:
                percent_of_total_tasks = (total_user_tasks / total_tasks) * 100
            else:
                percent_of_total_tasks = 0

            if total_user_tasks > 0:
                percent_completed = (
                    completed_user_tasks / total_user_tasks
                ) * 100
                percent_incomplete = (
                    incomplete_user_tasks / total_user_tasks
                ) * 100
                percent_overdue = (
                    overdue_user_tasks / total_user_tasks
                ) * 100
            else:
                percent_completed = 0
                percent_incomplete = 0
                percent_overdue = 0

            user_report.write(f"User: {user}\n")
            user_report.write(
                f"Total tasks assigned to user: {total_user_tasks}\n"
            )
            user_report.write(
                f"Percentage of total tasks assigned to user: "
                f"{percent_of_total_tasks:.2f}%\n"
            )
            user_report.write(
                f"Percentage of user's tasks completed: "
                f"{percent_completed:.2f}%\n"
            )
            user_report.write(
                f"Percentage of user's tasks incomplete: "
                f"{percent_incomplete:.2f}%\n"
            )
            user_report.write(
                f"Percentage of user's tasks overdue: "
                f"{percent_overdue:.2f}%\n\n"
            )

    print("\nReports generated successfully!")


# Define a function to present the contents of task_overview.txt
def display_task_overview():

    if logged_in_username != 'admin':
        print("Only admin users can view the task overview.")
        return

    try:

        with open('task_overview.txt', 'r') as f:
            print("\nTask Overview:\n")
            print(f.read())

    except FileNotFoundError:
        print("The task overview report has not been generated yet. Please generate reports first.")


# Define a function to present the contents of user_overview.txt
def display_user_overview():

    if logged_in_username != 'admin':
        print("Only admin users can view the user overview.")
        return

    try:

        with open('user_overview.txt', 'r') as f:
            print("\nUser Overview:\n")
            print(f.read())

    except FileNotFoundError:
        print("The user overview report has not been generated yet. Please generate reports first.")


# Define a function to display statistics about the tasks and users (admin only)
def display_statistics():
    if logged_in_username != 'admin':
        print("Only admin users can view statistics.")
        return

    task_report = Path("task_overview.txt")
    user_report = Path("user_overview.txt")

    # If reports don't exist → generate them
    if not task_report.exists() or not user_report.exists():
        print("\nReports not found. Generating reports...\n")
        generate_reports()

    # Display task overview
    print("\nTASK OVERVIEW:\n")
    with open(task_report, 'r') as f:
        print(f.read())

    # Display user overview
    print("\nUSER OVERVIEW:\n")
    with open(user_report, 'r') as f:
        print(f.read())


# ========================
# MAIN PROGRAM
# ========================


# Once user has successfully logged in, present them with a menu of options to perform
while True:

    # If the user is an admin, display this menu
    # make sure that the user input is converted to lower case
    if logged_in_username == 'admin':
        menu = input(
            "\nSelect one of the following options: \n"
            "\nr - register a user "
            "\na - add task "
            "\nva - view all tasks "
            "\nvm - view my tasks "
            "\nvs - view completed tasks "
            "\ngr - generate reports "
            "\nds - display statistics "
            "\ndel - delete tasks "
            "\ne - exit \n"
            "\nYour Choice: "
        ).lower()

    # If the user is not an admin, display this menu
    else:
        menu = input(
            "\nSelect one of the following options: \n"
            "\nr - register a user "
            "\na - add task "
            "\nva - view all tasks "
            "\nvm - view my tasks "
            "\ne - exit \n"
            "\nYour Choice: ").lower()

    # If the user selects 'r', allow them to register a new user
    # to the user.txt file only if they are an admin user
    if menu == 'r':
        reg_user()

    # If the user selects 'a', allow them to add a new task to task.txt file
    elif menu == 'a':
        add_task()

    # If the user selects 'va', allow them to view all the tasks from task.txt
    # file
    elif menu == 'va':
        view_all()

    # If the user selects 'vm', check if the username of the person logged in
    # is the same as the username read
    # If they are the same, print the task
    elif menu == 'vm':
        view_mine()

    # If the admin user selects 'vs', allow them to view all the completed tasks
    elif menu == 'vs':
        view_completed()

    # If the admin user selects 'ds', allow them to view statistics
    elif menu == 'ds':
        display_statistics()

    # If the admin user selects 'gr', allow them to generate reports
    elif menu == 'gr':
        generate_reports()

    # If the admin user selects 'del', allow them to delete a task from the task.txt file
    elif menu == 'del':
        delete_task()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")