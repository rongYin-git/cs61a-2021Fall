#disc 01
#Q1
# First, try solving this problem using an if statement.
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    if temp < 60 or raining:
    	return True
    else:
    	return False
# try to write this function using a single line.
def wears_jacket(temp, raining):
    "*** YOUR CODE HERE ***"
    return temp < 60 or raining
#Q2
def special_case():
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x

special_case()
# Answer: should return 12
def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x

just_in_case()
# Answer: should return 19
def case_in_point():
    x = 10
    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x

case_in_point()
# Answer: should return 12

#Q3
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.
    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 'equal', 'not equal')
    'not equal'
    >>> if_function(3>2, 'bigger', 'smaller')
    'bigger'
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> result = with_if_statement()
    61A
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    Welcome to
    61A
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    "*** YOUR CODE HERE ***"
    False
def true_func():
    "*** YOUR CODE HERE ***"
    print('Welcome to')
def false_func():
    "*** YOUR CODE HERE ***"
    print('61A')

#Q4: Square So Slow
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x=x+1
    return x / 0

square(so_slow(5))
# Answer: stuck in the loop

#Q5: Is Prime?
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    "*** YOUR CODE HERE ***"
    # a prime n % n == 0 and n % 1 == 0 otherwise all != 0
    # if there exists a number between 2 to n-1, and n % number == 0, it is not a prime
	for i in range(2, n):
		if n % i == 0:
			return False
	return True 

#Q6: Fizzbuzz
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result == None
    True
    """
    "*** YOUR CODE HERE ***"
    for i in range(1, n+1): # check n == 1
    	if i % 3 == 0 and i % 5 == 0:
    		print("fizzbuzz")
    	elif i % 3 == 0:
    		print("fizz")
    	elif i % 5 == 0:
    		print("buzz")
    	else:
    		print(i)

























