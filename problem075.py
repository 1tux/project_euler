from pe_utils import gcd
from math import sqrt

'''
algorithm:
	a+b+c=P
	c= P -(a+b)
	a^2+b^2=c^2
	P^2-2P(a+b)+2ab=0
	0.5*P(P-b-b)/(P-b)=a
	P-(P*b)/(P-b)=2a
	(P-2a)=(P*b)/(P-b)

	b should divide P ?!

	-> P | b+1


for each p:
	factorize(P) ....
	take all factors and dec 1 -> b.
	calc a # (0.5*P(P-b-b)/(P-b)=a)
	calc c ! 



'''

c1 = 0
c2 = 0
LIM = 1500000
M = int(sqrt(LIM/2))
#print M
been = {}
for m in xrange(2, M):
	for n in xrange(1, m):
		if ((m+n) % 2) == 1 and gcd(m, n) == 1:
			#q = sqrt(2*m*n)
			#int_q = int(q)
			#if q == int_q:
			if True:
				a, b, c = m*m+n*n, m*m-n*n,2*m*n #int_q+n,int_q+m,int_q+m+n # they are sorted!
				P = a+b+c
				#print P
				while P <= LIM:
					if P not in been:
						been[P]=1
						c1+=1
					else:
						been[P]+=1
						if been[P] == 2:
							c2 += 1
					P += a+b+c
print c1 - c2