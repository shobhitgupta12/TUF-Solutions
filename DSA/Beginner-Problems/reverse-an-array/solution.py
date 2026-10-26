class Solution:
    def reverse(self, arr: list, n: int) -> None:
        i = 0;
        j = n-1
        for i in range (n//2):
           a = arr[i]
           arr[i] = arr[j-i]
           arr[j-i] = a

        return arr
