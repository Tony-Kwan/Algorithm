class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		n = len(obstacleGrid)
		if n == 0: return 0
		m = len(obstacleGrid[0])
		if m == 0: return 0

		dp = [[0] * m for _ in xrange(n)]
		dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
		for i in xrange(1, n):
			dp[i][0] = min(dp[i - 1][0], 0 if obstacleGrid[i][0] == 1 else 1)
		for j in xrange(1, m): 
			dp[0][j] = min(dp[0][j - 1], 0 if obstacleGrid[0][j] == 1 else 1)
		for i in xrange(1, n):
			for j in xrange(1, m):
				if obstacleGrid[i][j] == 1:
					dp[i][j] = 0
				else:
					dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
		for i in xrange(n): print dp[i]
		return dp[n - 1][m - 1]

print Solution().uniquePathsWithObstacles([[0],[1]])