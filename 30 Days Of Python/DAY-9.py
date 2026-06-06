"""
user = int(input('Enter your age: '))
if user >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18 - user} more years to learn to drive.')    
"""

"""
age = 20
users = int(input('Enter your age: '))
if users > 20:
    print(f'You are {users - 20} years older than me.')
elif users < 20:
    print(f'You are {20 - users } years younger than me. ')
else:
    print('We are just the same age.')        
"""
"""
user1 = int(input('Enter number one: '))
user2 = int(input('Enter number two: '))

if user1 > user2:
    print(f"{user1} is greater than {user2}")
elif user1 < user2:
    print(f'{user1} is smaller than {user2}')
else:
    print(f'{user1} is equal to {user2}')
"""
"""
users1 = int(input('Please enter your grade: '))

match users1:
    case users1 if  90 <= users1 <= 100:
        print('A')
    case users1 if 80 <= users1 <= 89:
        print('B')
    case users1 if 70 <= users1 <= 79:
        print('C')    
    case users1 if 60 <= users1 <= 69:
        print('D')
    case users1 if 0 <= users1 <= 59:
        print('F')   
    case _:
        print('Wrong grade, Please type the correct one.')   
"""

"""
autumn =['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
month = input('Please enter the month today: ')

if month in autumn:
    print(f'{month} is Autumn Season.')
elif month in winter:
    print(f'{month} is Winter Season.')   
elif month in spring:
    print(f'{month} is Spring Season.') 
elif month in summer:
    print(f'{month} is Summer Season.') 
else:
    print('Invalid month name, Please type the month correctly.')    
"""


"""
#importing this is important so python ccan read and write
#text files that are formatted using json data.
import json

#python will open the file 'fruits.json' and will only do read mode 
#that represents 'r'
with open('fruits.json', 'r') as file:
    #python will read the file (contains json data) using json.load(file)
    #and it will convert your data back into a normal python list
    #that will be saved in a variable named fruits 
    fruits = json.load(file)

#make a user input that asks the user for his/her desired fruit.
#and save the value the user put in the user input in the variable named input_fruits.
input_fruits = input('Please enter your fruit: ')

#make a conditional statement, if the value of the variable named
#input_fruits are not in the fruits that are already saved in the lists fruits
#fruits.append will add the new fruit to the end of the temporary list in memory.
#displaying a print statement that confirms adding the input_fruits to the fruits list.
if input_fruits  not in fruits:
    fruits.append(input_fruits)
    print(f'{input_fruits} added successfully in the list fruits.')
#make an else statement that prints if the input_fruits the user typed
# has already exists in the list fruits.    
else:
    print(f'{input_fruits} already exist in the list.')

#opens the file 'fruits.json' and will do write mode 
with open('fruits.json', 'w') as file:
    #json.dump simply pour or puts the values into the json file 
    #while fruits is the one who will be written or saved and file is the container of the fruits 
    json.dump(fruits, file, indent=4)
"""

"""
#proper way of making a dictionary in python
person = {
    'first_name': 'Kent',
    'last_name': 'Barneso',
    'age':20,
    'country':'China',
    'is_married': False,
    'skills':['Javascript',  'HTML'],
    'address':{
        'street':'Ira',
        'zipcode':'8600'
    }
}

#accessing the skills key in person dictionary
if 'skills' in person:
    #accessing the skills value and its index(kung aha siya dapit na index)
    print(person['skills'][1])
#checks if the test value exists in the list of values in list 'skills'.
if 'Python' in person['skills']:
    print('this person has a Python skills')
else:
    print('this person doesnt have python skill')      

#checks if both values in the list "skills" exists 
if 'Javascript' and 'Python' in person['skills']:
    print('This person is a backend developer.')
else:
    print('This person is lazy as fuck.')    

#checks if the specific mentioned keys in the person dictionary exist.
if person['country'] == 'Philippines' and person['is_married'] == False:
    print(f'{person['first_name']} {person["last_name"]} lives in {person["country"]}. He is not married')
else:
    print(f'{person['first_name']} {person["last_name"]} lives in {person["country"]}. He is not married')

#print(f'{person['first_name']} {person["last_name"]} lives in {person["country"]}. He is not married')  
"""