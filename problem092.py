cache2 = {}
def digit_cache(n):
	if n <= 1:
		return n
	if n not in cache2:
		cache2[n] = ((n%10)**2) + digit_cache(n/10)
	return cache2[n]
		

cache = {}
def square_digits(n):
	if n == 89:
		return True
	if n == 1:
		return False
	if n not in cache:
		if n < 9**2 * 9:
			cache[n] = square_digits(digit_cache(n))
		else:
			return square_digits(digit_cache(n))

	return cache[n]

print sum(square_digits(i) for i in xrange(1, 10 ** 7))