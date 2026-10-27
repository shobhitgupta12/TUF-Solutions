class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        countmax = 0
        for i in nums:
            if(i == 1):
                count +=1
                countmax = max(countmax,count)
            else:
                count = 0  
        return countmax