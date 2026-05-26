dog = {
    'name': 'roger',
    'color': 'brown',
    'breed': 'wolf',
    'legs': 'four',
    'age': 'one'
}

del dog['name']#deleting the key and values of the dictionary
del dog#deleting dog dictionary
#print(dog)



student = {
    'first_name': 'kent',
    'last_name': 'barneso',
    'gender': 'male',
    'age':'20',
    'marital_status': 'single',
    'skills': ['basic_programming'],
    'country': 'Philippines',
    'city': 'Butuan',
    'address':'Ira'
}
#students = list(student.keys())

#students_values = list(student.values())

student['skills'].append('HTML')

del student['first_name']
print(len(student))
print(student['skills'])
print(type(student['skills']))
#print(students)
#print(students_values)
print(student)
