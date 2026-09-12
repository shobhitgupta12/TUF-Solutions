class Solution:

    def helper(self, ans, n):

        if n == 0:
            return ans

        ans = ans * n
        return self.helper(ans, n - 1)

    def factorial(self, n):
        return self.helper(1, n)