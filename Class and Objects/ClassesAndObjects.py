#EXCERCISE 1

class Cylinder:
    pi=3.14
    def __init__(self, height=1, radius=1):
        self.height=height
        self.radius=radius

    def volume(self):
        print(Cylinder.pi*self.radius**2*self.height)

    def surface_area(self):
        print((2*Cylinder.pi*self.radius*self.height)+(2*Cylinder.pi*self.radius**2))

c = Cylinder(2,3)
c.volume()
c.surface_area()

#EXCERCISE 2
import math
class Line:
    def __init__(self,c1,c2):
        self.x1,self.y1=c1
        self.x2,self.y2=c2

    def distance(self):
        print(((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5)

    def slope(self):
        print((self.y2-self.y1)/(self.x2-self.x1))

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()
li.slope()

#EXCERCISE 3
class Account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance =balance

    def __str__(self):
        return f'Account Name: {self.owner} \nAccount Balance: {self.balance}'

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Account: {}\n New Balance is {}".format(self.owner,self.balance))

    def withdraw(self,amount):
        if self.balance-amount<0:
            print("Sorry! The amount exceeds your account balance")
        else:
            self.balance=self.balance-amount
            print("Account: {} \n New Balance is {}".format(self.owner, self.balance))

acct1 = Account('Mia',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)