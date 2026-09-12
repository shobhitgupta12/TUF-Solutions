class Solution:

    def helper(self,current,n):
        if current >n:
            return
        print(current)
        self.helper(current+1,n)    
        
    def printNumbers(self,n):
        self.helper(1,n)
    
