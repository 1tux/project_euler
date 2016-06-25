cache = {1 : 1}

def collatz(n):
	global cache
	if n not in cache:
		if n % 2 == 0:
			cache[n] = 1 + collatz(n / 2)
		else:
			cache[n] = 1 + collatz(3 * n + 1)
	return cache[n]

maxi = 1
max_val = 1
for i in xrange(1, 10**6):
	if collatz(i) > max_val:
		maxi, max_val = i, collatz(i)

print maxi