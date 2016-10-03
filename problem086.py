from pe_utils import gcd
from math import sqrt
import pprint
opt = []
M = 1817

res2 = 0
cache = {}
def solve(M):
	if M in cache:
		return cache[M]
	res = 0
	for m in xrange(1, M):
		for n in xrange(1, m):
			if (m^n)&1 == 1 and gcd(m, n) == 1:
				a, b = m*m-n*n,2*m*n
				if b < a:
					a,b = b,a
				c = m*m+n*n
				for k in xrange(1, M/a+1): 
					for z in xrange(1, min(a*k,b*k/2+1, M+1)):
						if b*k <= M and z <= a*k-z <= b*k:
							res += 1
						if z <= b*k-z <= a*k:
							res += 1
	cache[M] = res
	return res

def main():
	# binary search
	start = 0
	end = 2000
	mid = (end + start) / 2
	while (mid - start) >= 1 or (end-mid) > 1:
		print mid
		if solve(mid) < 10 ** 6:
			start = mid
		else:
			end = mid
		mid = (end + start) / 2

	print "done"
	print mid+1, solve(mid), solve(mid+1)


import time
s = time.time()
main()
print "took:", time.time() - s