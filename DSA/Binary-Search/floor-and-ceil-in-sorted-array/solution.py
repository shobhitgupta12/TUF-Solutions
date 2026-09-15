class Solution:
    def getFloorAndCeil(self, nums, x):
        n = len(nums)

        floor = -1
        ceil = -1

        for i in range(n):
            if nums[i] <= x:
                floor = nums[i]

            if nums[i] >= x:
                ceil = nums[i]
                break

        return floor, ceil