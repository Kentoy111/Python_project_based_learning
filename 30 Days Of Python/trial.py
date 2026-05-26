"""def triangle():
    for row in range(6,1, -1): 
        for rows in range(1, 6):
            print("*" * rows) # Rows 1 to 5
        print("*" * row)
             # Multiplies row number by string 
    for row in range(1, 6):  # Rows 1 to 5
        print("*" * row) 
triangle()"""

"""def exists(n: int, numbers: list) -> bool:
    for i in range(len(numbers)):
        if numbers[i] == n:
            return True
    return False

print(exists(1, [1, 2, 3, 4, 5, 6]))
print(exists(3, [1, 2, 3, 4, 5]))
print(exists(6, [1,2,3,4,5]))
print(exists(5, []))"""
"""
#making a reverse triangle 
def triangle(n: int):
    #n represents the height, 0 represents the stopping point, and 
    #-1 represents step or skip by that certain number
    for row in range(n, 0, -1):
        print("*" * row)
triangle(6)
"""

"""
total = 0
#treat 1 as starting and 5 as stop number so 1,2,3,4 not include 5.
for i in range(1, 5):
    total += i
print(total)#OUTPUT: 1,2,3,4 total = 10
"""

def add_item(item, items = None):
    if items == None:# if you obviously leave an empty string("") on add_item  when calling the function
        items = []#It will create fresh or brand-new list everytime 
        #used only when adding one item in the end of a list
    items.append(item)
    #its important to put return statement 
    #so the python will do the function 
    # and by using return statement it will
    # remember and hand in the final result 
    return items

print(add_item(''))
print(add_item("b"))
