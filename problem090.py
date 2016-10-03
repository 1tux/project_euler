from itertools import combinations_with_replacement as combinations
from itertools import combinations
from itertools import product

good_vals = [(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(4,9),(4,6),(1,8)]
def good_cubs(a, b):

	results = list(product(a, b))
	# print results
	
	for g in good_vals:
		if g not in results and g[::-1] not in results:
			return False
	return True


cube1_opts = list(combinations(xrange(10), 6))
cube2_opts = list(combinations(xrange(10), 6))
print "got cube1 options", len(cube1_opts)
c = 0

saw = {}
for cube1 in cube1_opts:
	cube1 = list(cube1)
	c1 = tuple(sorted(cube1))
	if 6 in cube1 and 9 not in cube1:
		cube1.append(9)
	if 9 in cube1 and 6 not in cube1:
		cube1.append(6)
	for cube2 in cube2_opts:
		flag = True
		cube2 = list(cube2)
		c2 = tuple(sorted(cube2))
		if (c1, c2) in saw or (c2, c1) in saw:
			continue
		if 9 in cube2 and 6 not in cube2:
			cube2.append(6)
		if 6 in cube2 and 9 not in cube2:
			cube2.append(9)
		if good_cubs(cube1, cube2):
			saw[(c1, c2)] = 1
			saw[(c2, c1)] = 1
			c += 1

print c