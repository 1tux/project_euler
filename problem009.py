'''a**2 + b**2 = c**2

a+b+c=1000

a**2 = c**2-b**2
a**2 = (c-b)(c+b)

a**2 = (c-b)*(c+b) square root is an integer
a**2 = (c-b)*(1000-a) square root is an integer

a**2 / (1000-a) = c-b
a**2 / (1000-a) + a = c-b + a = 1000-2b
a**2 / (1000-a) + a - 1000 = -2b

now we scan a for i in xrange(293) calculates a b
if b is an inetger we are done :)


b**2 = (c-a)*(c+a) square root is an integer too


x+x+y=1000

2x**2=y**2
y = sqrt(2)*x

(2+sqrt(2))x=1000 

so x < 293 :)
'''

for a in xrange(1, 293):

	b = -0.5 * (a ** 2 / (1000 - a) + a - 1000)
	if int(b) == b and b > 0:
		if a**2 + b**2 == (1000-b-a)**2:
			print a, b, (1000 - b-a)
			print a*b*(1000-b-a)