def odd_even_number():
    num = int(input("Enter the Number: "))
    if num%2==0:
        print(num,"Even Number")
    else:
        print(num,"Odd Number")

def prime_number():
    count=0
    num=int(input("Enter the Number: "))
    for i in range(2,10):
            if num%i==0:
                count+=1
    if count>2:
                print("The given number is not a prime number")
    else:
        print("Prime Number")

def fibonocci_series():
    var1=0
    var2=1
    num2=int(input("Enter the Number: "))
    print(var1)
    print(var2)
    temp = 0;
    while True:
        temp = var1 + var2
        var1 = var2
        var2 = temp
        if var2 >= num2:
            break
        print(temp, end=" ")
def max_of_3_nos():
    num1=int(input("Enter number 1: "))
    num2 =int(input("Enter number 2: "))
    num3 =int(input("Enter number 3: "))
    if num1>=num2 and num1>=num3:
        print(num1,"is the biggest number")
    elif num2>=num1 and num2>=num3:
        print(num2,"is the biggest number")
    else:
        print(num3,"is the biggest number")

while True:
    print("\n--------------------------")
    print("1.Find Odd/Even Number")
    print("2.Find Prime Number")
    print("3.Fibonocci Series")
    print("4.Max of 3 numbers")
    print("5.Exit")
    user_input = input("Enter your choice: ")
    print("--------------------------")
    if user_input=="1":
        odd_even_number()
    elif user_input=="2":
        prime_number()
    elif user_input=="3":
        fibonocci_series()
    elif user_input == "4":
        max_of_3_nos()
    elif user_input=="5":
        break
    else:
        print("Can you enter the correct choice(1-4)?")








