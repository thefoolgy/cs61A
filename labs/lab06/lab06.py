from lzma import FILTER_LZMA2


this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    c = 0
    def g(b):
        nonlocal c
        sum = a + b + c
        c = c + 1
        return sum
    return g

#pku solution    
#    def adder(a):
#        nonlocal a
#        a = a + 1
#        return a + b - 1
#    return adder

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    n = -1
    f0,f1 = 0,1
    def g():
        nonlocal n
        n += 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            nonlocal f0,f1
            f = f0 + f1
            f0 = f1
            f1 = f
            return f
    return g
#pku solution
#   f1,f2 = 1,0
#   def fib():
#       nonlocal f1,f2
#       f1,f2 = f2,f1+f2 
#       return f1
#   return fib


def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    j = 1
    lst1 = lst[:]
    for i in range(len(lst1)):
        if lst1[i] == entry:
            lst.insert(i+j,elem)
            j += 1
    return lst




