class Solution:
    def pattern12(self, n):
        for i in range(2,n+2):
            for j in range(1,i):
                print(j,end="")
            for j in range(2*n+2-2*i):
                print(" ",end="")
            for j in range(i-1,0,-1):
                print(j,end="")    
            print()