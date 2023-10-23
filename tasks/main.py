"""
Task Management Application

This module defines a simple task management application. It allows users to add, remove, and mark tasks as completed.
The main function initializes the task list, displays a menu for user interaction, and handles user input.
"""


from .tasklist import TaskList
from logs import configure_logging
import logging

configure_logging()

def display_menu():
    """
    Display the main menu options for the task management application.
    """
    print("\nMenu :")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Mark a task as completed")
    print("4. Display the list of active tasks")
    print("5. Display the list of archived tasks")
    print("6. Quit")

def main():
    """
    Main function for the task management application.

    This function initializes the task list, displays the main menu, and handles user input.
    """
    task_list = TaskList()

    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            try:
                name = input("Task name: ")
                description = input("Task description: ")
                task_list.add_task(name, description)
                print(f"Task '{name}' added to the list.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            task_name = input("Name of the task to remove: ")
            task_list.remove_task(task_name)
            print(f"Task '{task_name}' removed from the list.")
        elif choice == "3":
            task_name = input("Name of the task to mark as completed: ")
            task_list.mark_task_completed(task_name)
            print(f"Task '{task_name}' marked as completed.")
        elif choice == "4":
            print("List of active tasks:")
            task_list.display_tasks()
        elif choice == "5":
            print("List of archived tasks:")
            task_list.display_archived_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()
