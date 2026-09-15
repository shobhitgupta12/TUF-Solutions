class Solution:
    # Helper function to find the target in the given range
    def func(self, nums, low, high, target):
        # base case
        if low > high:
            return -1

        # to store the index of target
        mid = low + (high - low)//2
        
        # If target is found, return the index 
        if nums[mid] == target:
            ind = mid
        
        # Else if nums[mid] > target, search is left space 
        elif nums[mid] > target:
            ind = self.func(nums, low, mid-1, target)
        
        # Else search in right space
        else:
            ind = self.func(nums, mid+1, high, target)

        return ind  # Return the index 

    # Function to find the given target in a sorted array
    def search(self, nums, target):
        n = len(nums)
        
        # Find the target in the whole array
        return self.func(nums, 0, n-1, target)
