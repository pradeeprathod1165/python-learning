class Tasks:
   def __init__(self,task_name,task_detail):
    self.name = task_name
    self.detail = task_detail

class TaskBook:
  def __init__(self):
    self.tasks = []

  def add_task(self,task):
    self.tasks.append(task)

  def view_tasks(self):
    for task in self.tasks:
      print(f"Name: {task.name}, Detail: {task.detail}")

  def search_task(self,search_term):
    found_task = []
    for task in self.tasks:
      if search_term in task.name or search_term in task.detail:
        found_task.append(task)
    if found_task:
      print("Tasks found:")
      for task in found_task:
          print(f"Name: {task.name}, Detail: {task.detail}")
    else:
      print("No tasks found.")

# create task instances
task1 = Tasks("Pradeep", "1234567890")
task2= Tasks("Anjali", "987654321")

# Create a task book
task_book = TaskBook()

# Add tasks
task_book.add_task(task1)
task_book.add_task(task2)

# View tasks
task_book.view_tasks()

#search tasks
task_book.search_task("Pradeep")
task_book.search_task("Anjali")