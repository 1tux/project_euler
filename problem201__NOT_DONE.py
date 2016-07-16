elements = [i**2 for i in xrange(1, 101)]
#elements = [1, 3, 6, 8, 10, 11]

from pe_utils import n_choose_k

U = 50
#U = 3
S = [e * n_choose_k(len(elements)-1, U-1) for e in elements]
print sum(S)
print n_choose_k(100, 50)