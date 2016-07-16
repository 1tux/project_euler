from itertools import dropwhile, count, ifilter

def bad_number(x):

	main_set = set(str(x))

	for i in xrange(2, 7):
		if main_set != set(str(x*i)):
			return True
	return False

print dropwhile(bad_number, count(1)).next()