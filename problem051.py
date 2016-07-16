from pe_utils import sieve
from itertools import combinations
N = 10 ** 6
primes = sieve(N)
primes_set = set(primes)

def digit_len(n):
	return len(str(n))

def change_num_dig(num, dig, val):
	num2 = num
	for i in xrange(1, dig):
		num2 /= 10
	cur_val = num2 % 10

	dif = cur_val - val
	num = num - dif * pow(10, dig-1)
	return num

def apply_mask(n, comb, val, best_c=10):
	p2 = n
	for x in comb:
		p2 = change_num_dig(p2, x+1, val)
	return p2


def prime_digit_replace(p, comb, best_c=10):
	c = 0
	for k in xrange(0, 10):
		p2 = apply_mask(p, comb, k) 
		if p2 in primes_set and p2 >= p:
			c += 1
		if c + (10-k) < best_c: #doesn't matter can't bypass best
			return c 
	return c

def gen_list_of_primes(p, comb):
	l = []
	c = 0
	for k in xrange(0, 10):
		p2 = apply_mask(p, comb, k) 
		if p2 in primes_set and p2 >= p:
			c += 1
			l.append(p2)
	return l

def main():
	best_c = 0
	best_p = 2
	c = 0

	for p in primes:
		dig_len = digit_len(p)
		for i in xrange(1, dig_len):
			for j in combinations(xrange(dig_len), i):
				c = prime_digit_replace(p, j, best_c)
				if c > best_c:
					best_c = c
					best = gen_list_of_primes(p, j)[0]
					print "found new best f(%d)=%d" % (best, c)
				if c == 8:
					return best

if __name__ == "__main__":

	print digit_len(13) == 2
	print change_num_dig(300, 3, 5) == 500
	print "found! num is %d" % main()

#import cProfile as profile
#profile.run("main()")