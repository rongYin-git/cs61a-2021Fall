def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***" ## try (5, 1) result = 5
    result = 1
    if k == 0:
        return result
    while k > 0:
        result = result * n
        k, n = k - 1, n -1
    return result

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    result = 0
    number = y
    while number > 0:
        digit = number % 10
        number = number // 10
        result += digit
    return result 

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    holder1 = False
    holder2 = False
    result = holder1 and holder2

    while n > 0:
        digit = n % 10
        if digit == 8:
            holder1 = holder2
            holder2 = True
            if (holder1 and holder2) is True:
                return True
        else: 
            holder1 = holder2
            holder2 = False
        n = n // 10

    return False















