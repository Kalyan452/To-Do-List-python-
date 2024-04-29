class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks in the to-do list.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
        else:
            print("Invalid task index.")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added.")
        elif choice == "2":
            todo_list.show_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)
            print("Task removed.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()