class Solution:
    def upperBound(self, nums, x):
        n = len(nums)
        for i in range(n):
            if(nums[i]>x):
                return i
                

        return n

        