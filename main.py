import sys
from storage import load_tasks, save_tasks

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Task added: {title}")

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")

def complete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print("Task completed!")
    else:
        print("Invalid task number")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: add <task> | list | done <number>")
    elif sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "done":
        complete_task(int(sys.argv[2]))
