class Solution:
    def countOccurrences(self, arr, target):
        n = len(arr)
        count = 0
        for i in range(n):
            if(arr[i]==target):
                count +=1
        return count    