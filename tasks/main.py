from tasklist import TaskList
import os
from task import Task


def display_menu():
    print("\nMenu :")
    print("1. Ajouter une tâche")
    print("2. Supprimer une tâche")
    print("3. Marquer une tâche comme terminée")
    print("4. Afficher la liste des tâches en cours")
    print("5. Afficher la liste des tâches archivées")
    print("6. Quitter")


def main():
    task_list = TaskList()
    file_path = "todo_list.txt"
    # si le fichier exist, enregistre la liste dans le fichier
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            todo_list = file.read().splitlines()
            for line in todo_list:
                data = line.split(',')
                if len(data) >= 2:
                    parts = line.split(",")
                    for part in parts:
                        if "The name of the task:" in part:
                            name = part.split(":")[1].strip()
                        elif "The description of the task:" in part:
                            description = part.split(":")[1].strip()
                        elif "The state of the task:" in part:
                            is_completed = part.split(":")[1].strip() == "True"
                    task = Task(name, description)
                    if is_completed:
                        task.mark_completed()
                        task_list.archived_tasks.append(task)
                    else:
                        task_list.tasks.append(task)
                else:
                    continue
        # vide le fichier pour ne répéter pas les listes
        with open(file_path, "w") as file:
            file.truncate(0)

    while True:
        display_menu()
        choice = input("Entrez le numéro de votre choix : ")

        if choice == "1":
            name = input("Nom de la tâche : ")
            description = input("Description de la tâche : ")
            task_list.add_task(name, description)
            print(f"Tâche '{name}' ajoutée à la liste.")
        elif choice == "2":
            task_name = input("Nom de la tâche à supprimer : ")
            task_list.remove_task(task_name)
            print(f"Tâche '{task_name}' supprimée de la liste.")
        elif choice == "3":
            task_name = input("Nom de la tâche à marquer comme terminée : ")
            task_list.mark_task_completed(task_name)
            print(f"Tâche '{task_name}' marquée comme terminée.")
        elif choice == "4":
            print("Liste des tâches en cours :")
            task_list.display_tasks()
        elif choice == "5":
            print("Liste des tâches archivées :")
            task_list.display_archived_tasks()
        elif choice == "6":
            task_list.save_list(file_path)
            break
        else:
            print("Choix non valide. Veuillez entrer un numéro valide.")


if __name__ == "__main__":
    main()
