import itertools

print ''.join(map(str, list(itertools.permutations(xrange(10), 10))[999999]))