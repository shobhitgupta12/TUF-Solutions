class Solution:
    def checkIthBit(self, n: int, i: int) -> bool:
        ans = n & (1 << i)

        if ans != 0:
            return True
        else:
            return False