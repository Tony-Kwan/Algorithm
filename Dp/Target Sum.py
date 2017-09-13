class Solution(object):
	def findTargetSumWays(self, nums, S):
		"""
		:type nums: List[int]
		:type t: int
		:rtype: int
		"""
		n = len(nums)
		if n == 0: return 0
		t = sum(nums)
		if S > 1000 or abs(S) > t: return 0
		dp = [[0] * (t * 2 + 1) for _ in range(n)]
		dp[0][nums[0]] += 1
		dp[0][-nums[0]] += 1
		for i in range(1, n):
			u = nums[i]
			for j in range(-t, t + 1):
				# print i, j, u, j - u, (0 if j - u < -t else dp[i - 1][j - u]), j + u, (0 if j + u > t else dp[i - 1][j + u])
				dp[i][j] = (0 if j - u < -t else dp[i - 1][j - u]) + (0 if j + u > t else dp[i - 1][j + u])
		return dp[n - 1][S]


print Solution().findTargetSumWays([1], 2)
print Solution().findTargetSumWays([1,1,1,1,1], 3)
print Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1], 1)
print Solution().findTargetSumWays([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,], 0)