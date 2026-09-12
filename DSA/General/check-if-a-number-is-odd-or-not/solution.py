class Solution:
    def isOdd(self, n: int) -> bool:
        nums = n & 1
        if (nums !=0):
           return True
        else: return False   