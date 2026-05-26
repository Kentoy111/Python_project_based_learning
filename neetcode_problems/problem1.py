#Example 1:
#Input: nums = [1, 2, 3, 3]
#Output: true

#Example 2:
#Input: nums = [1, 2, 3, 4]
#Output: false


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #make an empty set to be the new container for your anti duplicate list
        checklist1 = set()
        #loops one by one in the list nums (Ex: [1 ->2 ->3 ->4])
        for item in nums:
            #if  such value exist in the empty set return True to stop the adding of list
            if item in checklist1:
                return True
            #if no such value exist in the empty set add the items to the empty set
            checklist1.add(item)   
        #this is just the final result of the duplicate checker 
        # meaning there are no more duplicates detected by the loop
        return False
        
