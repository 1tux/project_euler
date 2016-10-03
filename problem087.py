from math import log
from pe_utils import sieve
N = 50*10**6
primes = sieve(int(N**0.5)+1)
primes2 = sieve(int(N**0.34)+1)
primes3 = sieve(int(N**0.25)+1)

print log(len(primes), 2)
print log(N, 2)

t = 0
x = set()
for a in primes:
	a_q = a**2
	for b in primes2:
		#if b > a:
		#	break
		b_q = b**3
		for c in primes3:
			#if c > b:
			#	break
			y =a_q+b_q+c**4 
			if y < N:
				#print a,b,c, a_q,b_q, a_q+b_q+c**4
				t += 1
				x.add(y)
			else:
				break

print len(x)