import sys


def main(filename="tasks.txt"):
    print(f"using {filename} as a db")

    print("1. Add task")
    print("2. View tasks")
    print("3. Quit")

    choice = input("Enter your choice:")
    if choice == "1":
        with open(filename, "a") as f:
            task = input("Enter a task:")
            f.write(task + "\n")



if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    main()


