class Solution:
    def searchRange(self, nums, target):
        first = -1
        last = -1
        n = len(nums)
        for i in range(n):
            if(nums[i] == target):
               first = i
               break
            
        for j in range(n-1,-1,-1):    
            if(nums[j] == target):
               last = j
               break

        return first,last
