"""
#1 
Define a class which has at least two methods: 
getString: to get a string from console input printString: to print the string in upper case.
"""

class MyClass:   
    def getString(self):
        self.a=str(input())
    
    def printString(self):
        print(self.a.upper())

p1=MyClass()
p1.getString()
p1.printString()

"""
#2
Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape
where Shape's area is 0 by default.
"""

class Shape:
    def area(self):
        print(0)
class Square(Shape):
        def __init__(self, length):
            self.length=length
        
        def area(self):
            print(self.length*self.length) 

x=Square(int(input()))
y=Shape()
x.area()
y.area()

"""
#3
Define a class named Rectangle which inherits from Shape class from task 2. 
Class instance can be constructed by a length and width. 
The Rectangle class has a method which can compute the area
"""

class Shape:
    def area(self):
        print(0)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        print(self.length*self.width)

x=Rectangle(int(input()), int(input()))
y=Shape()
x.area()
y.area()

"""
#4
Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points
"""

import math
class Point:
    def __init__(self, x1, y1):
        self.x1=x1
        self.y1=y1
    def show(self):
        print("Coordinates: ", self.x1, self.y1) 
    def move(self, x2, y2):
        self.x2=x2
        self.y2=y2
        print("Next coordinates:",self.x2, self.y2)
    def dist(self):
        print("Distance between two points:",math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2))

x=Point(int(input()), int(input()))
x.show()
x.move(int(input()), int(input()))
x.dist()

"""
#5
Create a bank account class that has attributes owner, 
balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    pass
"""

class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, months, percent):
        for i in range(months):
            self.balance+=self.balance*(percent/100)
        print("Your current balance is equal to", self.balance)
    def withdraw(self, wtdr):
        if wtdr<0:
            print("You haven't withdrawn the money")
        elif wtdr>self.balance:
            print("Your balance does not have such a withdraw")
        else:
            print("You took it off", wtdr, " and your current balance is exactly ", self.balance-wtdr)
            self.balance=self.balance-wtdr
x=Account("Alina", 50000)
x.deposit(24, 15)
x.withdraw(25000)

"""
#6
Write a program which can filter prime numbers in a list by using filter function.
Note: Use lambda to define anonymous functions.
"""

lst = list(map(int, input().split()))
primes = filter(lambda x: all(x%i != 0 for i in range(2, x)), lst)
result = list(primes)
if 1 in result:
    result.remove(1)
print(result)