#example_1

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#example_2

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#example_3

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#example_4

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#example_5

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#example_6

thislist = ["apple", "banana", "cherry"]
del thislist

#example_7

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)