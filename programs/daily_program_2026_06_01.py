# Automatically generated daily program
# Date: 2026-06-01 20:00:14

class TodoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        
    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            
    def display(self):
        for i, t in enumerate(self.tasks):
            status = "[x]" if t["done"] else "[ ]"
            print(f"{i}. {status} {t['task']}")

if __name__ == "__main__":
    todo = TodoList()
    todo.add_task("Learn Python")
    todo.add_task("Automate GitHub Push")
    todo.mark_done(1)
    print("My Tasks:")
    todo.display()
