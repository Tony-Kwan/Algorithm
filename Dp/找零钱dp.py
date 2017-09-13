INF = 1 << 31

coins = [2, 3, 5]

def f(n):
	if n == 0:
		return 0
	elif n < 0:
		return INF
	m = INF
	for i in range(0, len(coins)):
		v = coins[i]
		m = min(m, f(n - v) + 1)
	return m

print f(9)