arr = [1,567,1,1]

# answer 0:
# n = len(arr)
# r = range(0, n)
# def f0(i, j):
# 	if i == j:
# 		return arr[i]
# 	return max(arr[i] + s0(i + 1, j), arr[j] + s0(i, j - 1))

# def s0(i, j):
# 	if i == j:
# 		return 0
# 	return min(f0(i + 1, j), f0(i, j - 1))

# print max(f0(0, n - 1), s0(0, n - 1))

# answer 1:
n = len(arr)
r = range(0, n)
ff = [[-1 for _ in r] for _ in r]
ss = [[-1 for _ in r] for _ in r]
def f(i, j):
	if i == j:
		ff[i][i] = arr[i]
		return arr[i]
	v1 = ss[i + 1][j] if ss[i + 1][j] != -1 else s(i + 1, j)
	v2 = ss[i][j - 1] if ss[i][j - 1] != -1 else s(i, j - 1)
	ff[i][j] = max(arr[i] + v1, arr[j] + v2)
	return ff[i][j]

def s(i, j):
	if i == j:
		ss[i][j] = 0
		return 0
	v1 = ff[i + 1][j] if ff[i + 1][j] != -1 else f(i + 1, j)
	v2 = ff[i][j - 1] if ff[i][j - 1] != -1 else f(i, j - 1)
	ss[i][j] = min(v1, v2)
	return ss[i][j]

print max(f(0, n - 1), s(0, n - 1))
# print '----------'
# for i in r:
# 	print ff[i]
# print '----------'
# for i in r:
# 	print ss[i]
# print ''
# print ''


# answer 2:
n = len(arr)
r = range(0, n)
f = [[0 for _ in r] for _ in r]
s = [[0 for _ in r] for _ in r]
for j in r:
	for i in range(j - 1, -1, -1):
		f[i][j] = max(arr[i] + s[i + 1][j], arr[j] + s[i][j - 1])
		s[i][j] = min(f[i + 1][j], f[i][j - 1])
print max(f[0][n - 1], s[0][n - 1])

# print '----------'
# for i in r:
# 	print ff[i]
# print '----------'
# for i in r:
# 	print ss[i]