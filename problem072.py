from pe_utils import sieve2, get_prime_factors, is_prime

primes = sieve2(10 ** 6 + 2)
print "sieve created"

def phi_n(n):

	res = n
	been = []
	for p in set(get_prime_factors(n, primes)):
		res /= p
		res *= p-1
	return res

def main():
	c = 0
	LIM = 10**6
	for d in xrange(2, LIM+1):
		c += phi_n(d)

	print c

main()