s = 0
x,y = 1, 1
while y < 4 * 10 ** 6:
	if x & 1:
		s += x
	x, y = y, x+y
print s