# according to wikipedia
# the formula for P(n) is sum((-1) ** (k-1) p(n-k(3k-1)/2)

LIM = 10 ** 4
penta = sorted([i*(3*i-1)/2 for i in xrange(-LIM, LIM)])[1:]

sign = [1, 1, -1, -1]

cache = {1 : 1}
def p(n):
	if n < 0:
		return 0
	if n == 0:
		return 1
	if n not in cache:
		res = 0
		for k in xrange(1, len(penta)):
			if penta[k-1] > n:
				break
			res += sign[(k-1)%4] * p(n-penta[k-1])
		cache[n] = res % 10 ** 6 # a trick .. we can only work for the last 6 digits :)
	return cache[n]

for i in xrange(1, 10**6):
	if p(i) % 10 ** 6 == 0:
		print i, p(i)
		break


cache2 = {}
def solve(n, k = 1):

	if n == 0:
		return 1
	if n < 0 or n < k:
		return 0
	if (n,k) not in cache2:
		x = 0
		for i in xrange(k, n+1):
			x += solve(n-i, i)
		cache2[(n,k)] = x % 10 ** 6

	return cache2[(n, k)]

for i in xrange(1, 10**6):
	if solve(i) % 10 ** 6 == 0:
		print i, solve(i)
		break
	print i
