pals = []
for i in xrange(999, 100, -1):
	for j in xrange(999, 100 , -1):
		x = i * j
		if str(x) == str(x)[::-1]:
			pals.append(x)
			break

print max(pals)
