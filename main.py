def add_task():
    global tasks
    task = input("Enter Task Description: ")
    task_info = {"no": (len(tasks) + 1) ,"task": task, "completed": False}
    tasks.append(task_info)
    return 0

def change_task_status(task_no):
    global tasks
    print("Tasks available: ")
    if(task_no > 0 and task_no < len(tasks) + 1):
        tasks[task_no-1]["completed"] = not tasks[task_no-1]["completed"]
        print("Task status changed successfully")
        return 0
    print("Invalid task number")
    return 1

def print_task(desired_list):
    for task in desired_list:
        print(f'{task["no"]}. {task["task"]} - Completed?: {("✔️" if task["completed"] else "❌")}')
    return 0


def show_tasks():
    global tasks
    print_task(tasks)
    return 0

def show_incompleted_tasks():
    incomplete_tasks = [task for task in tasks if task["completed"] == False]
    print_task(incomplete_tasks)
tasks = []

print("Welcome to Task Manager: \n 1 for adding tasks. \n 2 for editing task status. \n 3 for showing incomplete tasks. \n 4 for exitting the program.")
while True:
    choice = input("Enter your choice: ")
    match choice:
        case '1':
            add_task()
        case '2':
            show_tasks()
            task_no = int(input("Enter task number:"))
            change_task_status(task_no,)
        case '3':
            show_incompleted_tasks()
        case '4':
            break
        case _:
            print("Invalid choice")