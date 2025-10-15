# To-Do List program with JSON
import json
import os

filename = "to_do.json"

# نحمل المهام من الملف (لو موجود) وإلا نبدأ بقائمة فاضية
if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        tasks = json.load(f)
else:
    tasks = []

while True:
    try:
        user_answer = input("Choose: add / list / done / search / exit: ").strip().lower()

        if user_answer == "exit":
            print("Thank you for using the To-Do program, come back again soon")
            break

        elif user_answer == "add":   # إضافة مهمة
            title = input("Enter task title: ").strip()
            date_time = input("Enter date & time (YYYY-MM-DD HH:MM:SS): ").strip()

            task = {
                "title": title,
                "datetime": date_time,
                "done": False   # افتراضيًا False
            }
            tasks.append(task)

            with open(filename, "w", encoding="utf-8") as f:
                json.dump(tasks, f, indent=4)

            print("Task added ✅")

        elif user_answer == "list":   # عرض المهام
            if not tasks:
                print("Your list is empty.")
            else:
                for i, t in enumerate(tasks, start=1):
                    status = "DONE" if t["done"] else "NOT DONE"
                    print(f"{i}- {t['title']} - {t['datetime']} - {status}")

        elif user_answer == "done":   # تعليم مهمة كـ DONE
            if not tasks:
                print("No tasks to mark.")
                continue

            for i, t in enumerate(tasks, start=1):
                status = "DONE" if t["done"] else "NOT DONE"
                print(f"{i}- {t['title']} - {t['datetime']} - {status}")

            try:
                num = int(input("Enter task number to mark as DONE: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1]["done"] = True
                    with open(filename, "w", encoding="utf-8") as f:
                        json.dump(tasks, f, indent=4)
                    print("Task updated ✅")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif user_answer == "search":   # البحث عن مهمة
            keyword = input("Enter keyword to search in titles: ").lower()
            found = False
            for i, t in enumerate(tasks, start=1):
                if keyword in t["title"].lower():
                    status = "DONE" if t["done"] else "NOT DONE"
                    print(f"{i}- {t['title']} - {t['datetime']} - {status}")
                    found = True
            if not found:
                print("No matching tasks.")

        else:
            print("Invalid choice. Try again.")

    except Exception as e:
        print("Error:", e)
