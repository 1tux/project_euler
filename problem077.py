cache = {}
from pe_utils import sieve
primes = sieve(10 ** 4)

def solve(n, k = 1):

	if n == 0:
		return 1
	if n < 0 or n < k:
		return 0
	if (n,k) not in cache:
		x = 0
		for i in primes:#xrange(k, n+1):
			if i < k:
				continue
			if i > n+1:
				break
			x += solve(n-i, i)
		cache[(n,k)] = x

	return cache[(n, k)]

res = 0
i = 0
while res <= 5000:
	i += 1
	res = solve(i)

print i, solve(i)