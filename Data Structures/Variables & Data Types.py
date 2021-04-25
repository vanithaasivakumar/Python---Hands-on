
#STRING

print("Python" + "Programming")
value="2"
print("My value is "+ value)
my_string="montreal"
print(len(my_string))
upper_string=my_string.upper()
print(upper_string)
print(upper_string.isupper())

word = "Hello World"

print(word[0]) #get one char of the word
print(word[0:1]) #get one char of the word (same as above)
print(word[0:3]) #get the first three char
print(word[:3]) #get the first three char
print(word[-3:]) #get the last three char
print(word[3:]) #get all but the three first char
print(word[:-3]) #get all but the three last character

#NUMBERS
print(1+6)
value_1=1
print(value)
print("converting number to string "+str(value_1))
value_2=100
value_3=value_1+value_2 #Same for subtraction,division,multiplication
print(value_3)
value_4=value_3%5
print(value_4)

#GETTING INPUT FROM THE USER -- default datatype is String
myname=input("Enter your name: ")
print("Your Name is " +myname)
myage=input("Enter your age: ")
print("Your age is "+ myage)
newage=int(myage)+1
print(newage)






