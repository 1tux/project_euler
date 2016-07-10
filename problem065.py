from fractions import Fraction as F

l = [(1,k,1) for k in xrange(2, 100, 2)]
l = [y for x in l for y in x]

cache = {}
def sum_digits(n, f = lambda x : x):
        if n == 0:
                return f(0)
        if n not in cache:
                cache[n] = sum_digits(n/10) + f(n % 10)
        return cache[n]


def solve(l):
	if len(l) == 0:
		return 0
	return F(1)/(l[0] + solve(l[1:]))

start = 2
LIM = 100
y = start+solve(l[:LIM-1])
print sum_digits(y.numerator)