class Solution(object):
	mod = int(1e9 + 7)

	def findPaths(self, n, m, N, x, y):
		"""
		:type m: int
		:type n: int
		:type N: int
		:type x: int
		:type y: int
		:rtype: int
		"""
		if N == 0:
			return 0
		mat = [[[0 for _ in range(0, m)] for _ in range(0, n)] for _ in range(0, N)]
		mat[0][x][y] = 1
		for k in range(1, N):
			for i in range(0, n):
				for j in range(0, m):
					mat[k][i][j] = self.get(n, m, i - 1, j, k, mat) + self.get(n, m, i + 1, j, k, mat)\
						+ self.get(n, m, i, j - 1, k, mat) + self.get(n, m, i, j + 1, k, mat)

		# for k in range(0, N):
		# 	print '------------------'
		# 	for i in range(0, n):
		# 		print mat[k][i]

		return self.count(n, m, N, mat) % self.mod


	def get(self, n, m, x, y, k, mat):
		if x >= n or x < 0 or y >= m or y < 0:
			return 0
		return mat[k - 1][x][y]

	def count(self, n, m, N, mat):
		ret = 0
		for k in range(0, N):
			for i in range(0, n):
				for j in range(0, m):
					if mat[k][i][j] != 0:
						if i == 0: ret += mat[k][i][j]
						if j == 0: ret += mat[k][i][j]
						if i == n - 1: ret += mat[k][i][j]
						if j == m - 1: ret += mat[k][i][j]
		return ret


# print Solution().findPaths(10, 10, 0 , 5, 5)
# print Solution().findPaths(1, 3, 3, 0, 1)
# print Solution().findPaths(8, 50, 23, 5, 26)
print Solution().findPaths(50, 50, 50, 25, 25)
print Solution().findPaths(50, 50, 50, 0, 0)