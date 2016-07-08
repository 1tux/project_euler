from pe_utils import is_prime
import itertools

def digits_to_num(seq):
	num = 0
	for i in seq:
		num = num*10+i
	return num
	
found = False
for k in xrange(10):
	if found:
		break
	for i in itertools.permutations(xrange(1, 10-k)):
		n = digits_to_num(i)
		if is_prime(n):
			print n
			found = True