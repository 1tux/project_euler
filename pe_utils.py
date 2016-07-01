def sieve(n):

	nums = range(2, n)
	primes = []
	for i in nums:
		if i != 0:
			primes.append(i)
			for j in xrange(2, ((len(nums)+1) / i) + 1):
				nums[i*j - 2] = 0
	return primes


def sieve2(n):

	nums = range(2, n)
	primes = []
	cur_index = 2
	for i in nums:
		if i == cur_index:
			primes.append(i)
			for j in xrange(2, ((len(nums)+1) / i) + 1):
				nums[i*j - 2] = i
		cur_index += 1
	return nums

def get_prime_factors(n, sieve_res):
	divs = []
	while n > 1:
		d =  sieve_res[n-2]
		n /= d
		divs.append(d)
	return divs