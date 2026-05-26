"""
Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Make an empty dictionary to store keys(item) and values(dft = 0) 
        tally = {}
        #make an if statement that decides if the lenght of the each of variables are not equal to each other
        # return False   
        if len(s) != len(t):
                return False
        #Make a for loop that checks every item in the variable s(r-a-c-e-c-a-r)
        for item in s:
            #Assign the dictionary to store the items(each letter) and add its value by 1 when the letter
            #exceeds the default value which is 0
            tally[item] = tally.get(item, 0) + 1
        #make a second loop that checks every item on variable t(c-a-r-r-a-c-e)    
        for item in t:
            #make a conditional statement that decides to return a falsy value when
            #the items in t didnt exist in the saved items in s
            if item  not in tally or tally[item] == 0:
                #Note:Everything past return false will not be read by python because it acts as a shutdown
                return False
            #update the item in t everytime it has the same keys as s decrease it by one its goal is to reset back to 0
            tally[item] -= 1 
        #its just telling the computer that we win because there is no error in the security above 
        return True
