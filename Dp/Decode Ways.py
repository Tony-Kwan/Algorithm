class Solution(object):
	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		n = len(s)
		if n == 0:
			return 0
		if s[0] == '0':
			return 0
		if n == 1:
			return 1
		if s[1] == '0' and s[0] > '2':
			return 0
		r = range(0, n)
		dp = [0 for _ in r]
		dp[0] = 1
		v = int(s[0:2])
		if v > 26:
			dp[1] = 1
		elif v % 11 == 0:
			dp[1] = 2
		elif v % 10 == 0:
			dp[1] = 1
		else:
			dp[1] = 2
		
		for i in range(2, n):
			if s[i] == '0' and s[i - 1] > '2':
				return 0
			if s[i] != '0':
				dp[i] += dp[i - 1]
			if s[i] <= '6' and s[i - 1] == '2':
				dp [i] += dp[i - 2]
			if s[i - 1] == '1':
				dp[i] += dp[i - 2]
		return dp[n - 1]

print Solution().numDecodings("8176")