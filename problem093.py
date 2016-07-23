import itertools

cache = {}
def compute_max_val(nums, init=0):
	tuple_nums = tuple(nums)
	if tuple_nums in cache:
		return cache[tuple_nums]

	if init==1 and len(nums)==4:
		y = []
		for x in itertools.permutations(nums):
			y += compute_max_val(x)
		return set(filter(lambda z: z >= 0 and int(z) == z, y))
	if len(nums) == 1:
		return [nums[0]]
	vals = []
	for o in "+*-/":
		if o == "+":
			val1 = map(lambda x: x + nums[0], compute_max_val(nums[1:]))
		elif o == "-":
			z = compute_max_val(nums[1:])
			val1 = map(lambda x: x - nums[0], z)
			vals += map(lambda x: nums[0] - x, z)
		elif o == "*":
			val1 = map(lambda x: x * nums[0], compute_max_val(nums[1:]))
		else:
			if nums[0]:
				val1 = map(lambda x: x / float(nums[0]), compute_max_val(nums[1:]))
			val1 += map(lambda x: float(nums[0]) / x, filter(lambda z: z != 0, compute_max_val(nums[1:])))
			#val1 = filter(lambda x: int(x)==x, val1)
		vals += val1
	cache[tuple_nums] = vals
	return vals

all_numbers = set(xrange(9**4)) # 9*9*9*9
def main():

	LIM = 10
	biggest = 0
	res = (0,0,0,0)
	for a in xrange(LIM):
		print a
		for b in xrange(a+1, LIM):
			for c in xrange(b+1, LIM):
				for d in xrange(c+1, LIM):
					r = min(compute_max_val([a,b,c,d], init=1) ^ all_numbers)
					if r > biggest:
						biggest = r
						res = (a,b,c,d)


	print res, biggest

import time
s = time.time()
main()
print time.time() - s