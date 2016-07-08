LIM = 10**5
triangles = set(i*(i+1)/2 for i in xrange(LIM))
penta = set(i*(3*i-1)/2 for i in xrange(LIM))
hexa  = set(i*(2*i-1) for i in xrange(LIM))

print (triangles & penta & hexa) ^ set((0, 1, 40755))