def sieve(n):

	nums = range(2, n)
	primes = []
	for i in nums:
		if i != 0:
			primes.append(i)
			for j in xrange(2, ((len(nums)+1) / i) + 1):
				nums[i*j - 2] = 0
	return primes


from math import log
N = 10001
p = sieve(N * int(log(N)) * int(log(log(N))))
print p[N-1]
