from pe_utils import get_prime_factors, sieve2 as sieve

N = 10 ** 6
k = 3
primes = sieve(N)
a = get_prime_factors(1, primes)
b = get_prime_factors(2, primes)
c = get_prime_factors(3, primes)

for i in xrange(4, N):
	d = get_prime_factors(i, primes)

	#print i, a, b, c
	if len(set(a)) == len(set(b)) == len(set(c)) == len(set(d)) == 4:
		print i-3 # starting from 4 ...
		break
	a,b,c = b,c,d

#print get_prime_factors(8, primes)