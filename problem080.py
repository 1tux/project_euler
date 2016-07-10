from fractions import Fraction as F

def num_digits(n):
	return len(str(n))

n = F(0)
last_n = F(1)
c = 0
for i in xrange(1000):
	n = 1+1/(1+last_n)
	last_n = n

	if num_digits(n.numerator) > num_digits(n.denominator):
		c += 1

s =  "%d" % (n * 10 ** 100)
print sum(map(int,s[:100]))
