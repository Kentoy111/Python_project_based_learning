import json
#Parent class
class Student:
    def __init__(self, name, course, grade):
        #private locker(Encapsulation)
        #put or store items like name, course, and grade for the 1st time
        #without self py would not know where to store the values   
        #think of this as the starting part of the game where the game will ask 
        #   for your information to be saved 
        self.__name = name
        self.__course = course
        self.__grade = grade

    def get_name(self):
        #looking at the locker and telling whos there
        #its purpose is to give its value later when someone asked for it 
        return self.__name 

    def set_name(self, name):
         #You want to change or override whats stored inside the locker
         self.__name = name

    def get_course(self):
        return self.__course 
    def set_course(self, course):
        self.__course = course

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade


#the ScholarStudent is now a Child class which it inherits the value of the parent class Student
class ScholarStudent(Student):
    def display_info(self):
        print("Name: " ,self.get_name())
        print("Course: ", self.get_course())
        print("Grade: ", self.get_grade())
        print("Scholarship Type: Scholar")

student1 = Student("Leo", "BSIT" , 90)
student2 = ScholarStudent("Ana", "BSCS", 95)
student3 = Student("Mark", "BSIT", 88)

#Make a list of students
students = [student1, student2, student3]

#Make an empty list to use later
student_list_for_json = []

#make a loop that scans the content of the list students
for s in students:
    #make a dictionary that holds the key and values, it is essential 
    # because this is one way json understands your values
    student_info = {
        "name": s.get_name(),
        "course": s.get_course(),
        "grade": s.get_grade()
    }
    #when the values of student_info is added to the empty list student_list_for_json
    #the empty list has now the studen_info values
    student_list_for_json.append(student_info)

#if the file is not made yet python will make the file for you and store the values based on the code below
#if the file is made it will automatically overrides the old values inside that file
#  like erasing the old mess on a whiteboard
with open('studentss.json', 'w') as file:
    json.dump(student_list_for_json, file, indent=4) # indent makes it look pretty!

print("Data saved as real JSON.")

#opens the files and just tells python that you only want to read the file
with open("studentss.json", "r") as file:
    #this acts as a translator from json syntax to python objects
    data = json.load(file)
    #make a loop that scans the content of data one by one(iteration) and prints your desired keys and values
    for item in data:
        print(f"Name: {item['name']}, Course: {item['course']}, Grade: {item['grade']}")

  



