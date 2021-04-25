#EXCERCISE 1
str = 'Print only the words that start with s in this sentence'
str_list=str.split()
for word in str_list:
    if word[0]=='s':
        print(word)

#EXCERCISE 2
#Use range() to print all the even numbers from 0 to 10.
for num in range(0,10):
    if num%2==0:
        print(num)

#EXCERCISE 3
#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
mylist=[number for number in range(1,50) if number%3==0]
print(mylist)

#EXCERCISE 4
#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
st_list=st.split()
for element in st_list:
    if len(element)%2==0:
        print(element)

#EXCERCISE 5
'''Write a program that prints the integers from 1 to 100.
But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".'''

for num in range(1,101):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%5==0:
        print("Buzz")
    elif num%3==0:
        print("Fizz")
    else:
        print(num)

#EXCERCISE 6
#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
st_list=st.split()
print([letter[0] for letter in st_list])


#EXCERCISE 7
def myfunc(txt):
    for char in txt:
        if txt.index(char)%2==0:
            txt.upper(char)
        else:
            txt.lower(char)
    print(txt)
myfunc("vanitha")
#EXCERCISE 2
#EXCERCISE 2

name="Sivakumar"
print(name[-1::-1])
print(name[-1::-1])

