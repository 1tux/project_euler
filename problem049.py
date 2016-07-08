from pe_utils import sieve

primes = sieve(10 ** 4)
primes_set = set(primes)

for p in primes:
	if p < 10 ** 3:
		continue
	if p > 10 ** 4:
		break

	for diff in xrange(10 ** 3, 5*10 ** 3):
		if p + diff in primes_set and p + diff + diff in primes_set:
			if sorted(str(p)) == sorted(str(p+diff)) == sorted(str(p+diff+diff)):
				print p, p+diff, p+diff+diff,diff