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
	best = 1
	best_n = 1
	LIM = 10**6
	for n in xrange(2, LIM+1):
		res = float(n) / phi_n(n)
		if res > best:
			best_n = n
			best = res

	print best_n

main()