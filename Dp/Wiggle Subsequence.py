class Solution(object):
	def wiggleMaxLength(self, nums):
		n = len(nums)
		if n == 0: return 0
		f = 0
		dp = 1
		for i in xrange(1, n):
			dif = nums[i] - nums[i - 1]
			if dif == 0:
				continue
			elif f == 0 or f * dif < 0:
				dp +=1
				f = dif
		return dp


print Solution().wiggleMaxLength([1,1,1,1,1,1])