from pe_utils import sieve

N = 10 ** 6
primes = sieve(N)
prime_set = set(primes)

c = 0
for i in primes:
	x = str(i)
	if len(x) == 1:
		c += 1
		continue
	if len([z for z in "024568" if z in x]):
		continue

	flag = True
	for j in xrange(len(x)):
		if int(str(x[j:]) + str(x[:j])) not in prime_set:
			flag = False
			break
	if flag:
		c += 1
	

print c