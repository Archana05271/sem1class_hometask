def add_student(students):
    student_id = input("Enter student ID: ")
    name = input("Enter student Name: ")
    grade = input("Enter student Grade: ")
    major = input("Enter student Major: ")
    students[student_id] = {'Name': name, 'Grade': grade, 'Major': major}
    print("Student added or updated successfully!")

def display_students(students):
    if not students:
        print("No students found.")
    else:
        for student_id, details in students.items():
            print(f"ID: {student_id}, Name: {details['Name']}, Grade: {details['Grade']}, Major: {details['Major']}")

def remove_student(students):
    student_id = input("Enter student ID to remove: ")
    if students.pop(student_id, None):
        print("Student removed successfully!")
    else:
        print("Student not found.")

def search_student(students):
    student_id = input("Enter student ID to search: ")
    details = students.get(student_id)
    if details:
        print(f"ID: {student_id}, Name: {details['Name']}, Grade: {details['Grade']}, Major: {details['Major']}")
    else:
        print("Student not found.")

def main():
    students = {}
    while True:
        print("\nMenu: 1-Add/Update, 2-Display, 3-Remove, 4-Search, 5-Exit")
        choice = input("Enter your choice (1-5): ")
        match choice:
            case '1':
                add_student(students)
            case '2':
                display_students(students)
            case '3':
                remove_student(students)
            case '4':
                search_student(students)
            case '5':
                print("Goodbye.....")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
