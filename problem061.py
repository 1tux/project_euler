is_4_digit = lambda n: n > 999 and n < 10000

triangles = filter(is_4_digit, [n*(n+1)/2 for n in xrange(10 **5)])
squares =  filter(is_4_digit, [n*n for n in xrange(10 ** 5)])
pentagonals = filter(is_4_digit, [n*(3*n-1)/2 for n in xrange(10 **5)])
hexagonals = filter(is_4_digit, [n*(2*n-1) for n in xrange(10 **5)])
heptagonals = filter(is_4_digit, [n*(5*n-3)/2 for n in xrange(10 **5)])
octagonals = filter(is_4_digit, [n*(3*n-2) for n in xrange(10 **5)])

def find(n, l, options):
	if options == []:
		return l

	possible = []
	for x in xrange(100):
		new_n = (n % 100) * 100 + x
		for opt in options:
			#print "opt", opt
			#print "wtf"
			if new_n in opt:
				new_opts = options[:]
				new_opts.remove(opt)
				x = find(new_n, l + [new_n], new_opts)
				if x:
					possible.append(x)
	if len(possible):
		if len(possible) == 1:
			return possible
		return possible

	#print l
	return False

flatten = lambda l: [y for x in l for y in x]

options = [octagonals, heptagonals, hexagonals, pentagonals, squares, triangles]
for o in options[0]:
	r = find(o, [o], options[1:])
	y = r

	if not y: # if False was returned
		continue
	while list in map(type, y[0]): # extracting all possible outcomes
		y = flatten(y)
	for z in y:
		if z:
			if (z[-1] % 100) == z[0] / 100:
				print sum(z), z