from math import log

D = 1000 - 1

x, y = 1, 1
i = 1
while x < 10**D:
	x,y = y, x+y
	i += 1

print i