
#Q1
def multiply(m, n):
	""" Takes two positive integers and returns their product using recursion.
	>>> multiply(5, 3)
	15
	"""
	"*** YOUR CODE HERE ***"
	# base case
	if n == 1:
		return m
	return m + multiply(m, n-1)

#Q4
def is_prime(n):
	"""Returns True if n is a prime number and False otherwise.

	>>> is_prime(2)
	True
	>>> is_prime(16)
	False
	>>> is_prime(521)
	True
	"""
	"*** YOUR CODE HERE ***"
	# prime number: divisible only by 1 and itself (n)
	
	def helper(divisor):
		if divisor == 1:
			return True
		elif n % divisor == 0:
			return False
		else:
			return helper(divisor-1)
	return helper(n-1)

#Q5
def hailstone(n):
	"""Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
	>>> a = hailstone(10)
	10
	5
	16
	8
	4
	2
	1
	>>> a
	7
	"""
	"*** YOUR CODE HERE ***"
	# base 
	print(n)
	if n == 1:
		return 1 # count   
	else:
		if n % 2 == 0:
			n //= 2
		else:
			n = n * 3 + 1 
		return 1 + hailstone(n)
#Q6
def merge(n1, n2):
	""" Merges two numbers by digit in decreasing order
	>>> merge(31, 42)
	4321
	>>> merge(21, 0)
	21
	>>> merge (21, 31) 
	3211
	"""
	"*** YOUR CODE HERE ***"
	#base case:
	if n1 == 0:
		return n2
	elif n2 == 0:
		return n1
	else:
		min_dig = min(n1%10, n2%10)
		if min_dig == n1 % 10:
			n1 //= 10
		else:
			n2 //= 10
		return min_dig + 10 * merge(n1, n2) #n1 or n2 needs to be changed based on the previous step












