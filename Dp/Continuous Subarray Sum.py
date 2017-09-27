class Solution(object):
	def checkSubarraySum(self, nums, k):
		d = {0: -1}
		s = 0
		for i in xrange(len(nums)):
			v = nums[i]
			s += v
			if k != 0:
				s %= k
			if d.has_key(s):
				prevIdx = d[s]
				if i - prevIdx > 1:
					return True
			else:
				d[s] = i
		return False


print Solution().checkSubarraySum([0, 0], 0)