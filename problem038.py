cache = {0 : 0}
def count_digits(n):
	if n not in cache:
		cache[n] = count_digits(n / 10)  + 1
	return cache[n]	

cache2 = {}
def get_digits(n, f = lambda x : x):
	if n == 0:
		return []
	if n not in cache2:
		if n >= 1:
			cache2[n] =  get_digits(n / 10) + [f(n%10)]
	return cache2[n]


def digits_to_num(seq):
	num = 0
	for i in seq:
		num = num*10+i
	return num

biggest = 0
for i in xrange(1, 10 ** 5):
	c = 0
	mul = 1
	digits = []
	while c < 9:
		x = i * mul
		c += count_digits(x)
		mul += 1
		digits += get_digits(x)
	if sorted(digits) == sorted(xrange(1, 10)):
		 biggest = max(biggest, digits_to_num(digits))
	
print biggest