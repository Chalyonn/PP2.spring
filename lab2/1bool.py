#EXERCISE_1

print(10 > 9)

True

#EXERCISE_2

print(10 == 9)

False

#EXERCISE_3

print(10 < 9)

False

#EXERCISE_4

print(bool("abc"))

True

#EXERCISE_5

print(bool(0))

False

#example_1

print(10 > 9)
print(10 == 9)
print(10 < 9)

#example_2

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#example_3
  
print(bool("Hello"))
print(bool(15))

#example_4

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#example_5

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#example_6

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#example_7

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#example_8

def myFunction() :
  return True

print(myFunction())

#example_9

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#example_10
  
x = 200
print(isinstance(x, int)) #isinstance() to determine if an object is of a certain data type