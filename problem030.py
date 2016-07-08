cache = {}

def sum_digits(n, f = lambda x : x):
	if n == 0:
		return f(0)
	if n not in cache:
		cache[n] = sum_digits(n/10) + f(n % 10)
	return cache[n]

s = 0
for i in xrange(2, 10 ** 6):
	if sum_digits(i, lambda x: x ** 5) == i:
		s += i

print s