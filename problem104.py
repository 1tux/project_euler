from itertools import permutations
def digits_to_num(seq):
	num = 0
	for i in seq:
		num = num*10+i
	return num

pandigrals = set(map(digits_to_num, permutations(xrange(1,10))))
#print "created"
a = 1
b = 1
a2 = 1
b2 = 1
c = 1
#POWERS_OF_TWO = [2**i for i in xrange(30)]
while True:
	c += 1
	a, b = b, a+b
	a2, b2 = b2, a2+b2

	a = a % 10 **9

	while a2 > 10 ** 18:
		a2 /= 10
		b2 /= 10

	if a in pandigrals:
		if int(str(a2)[:9]) in pandigrals:
			print a, str(a2)[:9]
			print "result:", c
			break