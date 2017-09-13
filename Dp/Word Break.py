class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		if len(wordDict) == 0: return False
		n = len(s)
		dp = [False] * n
		for word in wordDict:
			if s[0: 1] == word:
				dp[0] = True
		for i in range(1, n):
			for word in wordDict:
				l = len(word)
				sub = s[i + 1 - l: i + 1]
				if (dp[i - l] or i + 1 - l == 0) and word == sub:
					dp[i] = True
					break
		return dp[n - 1]

print Solution().wordBreak("abcd", ["a","abc","b","cd"])
print Solution().wordBreak('leetcode', ['leet', 'code'])
print Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa", "b"])