class Solution:
    def helperfunc(self,i,num,N):
        if(i>N):
            return num
        else:
            num = i + num
        return self.helperfunc(i+1,num,N)    

    def NnumbersSum(self, N):
        return self.helperfunc(1,0,N)