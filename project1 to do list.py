tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("✅ Task added!")

    elif choice == "2":
        print("\n📋 Your Tasks:")

        # Empty list check
        if not tasks:
            print("⚠️ No tasks yet!")
        else:
            # Numbering tasks
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice! Try again.")