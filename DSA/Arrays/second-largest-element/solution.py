class Solution:
    def secondLargestElement(self, nums):
        n = len(nums)
        slargest = -10**5
        largest = -10**4
        largest = nums[0]
        for i in range(len(nums)):
            if(nums[i]> largest):
                largest = nums[i]


        for i in range(len(nums)):
            if(nums[i]>slargest and nums[i] !=largest):
                slargest = nums[i]
                
        if slargest == -10**5:
            return -1

        return slargest                             


        