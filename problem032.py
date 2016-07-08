from math import factorial
import itertools

def digits_to_num(seq):
	num = 0
	for i in seq:
		num = num*10+i
	return num

s = set()
for i in itertools.permutations(xrange(1, 10)):

	for b in xrange(1, 3):
		for c in xrange(b, 6):
			a1 = digits_to_num(i[:b])
			a2 = digits_to_num(i[b:c])
			if a2 < a1:
				continue
			a3 = digits_to_num(i[c:])
			if a1 * a2 == a3:
				print a1, a2, a3
				s.add(a3)
print sum(s)