class Solution:
    def largestElement(self, nums):
        largest_element = -10**4
        for i in nums:
            largest_element = max(largest_element,i)

        return largest_element    
        