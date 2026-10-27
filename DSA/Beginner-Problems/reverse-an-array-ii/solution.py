class Solution:
    def reverseArray(self, nums):
        #your code goes here
        l = 0
        r = len(nums)-1
        def reverse(l, r):
            if l >= r:
                return

            nums[l], nums[r] = nums[r], nums[l]

            reverse(l + 1, r - 1)

        reverse(l, r)
        return nums
            
