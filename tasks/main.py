"""
Task Management Application

This module defines a simple task management application. It allows users to add, remove, and mark tasks as completed.
The main function initializes the task list, displays a menu for user interaction, and handles user input.
"""


from .tasklist import TaskList
from .main_gui import use_gui, TaskManagerGUI
from logs import configure_logging

import logging

configure_logging()

def display_menu():
    """
    Display the main menu options for the task management application.
    """
    print("\nMenu :")
    print("1. Ajouter une tâche")
    print("2. Supprimer une tâche")
    print("3. Marquer une tâche comme terminée")
    print("4. Afficher la liste des tâches en cours")
    print("5. Afficher la liste des tâches archivées")
    print("6. Quitter")


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
            use_gui_cli(task_list)  # Appeler la fonction pour lancer l'interface graphique
        elif choice == "7":
            break
        else:
            print("Choix non valide. Veuillez entrer un numéro valide.")


if __name__ == "__main__":
    main()
