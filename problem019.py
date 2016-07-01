import datetime

c = 0
for x in xrange(1901, 2001):
	for y in xrange(1, 13):
		if datetime.date(x, y, 1).weekday() == 1:
			c+=1

print c