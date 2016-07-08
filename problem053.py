def n_choose_k(n , k):
	from math import factorial as f
	return f(n) / f(k) / f(n-k)

c = 0
for n in xrange(1, 101):
	for k in xrange(1, n):
		if n_choose_k(n, k) > 10**6:
			c += 1

print c