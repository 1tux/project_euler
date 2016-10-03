from fractions import Fraction as F
from pe_utils import sieve
from math import sqrt

MAX_LEN = 2800

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b,a%b)

def sqrt_to_list(n, verbose=False):
	digits = []
	been = {}

	# represent as mone / sqrt(n) - mechane
	g = 1
	mone    = 1
	mechane = -int(sqrt(n))
	digits.append(abs(mechane))
	old_mone = 1

	for i in xrange(1,MAX_LEN):
		# multiplying with zamood
		if verbose:
			print "1.",mone,mechane
		old_mone = mone
		#if mone == 0:
		#	old_mone = mone = 1
		#else:
		mone = mone * (-mechane)
		mechane = n - (mechane)**2
		if verbose:
			print "2.",mone,mechane

		g = gcd(old_mone, gcd(mone, mechane))
		if g > 1:
			mone /= g
			mechane /= g
			old_mone /= F(g)

		if mechane == 0:
			return digits

		#if old_mone==0:
		#	old_mone += 1
		#	digits.append((old_mone*int(sqrt(n))+mone) / mechane)
			#mone += 1
		#else:
		#print old_mone
		digits.append(int((old_mone*int(sqrt(n))+mone) / mechane))
	#	print digits
		mone = mone - mechane * digits[-1]
		if verbose:
			print "3.",old_mone, mone,mechane
		mone, mechane = mechane, mone
		if verbose:
			print ""

		if (mone,mechane,old_mone) in been:
			return digits
		been[(mone,mechane,old_mone)] = 1
		#first_digits = digits[1:i+1]
		#last_digits = digits[-i:]
		#if i > 3 and first_digits == last_digits:
			#print first_digits, last_digits
		#	return digits
		#print last_digits, first_digits
	return None
	return digits

def get_period_length(l1):
	#if len(l1) != MAX_LEN+1:
	#	return 1

	l2 = l1[1:]
	for i in xrange(1, MAX_LEN/2):
		flag = True
		for j in xrange(i):
			if len(set(l2[j::i])) != 1:
				flag = False
				break
		if flag:
			return i

#print sqrt_to_list(23)
#print sqrt_to_list(8)

def create_fraction_from_list(l1,start=1):
	
	if len(l1) == 1:
		return F(0)

	l2 = l1

	add = 0
	if start:
		l2 = l1[1:-1]
		add = F(l1[0])
		if len(l2) == 1:
			return add+1/F(l2[0])
	return add+F(1)/(F(l2[0])+create_fraction_from_list(l2[1:],0))


def solve_eq(D, m = 1):
	l = sqrt_to_list(D)
	l = [l[0]] + l[1:] + l[i:m]
	f = create_fraction_from_list(l)
	x, y = f.numerator, f.denominator
	return x,y

powers = set(i**2 for i in xrange(40))
primes = set(sieve(10000))

x = (0, 0)
for i in xrange(10000+1):
	if i in powers or i not in primes:
		continue

	s = solve_eq(i)
	# x = max((s[0], i), x)
	m = 1
	xk = s[0]
	yk = s[1]
	n = i
	if xk**2-n*yk**2 != 1: # fix for the case the result is -1
		xk, yk = s[0]*xk+n*s[1]*yk, s[1]*xk+s[0]*yk
	assert xk**2-n*yk**2 == 1

	x = max(x, (xk,i))

print x

#print sqrt_to_list(53)
#print create_fraction_from_list(sqrt_to_list(661))

