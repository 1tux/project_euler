from pe_utils import sieve

N = 10 ** 6
primes = sieve(N)
prime_set = set(primes)

print "got primes"

best_length = 0
prime = 0
for i in xrange(len(primes)):
	for j in xrange(best_length+1, len(primes)-i):
		s = sum(primes[i:i+j])
		if s > N:
			break
		if s in prime_set:
			best_length = j
			prime = s

print best_length, prime