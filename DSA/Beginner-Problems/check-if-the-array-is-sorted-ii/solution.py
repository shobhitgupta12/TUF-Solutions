class Solution:
    def isSorted(self, nums):
        value = True
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                value = False
                
            if(value == False):
                return False
        else: return True
               