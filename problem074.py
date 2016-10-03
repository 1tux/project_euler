MAX_CHAIN = 60

from math import factorial as f
import time
import cProfile

z = lambda x: f(int(x))
def g(n):
	return sum(map(z, str(n)))

cache = {}
def chain_len(n, start, been = []):

	# print n, been
	if len(been) > 60:
		return [False]

	if n in been:
		return len(been)

	if n in cache and n < start:
		return len(been)+cache[n]
	
	#new_been = been[:]
	#new_been.append(n)
	cache[n] = chain_len(g(n),start, been[:]+[n])
	return cache[n]


def main():
	p = [2**i for i in xrange(22)]
	c = 0
	for i in xrange(10 ** 6):
		if i in p:
			print "p", i
		if chain_len(i,i) == 60:
			#print i
			c += 1

	print c

t = time.time()
main()
print time.time() - t