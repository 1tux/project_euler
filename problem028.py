from pe_utils import is_prime
s = 1
x = 1
to_add = 2
rate = 1
c = 0
c2 = 0
LIM = 0.1
while rate > LIM:
	for j in xrange(4):
		x += to_add
		if is_prime(x):
			c += 1
		#s += x
		#print x,
	c2 += 4
	to_add += 2
	rate = c / float(c2)

print c2 /2 + 1
print rate, c2, c