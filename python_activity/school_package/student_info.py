class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
    def introduce(self):
        return f"My name is {self.name} and I am taking {self.course}."

        