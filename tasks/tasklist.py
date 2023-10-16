from task import Task


class TaskList:
    def __init__(self):
        self.tasks = []
        self.archived_tasks = []

    def add_task(self, name, description):
        task = Task(name, description)
        self.tasks.append(task)

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                return
        print(f"Tâche '{task_name}' introuvable dans la liste.")

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_completed()
                self.archived_tasks.append(task)
                self.tasks.remove(task)
                return
        print(f"Tâche '{task_name}' introuvable dans la liste.")

    def display_tasks(self):
        if not self.tasks:
            print("Aucune tâche dans la liste.")
        else:
            for task in self.tasks:
                print(task)

    def display_archived_tasks(self):
        if not self.archived_tasks:
            print("Aucune tâche archivée.")
        else:
            for task in self.archived_tasks:
                print(task)

    def save_list(self, file_path):
        with open(file_path, "a") as file:
            file.write("### Tasks ###\n")
            for task in self.tasks:
                # 写入任务信息
                file.write(
                    f"The name of the task:{task.name}, The description of the task:{task.description}, The state of the task:{task.completed}\n")
            file.write("### Achived Tasks ###\n")
            for archived_task in self.archived_tasks:
                # 写入已完成任务信息
                file.write(
                    f"The name of the task:{archived_task.name}, The description of the task:{archived_task.description}, The state of the task:{archived_task.completed}\n")
