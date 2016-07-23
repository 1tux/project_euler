c = 0
for i in xrange(1, 10 ** 4):

	for k in xrange(1, 200):
		x = len(str(i ** k)) 
		if x == k:
			c += 1
		if x > k:
			break
print c