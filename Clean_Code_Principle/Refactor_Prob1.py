# Generate a Student Report

student_name = input("Enter student's name: ")

marks = []

for subject_number in range(1, 6):
    mark = float(input(f"Enter marks for Subject {subject_number}: "))
    marks.append(mark)

total_marks = sum(marks)
average_marks = total_marks / len(marks)

if average_marks >= 75:
    grade = "A"
elif average_marks >= 60:
    grade = "B"
elif average_marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print("\n----- Student Report -----")
print("Student Name :", student_name)
print("Marks        :", marks)
print("Total Marks  :", total_marks)
print("Average      :", average_marks)
print("Grade        :", grade)