import itertools

def digits_to_num(seq):
	num = 0
	for i in seq:
		num = num*10+i
	return num

s = 0
primes = [2, 3, 5, 7, 11, 13, 17]
for i in itertools.permutations(xrange(10)):
	n = digits_to_num(i)
	flag = True
	for j in primes:
		if digits_to_num(i[1:4]) % j == 0:
			i = i[1:]
		else:
			flag = False
			break
	if flag:
		print n
		s += n

print s