import logging

# Set up logging
logging.basicConfig(filename='main_errors.log', level=logging.ERROR, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

tasks = []

def main():
    print("Welcome to Task Manager: \n 1 for adding tasks. \n 2 for editing task status. \n 3 for showing incomplete tasks. \n 4 for exitting the program.")
    while True:
        choice = input("Enter your choice: ")
        match choice:
            case '1':
                add_task()
            case '2':
                show_tasks(tasks)
                try:
                    task_no = int(input("Enter task number:"))
                    change_task_status(task_no,)
                except ValueError as e:
                        print("Invalid value. Make sure you entered a number and not the task name \n check logs for more info")
                        logging.error(f"Error adding task: {e}")
                except e:
                    print("An error occured. Check logs for more info")
                    logging.error(f"Error adding task :{e}")

            case '3':
                show_incompleted_tasks()
            case '4':
                return 0
            case _:
                print("Invalid choice")

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


def show_tasks(tasks):
    print_task(tasks)
    return 0

def show_incompleted_tasks():
    incomplete_tasks = [task for task in tasks if task["completed"] == False]
    print_task(incomplete_tasks)

if(__name__ == "__main__"):
    main()