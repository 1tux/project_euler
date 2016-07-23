from pe_utils import sieve
from math import sqrt
#primes_set = set(sieve(10 ** 5))
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


def pe95(L = 10**6):
    d = [1] * L
    for i in xrange(2, L/2):
        for j in xrange(i*2, L,i):
            d[j] += i

    max_cl = 0
    for i in xrange(2, L):
        n, chain = i, []
        while d[n] < L:
            d[n], n = L+1, d[n]
            if n in chain:
            	k = chain.index(n)
            	if len(chain[k:]) > max_cl:
                	max_cl, min_link = len(chain[k:]), min(chain[k:])
            else:
            	chain.append(n) 
            
    return min_link

print "Smallest member of the longest amicable chain", pe95()


# calculating sum_of_divs for all x | x < 10 ** 6 is too much work ... 
# should be calculated from down up :)
'''    d = [1] * L
    for i in xrange(2, L/2):
        for j in xrange(i*2, L,i):
            d[j] += i
'''