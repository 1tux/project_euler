### numbers to letters

digits = ["one",
		"two",
		"three",
		"four",
		"five",
		"six",
		"seven",
		"eight",
		"nine",
		]

teens = ["eleven", "twelve"] + map(lambda x: x+"teen",["thir", "four", "fif", "six", "seven", "eigh", "nine"])
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hunderd"]

def to_letters(n):
	assert n > 0
	if 0 < n < 10 and n > 0:
		return digits[n-1]
	if n > 10 and n < 20:
		return teens[n-11]
	if n % 10 == 0 and n < 100:
		assert n >= 10
		return tens[n/10-1]
	if 20 < n < 100:
		return tens[n/10-1] + to_letters(n%10)
	if n >= 100 and n % 100 == 0 and n < 1000:
		return to_letters(n/100) + "hunderd"
	if n > 100 and  n < 1000:
		return to_letters(n/100) + "hunderd" + "and" + to_letters(n%100) #  + to_letters(n%10)
	if n == 1000:
		return "onethousand"

	print "errr!!!"


if __name__ == "__main__":
	print sum([len(to_letters(i)) for i in xrange(1, 1001)])
	print len(to_letters(342)) == 23
	print len(to_letters(115)) == 20