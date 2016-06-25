N = 100
sqare_of_sum = sum([i for i in xrange(N+1)]) ** 2
sum_of_square =  sum([i ** 2 for i in xrange(N+1)])

print sqare_of_sum - sum_of_square

# O(n)
# there might be an O(1) solution by solving the equation of sum of squares ...