class Solution(object):
	def integerBreak(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		dp = [0 for _ in range(0, 100)]
		dp[1] = 1
		for i in range(2, n + 1):
			for j in range(1, i):
				dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))
		return dp[n]

print Solution().integerBreak(3)
print Solution().integerBreak(10)
print Solution().integerBreak(58)