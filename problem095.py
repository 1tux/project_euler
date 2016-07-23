from math import sqrt
from pe_utils import sieve
primes_set = set(sieve(10 ** 5))
print "got primes"

def sum_divs(x):
    if x in primes_set:
	    return 1 + x
    divs = [1]
    for i in xrange(2, int(sqrt(x))+1):
        if x % i == 0:
            divs.append(i)
            divs.append(x/i)
    return sum(set(divs))

cache = {}

def chain(n, l = list()):

	''' for each number cache[n] returns a list '''

	if n in cache:
		return cache[n]

	l2 = list()
	while
	new_n = sum_divs(n)

	#print n, l
	if n > 10 ** 6:
		for x in l:
			cache[x] = []
		return False

		if l and n == l[0]: # found a circle!
		cache[n] = l
		return l

	if n in cache:
		if cache[n] and n == cache[n][0]:
			return cache[n]
		return []

	if n in l:
		cache[n] = l
		return []

	cache[n] = chain(new_n, l + [n])
	return cache[n]

for i in xrange(1, 10**5):
	x = chain(i)

