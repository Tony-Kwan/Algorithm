class Solution(object):
	def numberOfArithmeticSlices(self, a):
		"""
		:type A: List[int]
		:rtype: int
		"""
		if len(a) < 3:
			return 0
		dif = [a[i] - a[i - 1] for i in range(1, len(a))]
		n = len(dif)
		f = [1 for _ in range(0, n)]
		for i in range(1, n):
			f[i] = 1 if dif[i] != dif[i - 1] else f[i - 1] + 1
		mx = f[0]
		ans = 0
		for i in range(1, n):
			if f[i] < mx:
				ans += mx * (mx - 1) / 2
			mx = f[i]
		ans += mx * (mx - 1) / 2
		return ans


print Solution().numberOfArithmeticSlices([3, 1, 2, 3, 3])
print Solution().numberOfArithmeticSlices([1, 2, 3, 4])