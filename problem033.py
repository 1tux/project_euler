from fractions import Fraction as f


digits = lambda x: set([x/10, x%10])

def eliminate_digit(i, dig):
	if i % 10 == dig:
		new_i = (i - dig) / 10
	else:
		new_i = i - 10 * dig
	return new_i

def is_unique(nominator, denominator):

	common_digit = digits(nominator) & digits(denominator)
	#print common_digit
	if common_digit:
		common_digit = list(common_digit)[0]
		if common_digit > 0:
			new_nominator = eliminate_digit(nominator, common_digit)
			new_denominator = eliminate_digit(denominator, common_digit)
			if new_denominator and f(nominator, denominator) == f(new_nominator, new_denominator):
				#print f(nominator, denominator)
				return True
	return False



#print is_unique(49, 98)

prod = 1
for i in xrange(10, 100):
	for j in xrange(i+1, 100):
		if is_unique(i, j):
			prod *= f(i, j)

print prod.denominator

				

