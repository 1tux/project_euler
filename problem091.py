from pe_utils import gcd
import time

N = input('N=? (default is 50): ')
ti = time.time()
t = 0
for i in xrange(0, N+1):
	for j in xrange(0, N+1):

		for i2 in xrange(0, N+1):
			for j2 in xrange(0, N+1):

				if (i,j) == (0,0) or (i2,j2) == (0,0):
					continue
				if (i,j) != (i2,j2):
					d1 = (i**2+j**2)
					d2 = ((j2-j)**2+(i2-i)**2)
					d3 = (i2**2+j2**2)
					d1, d2, d3= max(d1, d2, d3), min(d1, d2, d3), d1+d2+d3
					d3 -= (d1+d2)

					if d1 - d2 == d3:
						#print (i,j), (i2,j2)
						t += 1

# use pypy :o it's quick as hell. like 0.27 seconds
print t/2
print time.time() - ti