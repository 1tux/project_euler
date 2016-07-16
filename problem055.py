def is_lyrical(new_n, c=0):

	if c > 60:
		return True

	reveresed_n_str = str(new_n)[::-1]
	if reveresed_n_str == str(new_n) and c:
		return False

	reversed_n = int(reveresed_n_str)
	return is_lyrical(reversed_n + new_n, c+1)


print len(filter(is_lyrical, xrange(10000)))

