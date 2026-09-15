class Solution:
    def search(self, nums, k):
        n = len(nums)
        ans = -1
        for i in range(n):
            if(nums[i] == k):
               ans = i
        return ans

