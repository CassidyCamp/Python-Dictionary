Students = {
    "Daler": {"age":17, "Jop":"backend developer"},
    "Samandar": {"age":21, "Jop":"frontend developer"}
}

getStudent = input("Enter Student Name: ").capitalize()

print(Students.get(getStudent,"Topilmadi"))