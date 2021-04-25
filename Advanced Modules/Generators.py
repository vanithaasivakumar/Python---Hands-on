'''Explain a use case for a generator using a yield statement
where you would not want to use a normal function with a return statement.

If the output has the potential of taking up a large amount of memory
and you only intend to iterate through it, you would want to use a generator.'''


#Create a generator that generates the squares of numbers up to some number N.
def mygen1(n):
    for num in range(1,n):
        yield num*num

for x in mygen1(10):
    print(x)

val=mygen1(2)


#Create a generator that yields "n" random numbers between a low and high number (that are inputs).
from random import randint
def mygen2(low,high,n):
    for i in  range(0,n):
        yield randint(low,high)

for x in mygen2(1,10,12):
    print(x)

gen=mygen2(1,10,12)
print(next(gen))

#Use the iter() function to convert the string below into an iterator:
s = 'hello'
s = iter(s)

print(next(s))


#generator comprehensions
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
