INF = 1 << 30
class Solution(object):
	def minimumTotal(self, triangle):
		"""
		:type triangle: List[List[int]]
		:rtype: int
		"""
		n = len(triangle)
		if n == 0:
			return 0
		dp = [[INF for _ in range(0, n)] for _ in range(0, n)]
		dp[0][0] = triangle[0][0]
		for i in range(1, n):
			for j in range(0, i + 1):
				dp[i][j] = triangle[i][j] + min(dp[i - 1][j], INF if j == 0 else dp[i - 1][j - 1])
		ans = INF
		for i in range(0, n):
			ans = min(ans, dp[n - 1][i])
		return ans


print Solution().minimumTotal([])
print Solution().minimumTotal([[-10]])
print Solution().minimumTotal([[2], [3,4], [6,5,7], [4,1,8,3]])