#example_1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#example_2

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#example_3

newlist = [x for x in fruits if x != "apple"]

#example_4

newlist = [x for x in fruits]

#example_5

newlist = [x for x in range(10)]

#example_6

newlist = [x for x in range(10) if x < 5]

#example_7

newlist = [x.upper() for x in fruits]

#example_8

newlist = ['hello' for x in fruits]

#example_9

newlist = [x if x != "banana" else "orange" for x in fruits]