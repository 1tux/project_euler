LIM = 10**5
LIM2 = int(LIM**0.5)
odds = set(xrange(3, LIM , 2))
from pe_utils import sieve

primes = sieve(LIM)
my_nums = set()
for p in primes:
	for i in xrange(LIM2):
		my_nums.add(p+2*i**2)

print sorted(list(odds - my_nums))[0]
