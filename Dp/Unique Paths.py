class Solution(object):
	def uniquePaths(self, m, n):
		if m == 0 or n == 0:
			return 0
		n += 1
		m += 1
		dp = [[0] * m for _ in xrange(n)]
		dp[1][1] = 1
		for i in xrange(1, n):
			for j in xrange(1, m):
				if i != 1 or j != 1:
					dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
		# for i in xrange(n): print dp[i]
		return dp[n - 1][m - 1]

print Solution().uniquePaths(3, 7)