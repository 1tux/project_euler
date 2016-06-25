x = set()
N = 100
for a in xrange(2, N+1):
	for b in xrange(2, N+1):
		x.add(a**b)

print len(x)