class Solution:
    def countDigit(self, n):
            cout = 0
            if(n==0):
                cout = 1
            while(n !=0):
                cout = cout+1
                n = n//10
            return cout         
