'''
	the first player loses if n1 ^ n2 ^ n3 = 0
	since any move he does changes the total xor
	and the other player can return the situtation to xor 0
	and the losing position is xor 0 :)

	now in order for n ^ 2n ^ 3n = 0
	meaning n ^ 2n = 3n
	meaning n ^ 2n = n + 2n

	xor is equal to + when no carry so we need:
		n and 2n to have no carry...
		looking at bits
		n = 01001010....
		2n = 1001010....

		so if n has z zero bit, the next bit can be eith {0, 1}
		if n has z one bit, the next bit has to be {1}

	the number of binary lists can be found with this recoursion:
		k is the number of bits:

		f(k) = f(k-1) + f(k-2)
		this is fib :)

		so we need to find the sum of all fib(n) where fib(n) < 2**30

'''

a = 1
b = 1
s = 0
c = 0
N = 30
while c < N:
	c += 1
	s += a
	a, b = b, a+b

print 1+s