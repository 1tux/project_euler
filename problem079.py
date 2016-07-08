l = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716""".splitlines()

#l = sorted(l)

l2 = set([y for x in l for y in x])
digits = sorted("".join(l2))
code = ''
for i in xrange(len(digits)):

	for guess in digits:
		if guess in code:
			continue
		flag = True
		for x in l:
			if guess == x[1] and x[0] not in code:
				flag = False
				break
			if guess == x[2] and (x[0] not in code or x[1] not in code):
				flag = False
				break
		if flag == True:
			code += guess
			break
print code