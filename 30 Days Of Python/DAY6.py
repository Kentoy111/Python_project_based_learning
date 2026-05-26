#making an empty tuple 
empty_tuple = ()
siblings = ('khristine', 'kier', 'kent')
parent = ('romel', 'lilian')
sibling_one, sibling_two, sibling_three = siblings
parent_one, parent_two = parent
family_members = siblings + parent
print(len(siblings))
print(family_members)
print(sibling_one)
print(parent_one)
print("")
fruits = ('apple', 'orange', 'mango')
food = ('chicken', 'rice', 'bread')
beverage = ('water', 'juice', 'coke')
food_stuff = fruits + food + beverage
print(food_stuff)
print('')
food_stuff_lt = list(food_stuff)
print(food_stuff_lt)
print('')
#sips by 4
slice_tuple = food_stuff[::4]
slice_tuple1 = food_stuff_lt[0:9]
slice_tuple2 = food_stuff_lt[0:4] + food_stuff_lt[-4:]
print(slice_tuple)
print(slice_tuple1)
print(slice_tuple2)
print(food_stuff)
print('')
print('')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
for item in nordic_countries:
    if item == 'Denmark':
        print('this is part of nordic countries')