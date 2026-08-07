'''
Refactor Student Management System
Build a Simple Student Management System

Features:
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
'''

def calculate_grade(average_marks):
    if average_marks >= 90:
        return "A"
    elif average_marks >= 80:
        return "B"
    elif average_marks >= 70:
        return "C"
    elif average_marks >= 60:
        return "D"
    elif average_marks >= 50:
        return "E"
    else:
        return "F"


def calculate_pass_fail(average_marks):
    if average_marks >= 50:
        return "Pass"
    else:
        return "Fail"


def get_student_details():
    while True:
        try:
            subject1 = int(input("Enter Subject 1 Marks: "))
            subject2 = int(input("Enter Subject 2 Marks: "))
            subject3 = int(input("Enter Subject 3 Marks: "))
            break
        except ValueError:
            print("Please enter valid numeric marks.")

    total_marks = subject1 + subject2 + subject3
    average_marks = total_marks / 3

    return {
        "Subject1": subject1,
        "Subject2": subject2,
        "Subject3": subject3,
        "Total": total_marks,
        "Average": average_marks,
        "Grade": calculate_grade(average_marks),
        "Status": calculate_pass_fail(average_marks)
    }


students = {}

while True:

    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue

    if choice == 1:

        student_name = input("Enter Student Name: ").lower()
        students[student_name] = get_student_details()

        print("Student Added Successfully!")

    elif choice == 2:

        if len(students) == 0:
            print("No student records found.")
        else:
            for student_name, details in students.items():
                print("\nName:", student_name)

                for key, value in details.items():
                    print(f"{key}: {value}")

    elif choice == 3:

        student_name = input("Enter Student Name to Search: ").lower()

        if student_name in students:

            print("\nStudent Found")
            print("Name:", student_name)

            for key, value in students[student_name].items():
                print(f"{key}: {value}")

        else:
            print("Student not found.")

    elif choice == 4:

        student_name = input("Enter Student Name to Update: ").lower()

        if student_name in students:

            students[student_name] = get_student_details()

            print("Student Details Updated Successfully!")

        else:
            print("Student not found.")

    elif choice == 5:

        student_name = input("Enter Student Name to Delete: ").lower()  

        if student_name in students:
            del students[student_name]
            print("Student Deleted Successfully!")
        else:
            print("Student not found.")

    elif choice == 6:
        print("Exiting Student Management System! \n Thanks for visiting.")
        break

    else:
        print("Invalid Choice!")