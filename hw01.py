from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return h(a, b)']
    """
def h(a,b):
    if b >= 0:
        h = add
    else:
        he = sub
    return h(a, b)


def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    sum = x + y + z
    middle = sum - min(x,y,z) - max(x , y, z)
    minimum = min(x,y,z)
    return minimum*minimum + middle*middle

def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    factor  =  x - 1
    while factor > 0:
        if x % factor == 0:
            return factor
        factor = factor - 1
    #另一种写法
    #for i in range(n-1, 0, -1):
     #   if n % i == 0:
      #      return i


def if_function(condition, true_result, false_result):
   
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    return if_function(cond(), true_func(), false_func())
#if_stsatement 只会根据条件来执行其中一个 if_function会执行所有的function

def cond():
    "*** YOUR CODE HERE ***"
    return False
def true_func():
    "*** YOUR CODE HERE ***"
    print(47)
def false_func():
    "*** YOUR CODE HERE ***"
    print(42)

def hailstone(x):
    count = 0
    x = int(x)
    print(x)
    while x != 1:
        if x%2 == 0:
            x = x/2
            print(int(x))
            count += 1
        else:
            x = x*3 + 1
            print(int(x))
            count += 1
    return count+1

