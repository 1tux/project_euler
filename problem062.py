def perm_uniq(x):

	return "".join(sorted(str(x)))


d = {}
REQ = 5
LIM = 10 ** 5
for i in xrange(LIM):
	p = perm_uniq(i ** 3)
	if p in d:
		d[p].append(i)
		if len(d[p]) == REQ:
			print "found!", d[p], min(d[p]) ** 3
			break
	else:
		d[p] = [i]