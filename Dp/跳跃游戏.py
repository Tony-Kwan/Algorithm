INF = 1 << 31

arr = [3, 2, 3, 1, 1, 4]	# ans = 2

cur = 0
next = 0
jump = 0

for i in range(0, len(arr)):
	if cur < i:
		jump += 1
		cur = next
	next = max(next, i + arr[i])
	print '%d: %d, %d, %d' % (i, cur, next, jump)
print jump