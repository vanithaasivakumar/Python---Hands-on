#REDUCE
'''reduce(function, sequence[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.'''
from functools import reduce #Built-in func Python 2
def funcsquare(a,b):
    return a+b
list1=[1,2,3]
result=reduce(funcsquare,list1)
print(result)

#ACCUMULATE
'''apply a particular function passed in its argument to all of the list elements 
returns a list containing the intermediate results'''
import itertools



#SUM
print(sum(list1))
