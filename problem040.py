from operator import mul

x = ""
c = 1
while len(x) < 10 ** 6:
	x = "".join(map(str, xrange(10**c)))
	c += 1

print reduce(mul, (int(x[10**i]) for i in xrange(7)))