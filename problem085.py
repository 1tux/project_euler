import sys
sys.setrecursionlimit(10000)

from itertools import product

def counting_rect(n, k):
	x = 0
	for a, b in product(xrange(n), xrange(k)):
		x += ((a+1)*(b+1))
	return x

LIM = 2*10**6
best = 0
best_min_2M = abs(best-LIM)
LIM2 = 2000
LAST_LIM = LIM2

for i in xrange(2, LIM2):
	local_best_min_2M = LIM
	for j in xrange(i,LAST_LIM):
		opt = counting_rect(i, j)
		if abs(opt-LIM) < local_best_min_2M:
			local_best_min_2M = abs(opt-LIM)
			LAST_LIM = j
		if abs(opt-LIM) < best_min_2M:
			best = (i, j)
			best_min_2M = abs(opt-LIM)
			#print best_min_2M, best

print best[0] * best[1], best_min_2M