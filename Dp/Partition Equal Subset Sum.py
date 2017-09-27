class Solution(object):
	def canPartition(self, nums):
		n = len(nums)
		s = sum(nums)
		if s % 2 == 1:
			return False
		t = s / 2
		st = set()
		st.add(0)
		for num in nums:
			tmpSet = set()
			for j in st:
				tmpSet.add(num + j)
			st.update(tmpSet)
			if t in st:
				return True
		return False

print Solution().canPartition([11, 5, 5, 1])