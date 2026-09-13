class Solution:
    def secondLargestElement(self, nums):
        largest = nums[0]
        slargest = -10**5
        n = len(nums)
        for i in range(n):
            if(nums[i] > largest):
                slargest = largest;
                largest = nums[i]
            else:
                if(nums[i] < largest and nums[i]> slargest):
                    slargest = nums[i]
        if(slargest == -10**5):
           return -1            
        return slargest              

        


        