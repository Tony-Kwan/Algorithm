# class Solution(object):
# 	def PredictTheWinner(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: bool
# 		"""
# 		total = sum(nums)
# 		n = len(nums)
# 		ff = [[None] * n for _ in range(n)]
# 		ss = [[None] * n for _ in range(n)]
# 		p1Max = self.f(nums, 0, n - 1, ff, ss)
# 		return p1Max >= total - p1Max

# 	def f(self, nums, i, j, ff, ss):
# 		if i == j:
# 			ff[i][j] = nums[i]
# 			return nums[i]
# 		s1 = ss[i + 1][j] if ss[i + 1][j] != None else self.s(nums, i + 1, j, ff, ss)
# 		s2 = ss[i][j - 1] if ss[i][j - 1] != None else self.s(nums, i, j - 1, ff, ss)
# 		ff[i][j] = max(nums[i] + s1, nums[j] + s2)
# 		return ff[i][j]

# 	def s(self, nums, i, j, ff, ss):
# 		if i == j:
# 			ss[i][j] = 0
# 			return 0
# 		f1 = ff[i + 1][j] if ff[i + 1][j] != None else self.f(nums, i + 1, j, ff, ss)
# 		f2 = ff[i][j - 1] if ff[i][j - 1] != None else self.f(nums, i, j - 1, ff, ss)
# 		ss[i][j] = min(f1, f2)
# 		return ss[i][j]


class Solution(object):
	def PredictTheWinner(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		total = sum(nums)
		n = len(nums)
		f = [[0] * n for _ in range(n)]
		s = [[0] * n for _ in range(n)]
		for i in reversed(xrange(0, n)):
			for j in xrange(i, n):
				print i, j
				if i == j:
					f[i][j] = nums[i]
					s[i][j] = 0
				else:
					f[i][j] = max(nums[i] + s[i + 1][j], nums[j] + s[i][j - 1])
					s[i][j] = min(f[i + 1][j], f[i][j - 1])
		p1Max = f[0][n - 1]
		return p1Max >= sum(nums) - p1Max

print Solution().PredictTheWinner([1,9,1, 1])
# print Solution().PredictTheWinner([1, 5, 233, 7])
# print Solution().PredictTheWinner([1163573,4225123,1034109,6416120,4401957,408968,8769389,7498770,6003151,2054050,2621821,8204739,2586055,6520977,2014732,4750306,4172182,6965656,1861876,9549339])
