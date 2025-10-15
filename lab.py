#To-Do List program
while True:
    try:

        user_answer = input("do you want to add a new To-Do item? answer by (y) for yes and (n) for no or exit.: ").strip().lower()
        if user_answer == "exit":
            print("thank you for using the To-Do program, come back again soon")
            break
        elif user_answer == "y":
            file = open("to_do.txt", "a+", encoding="UTF-8")
            to_do = input("Type the tasks you want to do.: ")
            file.write(to_do + "\n")
            file.close()

        elif user_answer =="n":
            answer = input("do you want to list your To-Do items? answer (y) for yes and (n) for no.").strip().lower()
            if answer == "y":
                file = open("to_do.txt", "r", encoding="utf-8")
                content = file.readlines()
                for item in content:
                    print(item.strip())
                file.close()

            elif answer == "n":
                continue

            else:
                raise TypeError("Please enter either (Y) for yes or (n) for no")
        else:
            raise TypeError("Please enter either (Y) for yes or (n) for no or exit ")
        
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)



        