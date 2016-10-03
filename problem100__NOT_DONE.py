''' n/y * (n-1)/(y-1) = 1/2
it means that n/y is close to sqrt(2)

n/y > (n-1)/(y-1) as 2/3 > 1/2
'''

from fractions import Fraction as F

F1 = F(1)
F2 = F(2)
F05 = F(0.5)

N = 10**12
def newton(x, goal=2):
	while x.denominator < 2*N:
		x =  x / F2 + F1 / x
	return x



d = {}
z = newton(2)
print z
#a, b = z.denominator, z.numerator
P = 12
a =  int(z * 10 ** P)
print a


print F(2*(10**P)*(2*10**P+1),  ((a) * (a+1)))


'''
	this solution dosn't work :(
'''