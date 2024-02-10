#example_1

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#example_2

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#example_3

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#example_4

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#example_5

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#example_6

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#example_7

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#example_8

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)