from pe_utils import sieve2
from math import sqrt

N = 10 ** 4
primes = sieve2(N)

def get_divs(x):
	divs = [1]
	for i in xrange(2, int(sqrt(x))+1):
		if x % i == 0:
			divs.append(i)
			divs.append(x/i)
	return divs

def d(x):
	return sum(get_divs(x))

y = []
for i in xrange(1, N):
	x = d(i)
	if d(x) == i and x != i:
		print "found pair", x, i
		y.append(i)

#print d(220)

#print d(220)
print y
print sum(y)
