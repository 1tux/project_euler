from pe_utils import sieve


def count_digits(n):
	from math import log
	return int(log(n, 10)) + 1

primes2 = sieve(10 ** 6)
primes = set(primes2)
print "ready"
digits = range(1, 10, 2) + [2]
found = range(1, 10, 2) + [2]

def is_trunc(n):

	bkp_n = n
	while n > 1:
		if n not in primes:
			return False
		n /= 10
	n = bkp_n
	while n > 1:
		if n not in primes:
			return False
		n = n % 10 ** (count_digits(n)-1)

	return bkp_n % 10 != 1 and str(bkp_n)[0] != "1"# / 10 ** (count_digits(bkp_n)-1) != 1
	return True


while len(set(found)) < 11:

	for next_ in primes2:
		flag = False
		for f in found:
			
			new_number1 = f * 10 + next_
			#print new_number1
			#new_number2 = int(str(next_) + str(f))

			if is_trunc(new_number1) and new_number1 not in found:
				found.append(new_number1)
				flag = True
			#if is_trunc(new_number2):
			#	found.append(new_number2)
			#print found
	if not flag:
		break

print sum(list(set(found) ^ set(digits)))
print list(set(found) ^ set(digits))

#print is_trunc(3797)