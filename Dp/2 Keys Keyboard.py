class Solution(object):
	def minSteps(self, n):
		n += 1
		dp = [1 << 31] * 1201
		dp[0] = 0
		dp[1] = 0
		for i in xrange(2, n):
			dp[i] = i
			for j in xrange(i - 1, 1, -1):
				if i % j == 0:
					dp[i] = min(dp[i], dp[j] + i / j)
		return dp[n - 1]			

# print Solution().minSteps(2)
print Solution().minSteps(741)
print Solution().minSteps(49)
