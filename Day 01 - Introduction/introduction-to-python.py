## Welcome to the Asabeneh's 30 days of python

## Introduction
## Day 1 - Basic Python

print(2+3) ##addition
print(3-1) ## subtraction
print(2*3) ##multiplication
print(3/2) ##division
print(3 ** 2) ##exponents
print(19%4) ##modulus or remainder
print(19//4) ##floor division or quotient

## checking data types using type()

a = 'This is the start of 30 days of Python'
b = 1.00
c = 100

print(type(a),type(b),type(c)) ## gives the output of string, float, int

dict = {1:'one', 2: 'two', 3: 'three'}
list = [1,2,3]
tuple = (1,2,3)
set = {1,2,3}

print(type(dict),type(list),type(tuple),type(set)) ## gives the output as dict, list,tuple, set


## EXERCISE

## Exercise Level 1 
    # 1. check the python version
    ## ans>> to check the python version, go to your command promt/anaconda command promt and type in python --version.
    ##       this will give you the current version of your python.

    # 2, 3 & 4 are done directly in the commant prompt

## Exercise Level 2
    # Done within the user directory

## Exercise Level 3
    ## 1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

print("EXERCISE 3.1 Answers")
print(type(1)) ## integer
print(type(10.00)) ##float
print(type(200 + 10j)) ##complex
print(type("This is a string")) ##string
print(type(True)) ##boolean
print(type([1,2,3])) ##list
print(type((1,2,3))) ##tuple
print(type({1,2,3})) ##set
print(type({1:'a', 2: 'b', 3 : 'c'})) ##dictonary

    ## 2. Find an Euclidian distance between (2, 3) and (10, 8)

## method 1 is to import math and use the sqrt function

print("EXERCISE 3.2 Answers")
import math

d1 = ((10-2)**2)
print(d1)
d2 = ((8-3)**2)
print(d2)
d3 = d1 + d2
print(d3)
d4 = math.sqrt(d3)

print(f"the distance between (2,3) & (10,8) is {round(d4,2)}")


## method 2 is to use string formatting directly with print function
print('The edist is {0:.2f} and this is method {1:d}'.format(((10-2)**2 + (8-3)**2)**0.5,2))

# method 3 is to use math.dist function directly which calculated the euclidian distance for you
p1 = 2
p2 = 3
q1 = 10
q2 = 8

print("the edist is {}".format(math.dist([p1,p2],[q1,q2])))