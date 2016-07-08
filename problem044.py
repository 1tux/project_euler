LIM = 10**4	
penta = [i*(3*i-1)/2 for i in xrange(1, LIM)]
penta_set = set(penta)

found = False
for p in penta:
	for y in penta:
		if y+p in penta_set and abs(y-p) in penta_set and p-y!=y:
			print abs(p - y)
			found = True
			break
	if found:
		break