class Solution:
    def printNumbers(self, n):
        if(n==1):
           print(1)
           return
        else:
           print(n)
        self.printNumbers(n-1)