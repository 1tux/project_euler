from numpy.polynomial import Polynomial as poly
from numpy import polyfit, polyval

'''
	interpolation:
		given k points I can deduce a polynom that contains the given points...
		this can be done by solving linear equations...

		a_1*x^k+a_2*x^(k-1)+....+a_n = y
		
		setting (x,y) we get linear equations of n variables :)

		numpy implements this using polyfit
	extrapolation:
		having k points of a function i can generate a polynom in K degree that mathes the original function at the given points

'''

def f(n):
	return sum([((-1) ** (i)) * (n**i) for i in xrange(11)])

def g(n):
	return n**3

def poly_val(x, c):
	return sum(c[i]*x**(len(c)-i-1) for i in xrange(len(c)))

deg = 10

#f, deg = g, 3
s = 0
for i in xrange(1,deg+1):
	x = range(1,i+1)
	y = map(f, x)

	z = polyfit(x, y, i-1)
	r = map(round, z)
	#print r
	s += poly_val(i+1, r)

print s