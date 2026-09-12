class Solution:
    def countSetBits(self,n: int) -> int:
        count = 0
        for i in range((len(bin(n))-2)):
            if (n & (1 << i)):
                count +=1
        return count    
