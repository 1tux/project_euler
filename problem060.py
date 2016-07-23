from pe_utils import sieve, is_prime
import itertools

primes = sieve(8400)
primes_set = set(sieve(10 ** 6))
set_size = 5
print "got primes"

def merge(a, b):
	return int(str(a) + str(b)) 

def all_primes(chain, p):
	for x in chain:
		if not is_prime(merge(x, p), primes_set) or not is_prime(merge(p, x), primes_set):
			return False
	return True

def make_chain(chain):
    if len(chain) == set_size:
        return chain 
    for p in primes:
        if p > chain[-1] and all_prime(chain+[p]):
            new_chain = make_chain(chain+[p])
            if new_chain:
                return new_chain
    return False  
        
def all_prime(chain):
    return all(is_prime(int(str(p[0]) + str(p[1])), primes_set) for p in itertools.permutations(chain, 2))

chain = 0
while not chain:
    chain = make_chain([primes.pop(0)])

print "Project Euler 60 Solution =", sum(map(int, chain)), chain