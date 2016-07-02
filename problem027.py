from pe_utils import sieve

primes = set(sieve(10 ** 6))


best = 0
best_score = 0
for a in xrange(-1000, 1000):
	for b in xrange(-1000, 1000):

		c = 0
		for n in xrange(1000):
			if n ** 2 + a*n+b in primes:
				c += 1
			else:
				break

		if c > best_score:
			best = (a, b)
			best_score = c


print best[0] * best[1]