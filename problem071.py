from fractions import Fraction as f
from pe_utils import gcd

N = 10**5
l = []

best = 0
last_i = 0
last_j = 1
target = f(3, 7)
#dif = f(3, 7) - best
for j in xrange(1, N+1):
	for i in xrange(last_i, last_i+last_i*j/last_j+2):
		if gcd(j,i) != 1:
			continue
		new_f = f(i, j)
		#print i, j, new_f - f(3, 7)
		if new_f > best and new_f < f(3,7):
		#new_dif = f(3, 7) - new_f
		#if new_dif < dif:
			best = new_f
			last_i = i
			last_j = j
			break
		if new_f > target:
			break
		#	dif = new_dif

print best