from itertools import permutations

indexes = [[0,1,2],[9,2,3],[8,3,4],[7,4,5],[6,5,1]]

def p_to_str(p):
	a = [p[j] for i in indexes for j in i]
	smallest_num = min(a[::3])
	b =  ''.join(map(str, a))
	starting_index = b.index(str(smallest_num))
	return b[starting_index:] + b[:starting_index]


def main():

	goods = {}
	for p in permutations(xrange(1,11)):
		sums = []
		flag = True
		old_sum = 0
		for s in indexes:
			if flag:
				x = 0
				for i in s:
					x += p[i]
				if not old_sum:
					old_sum = x
				elif x != old_sum: # not one sum
					flag = False
					break
		if flag:
			# found 
			sp = p_to_str(p)
			if len(sp) == 16:
				goods[sp] = old_sum


	x = max(goods)
	print x, len(x)
	print goods

def example():
	global indexes
	indexes = [[0,1,2],[3,2,4],[5,4,1]]
	goods = {}
	for p in permutations(xrange(1,7)):
		sums = []
		flag = True
		old_sum = 0
		for s in indexes:
			if flag:
				x = 0
				for i in s:
					x += p[i]
				if not old_sum:
					old_sum = x
				elif x != old_sum: # not one sum
					flag = False
					break
		if flag:
			# found 
			sp = p_to_str(p)
			if len(sp) == 9:
				goods[sp] = old_sum


	x = max(goods)
	print x, len(x)
	print goods

main()