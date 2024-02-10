#EXERCISE_1

from calendar import c
import dataclasses
import datetime


a = 50
b = 10
if a>b :
    print("Hello World")

#EXERCISE_2
    
a = 50
b = 10
if a!=b:
    print("Hello World")

#EXERCISE_3

a = 50
b = 10
if a==b:
    print("Yes")
else:
    print("No")

#EXERCISE_4

a = 50
b = 10
if a==b:
    print("1")
elif a>b:
    print("2")
else:
    print("3")

#EXERCISE_5
a=10 
b=10
c=10
d=10
if a == b and c == d:
  print("Hello")

#EXERCISE_6
  
a,b,c,d=10,10,20,20
if a == b or c == d:
  print("Hello")

#EXERCISE_7
  
if 5 > 2:
    print("YES")

#EXERCISE_8
    
a = 2
b = 5
print("YES") if a == b else print("NO")

#EXERCISE_9

a = 2
b = 50
c = 2
if a == c or b == c:

  print("YES")

#example_1

a = 33
b = 200
if b > a:
  print("b is greater than a")

#example_2
  
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#example_3
  
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#example_4
  
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#example_5
  
if a > b: print("a is greater than b")

#example_6

a = 2
b = 330
print("A") if a > b else print("B")

#example_7

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#example_8

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#example_9
  
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#example_10
  
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#example_11
  
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#example_12

a = 33
b = 200

if b > a:
  pass