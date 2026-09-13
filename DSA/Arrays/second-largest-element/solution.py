class Solution:
    def secondLargestElement(self, nums):
        nums.sort()
        n = len(nums)
        for i in range(n-2,-1,-1):
            largest_element=nums[n-1]
            if((nums[i] != largest_element)):
                  second_largest = nums[i]
                  break;
        else: return -1 
        return second_largest      
                  

        