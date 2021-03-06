from fractions import Fraction as F
from math import sqrt

MAX_LEN = 1400

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

def create_fraction_from_list(l1,maxi=100):
	x = F(1)
	l2 = l1[1:-1]
	for i in xrange(maxi+1):
		x = 1/(x + l2[i % len(l2)] )
	opt1 = l1[0] + x

	return opt1

def get_sum_of_digits(f):
	return sum(map(int, str(int(f * 10 ** 100)).replace('L','')[:100]))

def do_all(n, maxi=200):


	l = sqrt_to_list(n)
	f = create_fraction_from_list(l, maxi)
	while abs(f ** 2 - n) > F(0.0000000001):
		maxi += 1
		f = create_fraction_from_list(l, maxi)
	return get_sum_of_digits(f)

#print sqrt_to_list(23)
#print sqrt_to_list(8)
'''
c = 0
N = 10
for i in xrange(1, N+1):
	if int(sqrt(i)) != sqrt(i):
		l = sqrt_to_list(i)
		p = get_period_length(l) 
		if p % 2 == 1:
			c += 1
		print i, l[:p+2], p

print c	
'''
N = 100
x = 0 
print do_all(3)


for i in xrange(1, N+1):
	print i
	maxi = 101
	if int(sqrt(i)) != sqrt(i):
		r = do_all(i)
		x += r
print x

