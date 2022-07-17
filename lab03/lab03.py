from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    counter = 0 

    for i in range(0, 10): # 0 <= i <= 9
        if has_digit(n, i): 
            counter += 1

    return counter 

def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    "*** YOUR CODE HERE ***"

    while n > 0:
        digit = n % 10
        if digit == k:
            return True
        n //= 10 # check whether can change the value of n

    return False 


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"

    while x // 10 > 0: # from leftmost digit to the second one // as long as the next digit exists 
        cur_digit, next_digit = x % 10, (x // 10) % 10
        if cur_digit < next_digit:
            return False
        x //= 10       
    return True

def get_k_run_starter(n, k):
    """
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    i = 0
    final = None
    while i <= k:  # add stop point
        #find i_th chunck # loop until cur_digit <= next_digit (cur_digit -> final)
        while (n % 10) > ((n // 10) % 10) and ((n // 10) > 0): # add stop point, ##! and next one exists + n // 10 > 0 
            n //= 10
        final = n % 10
        i = i + 1 
        n = n // 10  ##! once find the 0th digit, cut it off and start with the rest 
    return final

def make_repeater(func, n):  #(return a func f)
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"
    # def apply_to(x):
    #     def helper(func, x, n):
    #         if n == 0:
    #             return x
    #         result = func(x) #take n as an input and the next value is func(n)
    #         return helper(func, result, n-1)
    #     return helper(func, x, n)
    # return apply_to

    ## Alternative
    # apply func to x n times == apply func to x (n-1) times and then apply func to it

    if n == 0:
        return identity
    else:
        def composer(func1, func2):
            """Return a function f, such that f(x) = func1(func2(x))."""
            def f(x):
                return func1(func2(x))
            return f

        return composer(func, make_repeater(func, n-1))

def apply_twice(func):
    """ Return a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    return make_repeater(func, 2)


def protected_secret(password, secret, num_attempts):
    """
    Returns a function which takes in a password and prints the SECRET if the password entered matches
    the PASSWORD given to protected_secret. Otherwise it prints "INCORRECT PASSWORD". After NUM_ATTEMPTS
    incorrect passwords are entered, the secret is locked and the function should print "SECRET LOCKED".

    >>> my_secret = protected_secret("correcthorsebatterystaple", "I love UCB", 2)
    >>> my_secret = my_secret("hax0r_1") # 2 attempts left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("correcthorsebatterystaple")
    I love UCB
    >>> my_secret = my_secret("hax0r_2") # 1 attempt left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("hax0r_3") # No attempts left
    SECRET LOCKED
    >>> my_secret = my_secret("correcthorsebatterystaple")
    SECRET LOCKED
    """
    def get_secret(password_attempt):
        "*** YOUR CODE HERE ***"
        if password_attempt == password and num_attempts > 0:
            print(secret)
            return protected_secret(password, secret, num_attempts)
        elif password_attempt != password and num_attempts > 0:
            print('INCORRECT PASSWORD')
            return protected_secret(password, secret, num_attempts - 1)
        else:
            print('SECRET LOCKED')
            return protected_secret(password, secret, num_attempts)
    return get_secret








