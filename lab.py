# To-Do List program

while True:
    try:
        user_answer = input("Do you want to add a new To-Do item? answer by (y) for yes and (n) for no or type exit: ").strip().lower()

        if user_answer == "exit":
            print("Thank you for using the To-Do program, come back again soon")
            break

        elif user_answer == "y":
            to_do = input("Type the task you want to add: ").strip()   
            if not to_do:
                print("Empty task was ignored.")
                continue

            with open("to_do.txt", "a", encoding="utf-8") as f:
                f.write(to_do + "\n")
            print("Task added ")

        elif user_answer == "n":
            answer = input("Do you want to list your To-Do items? answer (y) for yes and (n) for no: ").strip().lower()

            if answer == "y":
                with open("to_do.txt", "r", encoding="utf-8") as f:
                    content = f.readlines()
            
                if not content:
                    print("Your list is empty.")

                else:
                    print("Your To-Do items:")
                    for item in content:
                        print("- " + item.strip())

            elif answer == "n":
                continue

            else:
                print("Please enter either (y) for yes or (n) for no")

        else:
            print("Please enter either (y) for yes, (n) for no, or exit")

    except Exception as e:
        print("Error:", e)
