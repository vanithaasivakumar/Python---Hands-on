#EXCERCISE 1
#Alternate case
def myfunc1(txt):
    newstr=''
    i=0
    while i<len(txt):
        if i%2==0:
            newstr+=txt[i].upper()
        else:
            newstr+=txt[i].lower()
        i+=1
    print(newstr)
myfunc1("vanithaabamdnsvv")

#EXCERCISE 2
#Write a function takes a two-word string and returns True if both words begin with same letter
def myfunc2(txt):
    newtxt=txt.lower().split()
    if newtxt[0][0]==newtxt[1][0]:
        print(True)
    else:
        print(False)
myfunc2('Levelheaded Llama')
myfunc2('Crazy Kangaroo')


#EXCERCISE 3
#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or
# if one of the integers is 20. If not, return False
def myfunc3(a,b):
    if a+b==20 or a==20 or b==20:
        print(True)
    else:
        print(False)
myfunc3(1,2)
myfunc3(10,10)
myfunc3(1,20)

#EXCERCISE 4
#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def myfunc4(name):
    '''newname=''
    i=0
    while i<len(name):
        if i==0 or i==3:
            newname+=name[i].upper()
        else:
            newname+=name[i]
        i=i+1
    print(newname)'''
    print(name[:3].capitalize()+name[3:].capitalize())
myfunc4('macdonald')

#EXCERCISE 5
#Given a sentence, return a sentence with the words reversed
def myfunc5(txt):
    newtxt=txt.split()[::-1]
    print(' '.join(newtxt))
myfunc5('i am ready')

#EXCERCISE 6
#Given an integer n, return True if n is within 10 of either 100 or 200
def myfunc6(n):
    '''
    if n in range(90,111) or n in range(190,211):
        print(True)
    else:
        print(False) '''
    if abs(100-n)<=10 or abs(200-n)<=10:
        print(True)
myfunc6(101)
myfunc6(195)
myfunc6(80)
myfunc6(250)

#EXCERCISE 7
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def myfunc7(numbers):
    index3=numbers.index(3)
    if numbers[index3+1]==3:
        print(True)
    else:
        print(False)
myfunc7([1, 3, 3])
myfunc7([1, 3, 1, 3])
myfunc7([3, 1, 3])

#EXCERCISE 8
def myfunc8(txt):
    newtxt=''
    for char in txt:
        newtxt+=char*3
    print(newtxt)
myfunc8('hello')

#EXCERCISE 9
#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def myfunc9(a,b,c):
    total=a+b+c
    if total<=21:
        print(total)
    elif a==11 or b==11 or c==11:
        if total-10<=21:
            print(total-10)
        else:
            print("BUST")
    else:
        print("BUST")
myfunc9(5,6,7)
myfunc9(9,9,9)
myfunc9(9,9,11)

#EXCERCISE 10
#SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9
#(every 6 will be followed by at least one 9).
# Return 0 for no numbers
def myfunc10(numbers):
    sum=0
    i=0
    while i<len(numbers):
        if numbers[i]==6 and 9 in numbers[i:]:
            i=numbers.index(9)+1
        else:
            sum+=numbers[i]
            i=i+1
    print(sum)

myfunc10([1, 3, 5])
myfunc10([4, 5, 6, 7, 8, 9])
myfunc10([2, 1, 6, 9, 9])

''' Awesome job.'''
#EXCERCISE 11
#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order¶
def myfunc11(numbers):
    '''
    i=0
    no_of_zeros=0
    if 7 in numbers:
        for i in range(0,numbers.index(7)):
            if numbers[i]==0:
               no_of_zeros+=1
    else:
        print(False)
    if no_of_zeros==2:
        print(True)
    else:
        print(False)
    '''
    code=[0,0,7,'x']
    for num in numbers:
        if num==code[0]:
            code.pop(0)
    if len(code)==1:
        print(True)
    else:
        print(False)

myfunc11([1,2,4,0,0,7,5])
myfunc11([1,0,2,4,0,5,7])
myfunc11([1,7,2,0,4,5,0])

#EXCERCISE 12
#COUNT PRIMES: Write a function that returns the number of prime numbers
# that exist up to and including a given number¶
'''def myfunc12(input):
    count=0
    while
        for div in range(2,10):
            if num%div==0:
                continue
            else
    if count'''

#EXCERCISE 13
#The volume of a sphere
def myfunc13(radius):
    print(4/3*22/7*radius*radius*radius)

myfunc13(2)

#EXCERCISE 14
#Write a function that checks whether a number is in a given range (inclusive of high and low)
def myfunc14(num,l_range,h_range):
    if num in range(l_range,h_range+1):
        print("{} is in the range between {} and {}".format(num,l_range,h_range))
    else:
        print("{} is not in the range between {} and {}".format(num,l_range,h_range))

myfunc14(5,3,6)
myfunc14(5,3,5)
myfunc14(2,2,3)


#EXCERCISE 15
#Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def myfunc15(txt):
    lo_num=0
    up_num=0
    for char in txt:
        if char.isupper()==True:
            up_num+=1
        elif char.islower()==True:
            lo_num+=1
        else:
            pass
    print("No. of Upper case characters : {}".format(up_num))
    print("No. of Lower case characters : {}".format(lo_num))

myfunc15('Hello Mr. Rogers, how are you this fine Tuesday?')

#EXCERCISE 16
#Python function that takes a list and returns a new list with unique elements of the first list
def myfunc16(numbers):
    print(set(numbers))

myfunc16([1,1,1,1,2,2,3,3,3,3,4,5])

#EXCERCISE 17
#Write a Python function to multiply all the numbers in a list.
def myfunc17(numbers):
    result=1
    if 0 in numbers:
        print(0)
    else:
        for num in numbers:
            result=result*num
        print(result)

myfunc17([1, 2, 3, -4])

#EXCERCISE 18
#Python function that checks whether a word or phrase is palindrome or not
def myfunc18(txt):
    newtxt=txt.replace(' ','')
    if newtxt==newtxt[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")
myfunc18('helleh')
myfunc18('nurses run')

#EXCERCISE 19
#Python function to check whether a string is pangram or not.
#(Assume the string passed in does not have any punctuation)
def myfunc19(txt):
    alphabet_set=set(list('abcdefghijklmnopqrstuvwxyz'))
    txt_set=set(txt.lower().replace(' ',''))
   # new_set=alphabet_set.difference(txt_set)
   # if len(new_set)==0:
    if alphabet_set==txt_set:
        print('Pangram')
    else:
        print('Not a Pangram')

myfunc19("The quick brown fox jumps over the lazy dog")
myfunc19("Hello World")

