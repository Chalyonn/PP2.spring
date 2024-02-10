"""
№1
A recipe you are reading states how many grams you need for the ingredient. 
Unfortunately, your store only sells items in ounces. 
Create a function to convert grams to ounces. ounces = 28.3495231 * grams
"""
grams=float(input())
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
result=grams_to_ounces(grams)
print(result)

"""
№2
Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature.
The following formula is used for the conversion: C = (5 / 9) * (F - 32)
"""

F=float(input())
def fah_to_C(F):
    C = (5 / 9) * (F - 32)
    return C
result = fah_to_C(F)
print(result)

"""
№3
Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
"""

def solve(numheads, numlegs):
    rabbit=(numlegs-2*numheads)/2
    chicken=numheads-rabbit
    print("rabbit: ", int(rabbit), " chicken: ", int(chicken))
a=int(input())
b=int(input())
solve(a,b)

"""
№4
You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of numbers as an agrument 
and returns only prime numbers from the list.
"""
import math
def filter_prime(lst):
    primes = []
    for x in lst:
        if x < 2:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return primes

n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

print(filter_prime(numbers))

"""
№5
Write a function that accepts string from user and print all permutations of that string.
"""

def permutation(word):
    if len(word) == 1:
        return [word]
    
    perms = permutation(word[1:])
    char = word[0]
    res = []

    for per in perms:
        for i in range(len(per)+1):
            res.append(per[:i] + char + per[i:])
    
    return res

wrd = input()
print(permutation(wrd))

"""
#6
Write a function that accepts string from user, 
return a sentence with the words reversed. We are ready -> ready are We
"""

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

sentence = input()
print(reverse_sentence(sentence))

"""
#7
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    pass

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""

def three_33(arr):
    count = 0
    for i in range(len(arr)-1):
        if(arr[i] == arr[i+1] == 3):
            count+=1
        if count >= 1:
            return True
    return False

n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

print(three_33(numbers))

"""
#8
Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
"""

def spy_game(arr):
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] == 0 and arr[i+2] == 7:
            return True
        else:
            continue
    return False


n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

print(spy_game(numbers))

"""
#9
Write a function that computes the volume of a sphere given its radius.
"""

import math
def volume(R):
    print((4*math.pi*(R**3))/3)

radius = int(input())
volume(radius)

"""
#10
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Note: don't use collection set.
"""

def unique_elems(arr):
    list = []
    for i in arr:
        if i not in list:
            list.append(i)
    return list

n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

print(unique_elems(numbers))

"""
#11
Write a Python function that checks whether a word or phrase is palindrome or not. 
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
"""
def check(a):
    for i in range(len(a)//2):
        if a[i]!=a[-i-1]:
            return False
    return True

r = input()
print(check(r))

"""
#12
Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:

****
*********
*******
"""

def his(arr):
    for i in range(len(arr)):
        print(arr[i]*'*')
    
his(list(map(int, input().split())))

"""
#13
Write a program able to play the "Guess the number" - game, 
where the number to be guessed is randomly chosen between 1 and 20. 
This is how it should work when run in a terminal:
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""
import random
def guess():
    x = input("Hello! What is your name?")
    num = random.randint(1,20)
    print(f"Well, {x}, I am thinking of a number between 1 and 20.")
    i = 0
    while True:
        i+=1
        print("Take a guess.")
        popitka = int(input())
        if popitka == num:
            print(f"Good job, {x}! You guessed my number in {i} guesses!")
            break
        elif(popitka > num):
            print("Your guess is too big")
            continue
        elif(popitka < num):
            print("Your guess is too low")
            continue
        
guess()

"""
#14
Create a python file and import some of the functions from the above 13 tasks and try to use them.
"""

def spy_game(arr):
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] == 0 and arr[i+2] == 7:
            return True
        else:
            continue
    return False

n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

print(spy_game(numbers))

def solve(numheads, numlegs):
    rabbits = (numlegs - 2*numheads)/2
    chicken = numheads - rabbits
    print(int(rabbits), int(chicken))

inp = input()
x, y = map(int, inp.split())
solve(x, y)