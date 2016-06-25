from math import sqrt

n = 600851475143 
lim = int(sqrt(n)) + 1

for i in xrange(3, lim, 2):
	while n % i == 0:
		n /= i
		print i
		lim = int(sqrt(n)) + 1

