#ITERATING 0-10 using for and while loop
#for item in range(1, 11, 1):
#    print(item)
#item = 0
#while item != 10:
#    print(item)
#    item += 1



#ITERATING 10-0 using for and while loop
#for item in range(10, 0, -1):
#    print(item) 

#items = 10
#while items != 0:
#    print(items)
#    items -= 1 

#LOOP that makes right triangle
#for item in range(1, 8, 1):
#    print('#' * item)
    
"""
for col in range(4):
    for row in range(8):
        print('#' , end='')
    
    print()
"""
#Exercise 1:Countdown Loop
"""
for i in range(10, 0, -1):
    print(i)
print("Blastoff")
"""


#Exercise 2: Even number sum
"""
sum = 0
sums = 0
for i in range(0, 51):
    if (i % 2) == 0:
        sum += i
    else:
        sums += i        
print(sum)
print(sums)
"""

"""
#Exercise 3:Score Validator
user = True
count = 1
scores = 0
while user:
    score = int(input("Enter your grade: "))
    count += 1
    if 100 > score > 0:
        scores += score
    else:
        user = False    
    if count > 5:
        user = False
average = scores / 5 
print(average)    
"""
"""
#Exercise: Looping through list and checks the values if it mets the condition
list = [12, 5, 8, 19, 21, 3, 14]
lists = []
for i in list:
    if i > 10:
        print('Yes')
        lists.append(i)
        if i == 21:
            print('Found 21')    
    else:
        print('No')
print(lists)         
"""

"""
#Exercise: Multiples of 3
for i in range(0, 31, 3):
    print(i)
    """
"""
#Exercise: Countdown
for i in range(5, 0, -1):
    print(i)
print('Bayot')    
"""
"""
scores = [25, -5, 40, 120, 15]
score = []
sum = 0
for i in scores:
    if 100 > i > 0:
        sum = sum + i
        score.append(i)
        print(i)
    else:
        print('One error found')    
print(score)
"""

"""
user =  True
while user:
    inputs = input('Enter the password: ')
    if inputs == 'Bayot':
        print('Access Granted, Yads :>')
        user = False
    else:
        print('Wrong password, Try Again')
        user == True    
"""

list = [1, 2, 3, 4, 5]
for i in range(1, 6):
    for j in range(1):
        print(i * j)
