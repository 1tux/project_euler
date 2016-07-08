cache = {}
def sum_digits(n, f = lambda x : x):
	if n == 0:
		return f(0)
	if n not in cache:
		cache[n] = sum_digits(n/10) + f(n % 10)
	return cache[n]


biggest = 0
for a in xrange(1, 100):
	for b in xrange(1, 100):
		biggest = max(biggest, sum_digits(a**b))

print biggest