s = 0
for i in xrange(1, 1001):
	s += pow(i, i, 10**10)
	
s = s % 10 ** 10

print s
print len(str(s))
