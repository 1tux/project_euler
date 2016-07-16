def sieve(n):

	nums = range(2, n)
	primes = []
	for i in nums:
		if i != 0:
			primes.append(i)
			for j in xrange(2, ((len(nums)+1) / i) + 1):
				nums[i*j - 2] = 0
	return primes

def gcd(a,b):
	if not b:
		return a
	return gcd(b, a%b)

def sieve2(n):

	nums = range(2, n)
	primes = []
	cur_index = 2
	for i in nums:
		if i == cur_index:
			primes.append(i)
			for j in xrange(2, ((len(nums)+1) / i) + 1):
				nums[i*j - 2] = i
		cur_index += 1
	return nums

def get_prime_factors(n, sieve_res):
	divs = []
	while n > 1:
		d =  sieve_res[n-2]
		n /= d
		divs.append(d)
	return divs


from random import randrange

def __surely_composite(n, d, s, a):
    'n-1 == 2**s * d'
    x = pow(a, d, n) # a^d mod n, efficiently        
    if x == 1 or x == n - 1:
        return False
    for _ in range(s):
        x = pow(x, 2, n)
        if x == 1: return True
        if x == n - 1: return False
    return True

def miller_rabin(n, number_of_rounds):    
	''' return True for prime '''
	(d, s) = n - 1, 0
	while d % 2 == 0:
	  	(d, s) = (d//2, s+1)
    
	for round in range(number_of_rounds):
		if __surely_composite(n, d, s, randrange(2, n - 1)):
			return False
	return True

primes_set = None
def is_prime(x, primes = None):
	global primes_set
	if not primes and not primes_set:
		primes_set = set(sieve(10 ** 5))
	if primes_set and not primes:
		primes = primes_set
	if x in primes:
		return True
	return miller_rabin(x, 10)

def n_choose_k(n, k):
	from math import factorial as f
	return f(n) / (f(k) * f(n-k))