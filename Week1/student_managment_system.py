import csv
import os

FILE = "students.csv"


# Load data
def load_students():
    students = []
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(row)
    return students


# Save data
def save_students(students):
    with open(FILE, "w", newline="") as f:
        fieldnames = ["id", "name", "age"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)


# Add student
def add_student(students):
    try:
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")

        students.append({"id": sid, "name": name, "age": age})
        save_students(students)

        print("Student added\n")
    except:
        print("Error adding student\n")


# View students
def view_students(students):
    if not students:
        print("No students found\n")
        return

    for s in students:
        print(s)
    print()


# Search student
def search_student(students):
    sid = input("Enter ID: ")

    for s in students:
        if s["id"] == sid:
            print("Found:", s, "\n")
            return

    print("Student not found\n")


# Update student
def update_student(students):
    sid = input("Enter ID: ")

    for s in students:
        if s["id"] == sid:
            s["name"] = input("New Name: ")
            s["age"] = input("New Age: ")
            save_students(students)
            print("Updated\n")
            return

    print("Student not found\n")


# Delete student
def delete_student(students):
    sid = input("Enter ID: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_students(students)
            print("Deleted\n")
            return

    print("Student not found\n")


# Main
def main():
    students = load_students()

    while True:
        print("1.Add")
        print("2.View")
        print("3.Search")
        print("4.Update")
        print("5.Delete")
        print("6.Exit")

        try:
            choice = int(input("Enter choice: "))

            match choice:
                case 1:
                    add_student(students)
                case 2:
                    view_students(students)
                case 3:
                    search_student(students)
                case 4:
                    update_student(students)
                case 5:
                    delete_student(students)
                case 6:
                    break
                case _:
                    print("Invalid choice\n")

        except ValueError:
            print("Enter a number only\n")


if __name__ == "__main__":
    main()