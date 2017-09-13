N = 200
INF = 1 << 31
dp = [[0 if i == j else INF for j in xrange(N)] for i in xrange(N)]
# for i in xrange(N - 1): dp[i][i + 1] = i + 1
# for k in xrange(2, N):
# 	for i in xrange(0, N - k):
# 		j = i + k
# 		for u in xrange(i + 1, j):
# 			dp[i][j] = min(dp[i][j], u + 1 + max(dp[i][u - 1], dp[u + 1][j]))

for 

# for i in xrange(N): print dp[i]

class Solution(object):
	def getMoneyAmount(self, n):
		return dp[0][n - 1]

# print Solution().getMoneyAmount(4)
# print Solution().getMoneyAmount(5)
# print Solution().getMoneyAmount(10)