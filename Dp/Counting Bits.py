class Solution(object):
    def countBits(self, n):
        if n == 0:
            return [0]
        dp = [-1] * (n + 1)
        dp[0] = 0
        for i in reversed(xrange(n + 1)):
            if dp[i] == -1:
                self.f(dp, i)
        return dp

    def f(self, dp, n):
        nn = n & (n - 1)
        if dp[nn] != -1:
            pass
        else:
            self.f(dp, nn)
        dp[n] = dp[nn] + 1


print Solution().countBits(5)