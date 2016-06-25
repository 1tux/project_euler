def gcd(a,b):
	if not b:
		return a
	return gcd(b, a%b)

s = 1
for i in xrange(20, 0, -1):
	if s % i != 0:
		s *= i / gcd(s, i)

print s


# ^ this algorithm is of O(n * log n) since gcd is log 

# another algorithm is using a sieve to get primes till N
# then finding their exponent using log: log(N, p)
# and multipying them

# but creating the sieve is already n*log(n)*loglog(n) of work.