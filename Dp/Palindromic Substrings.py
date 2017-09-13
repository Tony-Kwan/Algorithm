class Solution(object):
	def countSubstrings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		n = len(s)
		r = range(0, n)
		f = [[True if i == j or j < i else False for j in r] for i in r]
		for k in range(1, n):
			for i in range(0, n - k):
				j = i + k
				if s[i] != s[j]:
					f[i][j] = False
				else:
					f[i][j] = f[i + 1][j - 1]
					
		ans = 0
		for i in r:
			for j in range(i, n):
				ans += 1 if f[i][j] else 0
		return ans

print Solution().countSubstrings('abc')
print Solution().countSubstrings('aaa')
print Solution().countSubstrings('abcba')