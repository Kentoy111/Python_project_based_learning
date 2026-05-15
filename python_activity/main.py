import pyfiglet
import random
import datetime
import student_tools
from school_package import final_grade, attendance_status, Student



name = input("Enter student name: ")
course = input("Enter course: ")
attendance = input("Enter attendance status (present/absent): ")

student = Student(name, course)

print("\n--- STUDENT REPORT ---")
print(student_tools.student_greeting(name))
print(student.introduce())
avg = student_tools.compute_average(90, 85, 88)
print("Average from module:", avg)
grade = final_grade(89, 91, 94)
print("Final grade from package:", grade)
print(attendance_status(attendance))
print("Random Student ID:", random.randint(1000, 9999))
print("Date and Time:", datetime.datetime.now())
print(pyfiglet.figlet_format("Python Lab"))




