from pe_utils import gcd 

# foreach d:
#    starts with x = d/3 and end with d/2:
#    	write all the foriegn numbers of d

def main():
	c = -2
	N = 12000 # todo: change to 12000
	pot = [2**i for i in xrange(20)]
	for d in xrange(1,N+1):
		if d in pot:
			print d
		for x in xrange(d/3,d/2+1):
			if x and gcd(d, x) == 1 and 2*x<=d<=3*x:
				# print "%d/%d" % (x,d)
				c += 1

	print c

# runs faster with pypy (1.6 seconds)
import time
t = time.time()
main()
print time.time() - t