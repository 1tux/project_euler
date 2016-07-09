from pe_utils import sieve2, get_prime_factors, is_prime, sieve

primes = None
small_primes = sieve(1000)
print "sieve created"

def phi_n(n):

	res = n
	been = []
	for p in set(get_prime_factors(n, primes)):
		res /= p
		res *= p-1
	return res

def old_main():
	global primes
	prime = sieve2(10 ** 7 + 2)
	best = 5
	best_n = 1
	LIM = 10**7
	for n in xrange(2, LIM+1):
		if any(not n % x for x in small_primes): # for ratio to be smallest we need phi(n) higher so n musn't divide with lot's of primes :)
			continue
		phi = phi_n(n)
		res = float(n) / phi
		if res < best:
			if sorted(str(phi)) == sorted(str(n)):
				best_n = n
				best = res

	print best_n, best

def main():
	global primes
	primes = sieve(10 ** 4)
	best = 5
	best_n = 1
	for p in primes:
		for q in primes:

			n = p * q
			if n > 10 ** 7:
				break

			phi = (p-1) * (q-1)
			res = float(n) / phi
			if res < best:
				if sorted(str(phi)) == sorted(str(n)):
					best_n = n
					best = res

	print best_n, best
main()

# result = 8319823
# print get_prime_factors(8319823, primes)

# after getting the correct result and looking at it primes factors it became clear, in order to N/phi(N) to be the smallest N has to be p1*p2 ...
# this makes the solution way faster!