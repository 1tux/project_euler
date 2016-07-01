from math import sqrt
def sieve2(n):

	nums = range(2, n)
	primes = []
	cur_index = 2
	for i in nums:
		if i == cur_index:
			primes.append(i)
			for j in xrange(2, ((len(nums)+1) / i) + 1):
				nums[i*j - 2] = i
		cur_index += 1
	return nums



### algorithm:
### get all prime dividors:
### using modified version of sieve2
### the number of divs is the multiplication of the power of the primes
### so for example 28 = 2**2*7*1, so we had:
# 1 = 0, 0
# 2 = 1, 0
# 4 = 2, 0
# 7 = 0, 1
# 14 = 1, 1
# 28 = 2, 1

# this is (2+1)*(1+1)


# another algorithm is to bf over powers of primes so that their multiplication+1 is over 500
# and finding the smallest :)

N = 10 ** 5
sieve2_res = sieve2(N)
k = 500
print "got primes"

def divs_count(n, to_print = False):
#n = 28
	divs = []
	while n > 1:
		d =  sieve2_res[n-2]
		n /= d
		divs.append(d)
	divs_set = set(divs)
	l = [divs.count(i) for i in divs_set]
	if to_print:
		print l
	return reduce(lambda x,y : x * y, map(lambda x: x + 1, l))


def divs_count2(n, to_print = False):
#n = 28
	divs = []
	c = 1
	while n > 1:
		d =  sieve2_res[n-2]
		exp = 1
		while n % d == 0:
			n /= d
			exp += 1

		c *= exp
	return c
 


from time import time
'''
a = time()
for i in xrange(3, int(sqrt(N))):
	x = sum(xrange(i))
	if divs_count(x, 0) > k:
		print x
		break

print time() - a
'''
b = time()
for i in xrange(3, N):
	x = i * (i + 1) / 2

	if i % 2 == 0:
		c = divs_count2(i/2) * divs_count2(i+1) # == divs_count2(i * (i + 1) / 2, 0)
	else:
		c = divs_count2(i) * divs_count2((i+1)/2) # == divs_count2(i * (i + 1) / 2, 0)

	if c > k:
		print "found:", x
		break

print time() - b