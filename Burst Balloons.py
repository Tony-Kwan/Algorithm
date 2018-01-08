class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        if n == 2:
            return 0
        dp = [[0] * n for _ in xrange(n)]
        for k in xrange(2, n):
            for i in xrange(0, n - k):
                j = i + k
                for u in xrange(i + 1, j):
                    dp[i][j] = max(dp[i][j],dp[i][u] + dp[u][j] + nums[i] * nums[u] * nums[j])
        return dp[0][n - 1]
        

print Solution().maxCoins([2, 3, 4])    #36
print Solution().maxCoins([3, 1, 5, 8])   #167