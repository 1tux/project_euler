from math import factorial as f

def n_choose_k(n, k):
	return f(n) / f(k) / f(n-k)


N = 20
print n_choose_k(2*N, N)
