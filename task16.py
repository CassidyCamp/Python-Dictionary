student = {"name": "Ali", "age": 25, "grade": "A"}

delete = input("Enter delete text: ")

if delete.lower() in student:
    del student[delete]
    print(student)
else:
    print("Bunday kalit yo‘q")
