import sys
from task import TaskManager, TaskPresenter


def main(filename="tasks.txt"):
    print(f"using {filename} as a db")

    tm = TaskManager()
    tp = TaskPresenter()

    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("q. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            create_task(tm)
        elif choice == "2":
            tp.print()
        elif choice == "3":
            complete_task(tm)
        elif choice == "q":
            break


def create_task(tm, msg="Enter a task: "):
    title = input(msg)
    tm.create(title)


def complete_task(tm):
    try:
        task_id = int(input("Enter task id: "))
        if tm.complete(task_id) == None:
            print("Task not found")
        else:
            print("Task completed 🎉")
    except ValueError:
        print("Invalid id")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    main()
