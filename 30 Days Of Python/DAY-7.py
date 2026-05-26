it_companies = {'google', 'firefox', 'edge'}
it_comapanies1 = {'yahoo', 'cloud', 'gmail'}


#Adds single element values to the target set
it_companies.add('yahoo')

#Adds multiple element values, like the second container of sets that have multiple values in it 
#when adding multiple values and not a container set just use .update(['value1', 'value2'])!
#it_companies.update(it_comapanies1)

#raises KeyError, use this if you want the resulted error to help you identify bugs in your logic.
#it_companies.remove('cloud')

#raises nothing, use this if you want to not crash your program like playing safe and if you dont care if the element is missing.
#it_companies.discard('gmail')

#print(len(it_companies))
#print(it_companies)

a = {3}
b = {4,5, 6}

#joining a and b result:123456
#a.update(b)
#print(a)

#a intersection b
#result = a.intersection(b)
#print(result)

#a subset b
#False if a has no subset of b Ex:a = {1, 2},b = {3, 4, 5, 6}
#Also false if 1 value of a is subset of b while 1 value of a is not
#True  if Ex:a = {1, 3},b = {3, 4, 5, 6}
#print(a <= b)

#prints true if values between two sets are the same.
#results = a.issubset(b)

#prints TRUE if values between two sets are not the same,same principles 
#of symmetric_difference but different behavior 
#result = a.isdisjoint(b)

#prints values between the sets  that are different Ex: a = {1, 3, 4}, b = {4, 5, 6}
#Result: {1,2,3,4,5,6}
#resultss = a.symmetric_difference(b)

#print(results)
#print(result)
#print(resultss)


list = [20, 22, 20, 19, 25, 22]
sets = set(list)
tuples = tuple(list)
#print(list)
#print(sets)
#print(tuples)

#print(len(tuples))#Tuples is the same as list because they both accepts duplicates
#print(len(list))#List is bigger because it accepts duplicates
#print(len(sets))#sets is shorter because it auto rejects duplicates



words = ["I","am", "a", "teacher", "and", "I", "love", "to", "inspire", "and", "teach", "people"]
setss = set(words)
print(setss)