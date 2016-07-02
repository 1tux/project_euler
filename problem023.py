from math import sqrt

def get_divs(x):
	divs = [1]
	for i in xrange(2, int(sqrt(x))+1):
		if x % i == 0:
			divs.append(i)
			divs.append(x/i)
	return list(set(divs))

def is_abundant(n):
	return sum(get_divs(n)) > n


def binary_search(l, x):
	start = 0
	end = len(l) - 1
	middle = (start + end) /2
	while abs(start - end) <= 1:
		if l[middle] == x:
			return middle
		elif l[middle] < x:
			start = middle
			middle = (start + end) /2
		else:
			end = middle
			middle = (start + end) /2
	return -1

N = 28123
abundants = filter(is_abundant, xrange(1, N))


def is_sum(l, x):
	'''
		checks if 2 variables on L can be summed to be x 
		O(n) 
	'''
	l2 = set()
	for i in l:
		l2.add(x-i)
	for i in l:
		if i in l2:
			return True
	return False

def is_sum2(setl, x):
	for i in setl:
		if x-i in setl:
			return True
	return False

print len(abundants)
abundants2 = set(abundants)

'''
s = 0
for x in xrange(1, 28123):
	if not is_sum(abundants, x):
		s += x

print s
'''

#print sum(filter(lambda x: not is_sum(abundants, x), xrange(28123)))
print sum(filter(lambda x: not is_sum2(abundants2, x), xrange(28123)))