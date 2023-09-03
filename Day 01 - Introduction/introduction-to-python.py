# Exercise: Level 1
# 1. Check the python version you are using

# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
a,b = 3,4 #defining the operands

print("The addition of operands is: ", a+b)    # addition(+)
print("The subtraction of operands is: ", a-b)    # subtraction(-)
print("The multiplication of operands is: ", a*b)    # multiplication(*)
print("The modulus of operands is: ", a%b)    # modulus(%)
print("The division of operands is: ", a/b)    # division(/)
print("The exponent of operand 1 to operand 2 is: ", a**b)    # exponential(**)
print("The floor division of operands is: ", a//b)    # floor division operator(//)

# 3. Write strings on the python interactive shell. The strings are the following:

print("My name is Shrey")    # Your name
print("My family name is Kshatriya")    # Your family name
print("My country is United States of America")    # Your country
print("I am enjoying 30 days of Python")    # I am enjoying 30 days of python

# 4. Check the data types of the following data:

print("This data type is: ", type(10))    # 10
print("This data type is: ", type(9.8))    # 9.8
print("This data type is: ", type(3.14))    # 3.14
print("This data type is: ", type(4 - 4j))    # 4 - 4j
print("This data type is: ", type(['Shrey', 'Python', 'United States of America']))    # ['Shrey', 'Python', 'United States of America']
print("This data type is: ", type("Shrey"))    # Your name
print("This data type is: ", type("Kshatriya"))    # Your family name
print("This data type is: ", type("United States of America"))    # Your country

# Exercise: Level 2
# 1. Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

# Exercise: Level 3
# 1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

print("Example for integer data type is 10. Type: ", type(10))
print("Example for float data type is 1.1. Type: ", type(1.1))
print("Example for complex data type is 3 + 2j. Type: ", type(3 + 2j))
print("Example for string data type is Hello World. Type: ", type("Hellow World"))
print("Example for boolean data type is True or False. Type: ", type(True))
print("Example for list data type is [1,2,3,4,apples]. Type: ", type([1,2,3,4,'apples']))
print("Example for tuple data type is (1,2,3,4). Type: ", type((1,2,3,4)))
print('''Example for set data type is {12,3,5,6 }. Type: ''', type({12,3,5,6}))
print("Example for dictionary data type is {'fruits' : ['apple', 'banana'], 'name' : 'Shrey' }. Type: ", type( {'fruits' : ['apple', 'banana'], 'name' : 'Shrey'}))

# 2. Find an Euclidian distance between (2, 3) and (10, 8)

x1,y1 = 2,3
x2,y2 = 10,8

e_dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

print("The euclidian distance between (2,3) and (10,8) is: ", e_dist)