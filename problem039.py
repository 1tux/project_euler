d = {}
for P in xrange(1, 1001):
	for a in xrange(1, P):

		if (a**2) % (P-a) == 0:
			if P in d:
				d[P] += 1
			else:
				d[P] = 1

#print max(d.values())
print sorted(d.items(), key=lambda x: x[1])[-1][0]