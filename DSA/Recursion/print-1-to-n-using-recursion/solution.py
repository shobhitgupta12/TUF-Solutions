class Solution:
    def helperfunc(self,i,n):
        if (i>n):
           return
        else:
            print(i)

        self.helperfunc(i+1,n)    

    def printNumbers(self, n):
        self.helperfunc(1,n)
        