from fractions import Fraction as f
from pe_utils import sieve
max_cycle = 1
max_d = 0

primes = sieve(1000)

for d in primes:
	for c in xrange(1, 1000):
		x = f(1, d)
		y = x * (10 ** c) - x
		z = x * (10 ** c)
		if z.denominator == 1: # no cycle
			break
		if y.denominator == 1: # got cycle
			if c > max_cycle:
				max_cycle = c
				max_d = d
			break

print max_d, max_cycle
