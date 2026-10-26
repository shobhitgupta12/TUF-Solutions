class Solution:
    def countOdd(self, arr, n):
        count = 0
        for num in arr:
            if(num%2 == 1):
                count +=1
        return count