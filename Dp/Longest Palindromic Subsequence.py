class Solution(object):
	def longestPalindromeSubseq(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		n = len(s)
		if n == 0: return 0
		dp = [[1] * n for i in range(n)]
		for k in range(1, n):
			for i in range(0, n - k):
				j = i + k
				if s[i] == s[j]:
					dp[i][k] = (0 if i + 1 > j - 1 else dp[i + 1][k - 2]) + 2
				else:
					dp[i][k] = max(dp[i][k - 1], dp[i + 1][k - 1])
		# for i in range(n): print dp[i]
		return dp[0][n - 1]

print Solution().longestPalindromeSubseq('')
print Solution().longestPalindromeSubseq('aba')
print Solution().longestPalindromeSubseq('bbbab')
print Solution().longestPalindromeSubseq('cbbd')
print Solution().longestPalindromeSubseq("dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")