cache = {}
def coins_sum(n, min_=0):

	#print n, min_
	r = 0
	if n == 0:
		return 1
	if n < 0:
		return 0

	if (n, min_) not in cache:
		for i in [1, 2, 5, 10, 20, 50, 100, 200]:
			if i >= min_ and i <= n:
				r += coins_sum(n-i, i)
		cache[(n, min_)] = r

	return cache[(n, min_)]

print coins_sum(200)