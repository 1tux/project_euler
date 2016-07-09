cache = {}

def solve(n, k = 1):

	if n == 0:
		return 1
	if n < 0 or n < k:
		return 0
	if (n,k) not in cache:
		x = 0
		for i in xrange(k, n+1):
			x += solve(n-i, i)
		cache[(n,k)] = x

	return cache[(n, k)]

print solve(100) -1