map = [
	[-2, -3, 3],
	[-5, -10, 1],
	[0, 30, -5]
]

dp = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]
]

n = len(map) - 1
m = len(map[0]) - 1

dp[2][2] = max(-map[2][2] + 1, 1)
for i in range(n, -1, -1):
	for j in range(m, -1, -1):
		if i == n and j == m:
			continue
		dRight  = 1 << 31 if j + 1 > m else max(1, dp[i][j + 1] - map[i][j])
		dDown = 1 << 31 if i + 1 > n else max(1, dp[i + 1][j] - map[i][j])
		dp[i][j] = min(dRight, dDown)

for i in range(0, len(dp)):
	print dp[i]