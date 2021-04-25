#This file contains all the string methods
sample_str1="Hello World!"
sample_str2="python programming"
sample_str3="My name is Vanitha Alaguvel"
sample_str4="rain rain go away"

#Converts the first character to upper case
capitalized_string=sample_str2.capitalize()
print(sample_str2,"\nCapitalized String: ",capitalized_string)

#Converts string into lower case
casefolded_string=sample_str2.casefold()
print(sample_str2,"\nCasefolded String: ",casefolded_string)

#Returns a centered string spcified by the width and filler
centered_string=sample_str1.center(100,"*")
print(sample_str1,"\nCentered String: ", centered_string)

#Returns the number of times a specified value occurs in a string
count_words=sample_str4.count("rain")
print(sample_str4,"\nNo of rain count: ",count_words)

#Returns an encoded version of the string such as UTF-8,ASCII. default encoding is UTF_8
#Error values - backslashreplace,ignore,namereplace,strict,replace,xmlcharrefreplace
encoded_string=sample_str1.encode("ASCII",errors="ignore")
print(sample_str1,"\nASCII Encoded String: ",encoded_string)

#Check if the string ends with a particular char/string
is_ends_with=sample_str1.endswith("!")
print(sample_str1,"\nThe text ends with !", is_ends_with)

#Returns string with specified tab space
str_head="col1\tcol2\tcol3\tcol4"
print("Original String: ",str_head)
tab_space1=str_head.expandtabs(1)
print("Tab space 1: ",tab_space1)
tab_space15=str_head.expandtabs(15)
print("Tab space 15: ",tab_space15)

#Searches the string for a specified value and returns the position of where it was found
name_position=sample_str3.find("Vanitha")
print("The position of my name is",name_position)

#FORMATTING STRINGS
#formats specified value and insert them into the placeholders{}
str1="The product name is {pname} and the price is {price}"
out1=str1.format(pname="Macbook Pro",price=1500)
str2="The product name is {} and the price is {}"
out2=str2.format("Macbook Pro",1500)
str3="The product name is {0} and the price is {1}"
out3=str3.format("Macbook Pro",1500)
print(out1)
print(out2)
print(out3)

str4="The sample alignment text {:<25}{:>25}{:^50}"
out4=str4.format("Left","Right","Center")
print(out4)

str5="Specifies 10 spaces between the sign and number:{:=10}"
out5=str5.format(-25)
print(out5)
str6="To specify space before positive and negative numbers {: }{: }"
out6=str6.format(-10,15)
print(out6)

str7="Comma as a thousand separator in number {:,}"
print(str7.format(1755645345))
str8="Underscore as a thousand separator in number {:_}"

print(str8.format(1755645345))
str9="Binary format of 10 is {:b}"
print(str9.format(10))
str10="Unicode Character of 67 is {:c}"
print(str10.format(67))
str11="Decimal format of binary 1011 is {:d}"
print(str11.format(0b1011))
str12="Scientific format of 123456789 with lower case e is {:e}"
print(str12.format(123456789))
str13="Scientific format of 123456789 with lower case e is {:E}"
print(str13.format(123456789))
str14="default decimal place in number {:f} and 2 decimal places {:.2f}"
print(str14.format(45,45))

str15="Specify INF (Infinity) and NAN (Not a Number) in upper case {:F} {:F}"
x=float("inf")
print(x)
y=float("inf")-float("inf")
print(y)
print(str15.format(x,y))

str16="Specifies general format for number in lowercase {:g} and upper case {:G}"
print(str16.format(123456789,123456789))
str17="Octal format of 9 is {:o}"
print(str17.format(9))
str18="Hexadecimal format of 20 in Uppercase {:X} and lowercase {:x}"
print(str18.format(209878,209878))
str19="The number format of 1213 is {:n}"
print(str19.format(1.23457e+08))

print("To specify number using number format {:n}".format(1000000))
import locale
locale.setlocale(locale.LC_ALL, '')
print("After importing locale {:n}".format(1000000))

print("The percentage of .37 is {:.2%}".format(.37))

