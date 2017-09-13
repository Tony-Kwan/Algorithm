class Solution(object):
	def findMaxForm(self, strs, t0, t1):
		n = len(strs)
		if n == 0: return 0
		arr = []
		for s in strs:
			count = sum([int(c) for c in s])
			arr.append((len(s) - count, count))
		t0 += 1
		t1 += 1
		dp = [[0] * t1 for _ in xrange(t0)]
		for t in arr:
			for i in reversed(xrange(t[0], t0)):
				for j in reversed(xrange(t[1], t1)):
					dp[i][j] = max(dp[i][j], dp[i - t[0]][j - t[1]] + 1)
		return dp[t0 - 1][t1 - 1]

		
print Solution().findMaxForm(["10","0001","111001","1","0"], 5, 3)