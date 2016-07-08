import profile
from math import factorial

table = map(factorial, xrange(10))
def f(n):
	return table[n]

cache = {}
def get_digits(n, f = lambda x : x):
	if n == 0:
		return [f(0)]
	if n not in cache:
		if n >= 1:
			cache[n] = [f(n%10)] + get_digits(n / 10)
	return cache[n]

def sum_digits(n, f = lambda x : x):
	if n == 0:
		return f(0)
	if n not in cache:
		cache[n] = sum_digits(n/10) + f(n % 10)
	return cache[n]

def main():
	s = 0
	for i in xrange(3, factorial(9) * 6):
		if sum_digits(i, f) == i:
			s += i

	print s

main()