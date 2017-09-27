class Solution(object):
	def combinationSum4(self, nums, target):
		n = len(nums)
		if n == 0:
			return 0
		dp = [0] * (target + 1)
		dp[0] = 1
		for i in xrange(1, target + 1):
			for j in sorted(nums):
				if j > i:
					break
				dp[i] += dp[i - j]
		return dp[target]


print Solution().combinationSum4([1, 2, 3], 4)