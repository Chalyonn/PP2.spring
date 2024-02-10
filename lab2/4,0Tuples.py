#example_1

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#example_2

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#example_3

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#example_4

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#example_5

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#example_6

tuple1 = ("abc", 34, True, 40, "male")

#example_7

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#example_8

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)