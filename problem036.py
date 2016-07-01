s = 0
for i in xrange(10 ** 6):

	stri = str(i)
	bini = bin(i)[2:]
	if stri == stri[::-1] and bini == bini[::-1]:
		s += i


print s