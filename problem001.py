def multiples(a1, an):
	n = an / a1
	return ( a1 * (n + 1)) * n / 2

print multiples(3, 999) + multiples(5, 999) - multiples(15, 999)