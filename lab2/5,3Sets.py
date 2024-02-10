#example_1

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#example_2

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#example_3

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#example_4

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#example_5

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)