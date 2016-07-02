s = 1
x = 1
to_add = 2
N = 1001
for i in xrange(N/2):
	for j in xrange(4):
		x += to_add
		s += x
		#print x,
	to_add += 2

print s