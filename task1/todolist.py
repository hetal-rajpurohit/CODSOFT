# list to store the tasks
tasks = []
completed_task = []

while True:
    print("\n--- TO DO LIST MENU ---")
    print("1. Create task.")
    print("2. Update task.")
    print("3. Track tasks.")
    print("4. Exit.")

    choice = input("Enter your choice (1/2/3/4): ")

    #create task
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("New task created successfully!")

    #update task
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available to update.")

        else:
            print("---PENDING TASKS---")
            for i in range(len(tasks)):
                print(i + 1,".", tasks[i])

            print("\n1. Mark task as completed.")
            print("2. Delete task.")

            new_choice = input("Choose an option (1/2): ")

            num = int(input("Enter task number: "))

            if new_choice == "1":
                completed_task.append(tasks[num - 1])
                tasks.pop(num-1)
                print("Task marked as completed!")

            elif new_choice == "2":
                tasks.pop(num-1)
                print("Task deleted.")

            else:
                print("invalid update option.")

    #track tasks
    elif choice == "3":
        print("---PENDING TASKS---")
        if len(tasks) == 0 :
            print("No tasks pending.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

        print("---COMPLETED TASKS---")
        if len(completed_task) == 0:
            print("Zero tasks completed. ")
        else:
            for i in range(len(completed_task)):
                print(i + 1 , ".", completed_task[i])
    
    #done
    elif choice =="4":
        print("Exiting TO-DO list.Goodbye!!")
        break

    else:
        print("Invalid choice, please choose again.")
