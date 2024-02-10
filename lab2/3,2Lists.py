#example_1

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#example_2

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#example_3

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#example_4

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#example_5

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)