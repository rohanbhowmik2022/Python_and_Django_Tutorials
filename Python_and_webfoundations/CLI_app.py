# Class -> Task, TodoApp
# Object -> task = Task(title)
# Encapsulation -> Task state inside class
# Method -> mark_complete()
# Abstraction -> CLI logic hidden in run()

# Design
# Task -> Represents a single task
# ToDoApp -> manages tasks and uder interaction


class Task:
    """ Represents a single Task """

    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.title}"
    
class TodoApp:
        """"Main CLI Application"""

        def __init__(self):
             self.tasks = []

        def add_task(self, title):
             task = Task(title)
             self.tasks.append(task)
             print("Task added successfully!")

        def view_tasks(self):
             if not self.tasks:
                  print("No tasks available")
                  return
             
             for index, task in enumerate(self.tasks, start=1):
                  print(f"{index}.{task}")

        def complete_task(self, task_number):
            try:
                task = self.tasks[task_number - 1]
                task.mark_complete()
                print("Task marked as completed!")
            except IndexError:
                print("Invalid task number.")

        def run(self):
            while True:
                print("\n--- Todo CLI App ---")
                print("1. Add Task")
                print("2. View Tasks")
                print("3. Complete Task")
                print("4. Exit")

                choice = input("Choose an option: ")

                if choice == "1":
                    title = input("Enter task title: ")
                    self.add_task(title)

                elif choice == "2":
                    self.view_tasks()

                elif choice == "3":
                    self.view_tasks()
                    try:
                        num = int(input("Enter task number to complete: "))
                        self.complete_task(num)
                    except ValueError:
                        print("Please enter a valid number.")

                elif choice == "4":
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice. Try again.")


if __name__ == "__main__":
    app = TodoApp()
    app.run()         
