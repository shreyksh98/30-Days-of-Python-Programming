# Day 9 of 30 days of Python

# Day 9 Conditionals

# Exercise Level 1

# 1.1 Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years

age = int(input("Enter your age: "))
print("You are old enough to drive" if age >= 18 else ("You need to wait {0:.2f} years".format(18-age)))

# 1.2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 

your_age = int(input("Enter your age: "))
my_age = 25

if your_age > my_age:
    if your_age - my_age == 1:
        print("You are 1 year older")
    else:
        print("You are {} years older".format(your_age-my_age))
elif my_age > your_age:
    if my_age - your_age == 1:
        print("I am 1 year older than you")
    else:
        print("I am {} years older".format(my_age-your_age))
else:
    print("We are same years old")

# 1.3 Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# print(("A is greater than B") if a>b ("A is smaller than B") elif a<b else ("A and B are equal"))

if a>b:
    print("A is greater than B")
elif a<b:
    print("A is smaller than B")
else:
    print("A and B are equal")

# Exercise Level 2

# 2.1 Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-79, B
# 60-69, C
# 50-59, D
# 0-49, F

score = int(input("Enter your grade: "))

if score >= 80 and score <101:
    print("Your grade is A")
elif score >= 70 and score < 80:
    print("Your grade is B")
elif score >= 60 and score < 70:
    print("Your grade is C")
elif score >= 50 and score < 60:
    print("Your grade is D")
else:
    print("PLEASE TRY AGAIN YOU HAVE FAILED!!!")

# 2.2 Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer

month = input("What month is it? ")

if month == "September" or month == "October" or month == "November":
    print("The season is Autumn")
elif month == "December" or month == "January" or month =="February":
    print("The season in Winter")
elif month == "April" or month == "March" or month == "May":
    print("The season is Spring")
else:
    print("The season is Summer")

# 2.3 The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter the name of a fruit: ")

if new_fruit not in fruits:
    fruits = fruits.append(new_fruit)
    print(fruits)
else:
    print("The fruit already exist in the list")

# Exercise 3

# Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Shrey',
    'last_name': 'Kshatriya',
    'age': 25,
    'country': 'United States of America',
    'is_marred': False,
    'skills': ['Tableau', 'SQL', 'PowerBI', 'Excel', 'Python'],
    'address': {
        'street': 'Top of Empire State',
        'zipcode': '10001'
    }
    }

# 3.1  Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if "skills" in person.keys():
    vals = list(person.get("skills"))
    if len(vals)%2 != 0:
        ind = int(len(vals)/2 - 0.5)
        print(vals[ind])
    else:
        ind_1 = int(len(vals)/2)
        ind_2 = int(len(vals)/2 - 1)
        print(vals[ind_1]+","+vals[ind_2])

else:
    print("The key skills does not exist")

# 3.2 Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if 'skills' in person.keys() and 'Python' in (list(person.get("skills"))):
    print("{} is skilled in Python".format(person.get('first_name')))
else:
    print("{} is not skilled in Python".format(person.get('first_name')))

# 3.3 If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!

if 'Javascript' in (list(person.get("skills"))) and 'React' in (list(person.get("skills"))):
    print("{} is a front end developer".format(person.get('first_name')))
elif 'Node' in (list(person.get("skills"))) and 'Python' in (list(person.get("skills"))) and 'MongoDB' in (list(person.get("skills"))):
    print("{} is a backend developer".format(person.get('first_name')))
elif 'React' in (list(person.get("skills"))) and 'Node' in (list(person.get("skills"))) and 'MongoDB' in (list(person.get("skills"))):
    print("{} is a fullstack developer".format(person.get('first_name')))
else:
    print("{} is a not full stack, front end or a backend developer".format(person.get('first_name')))

# 3.4 If the person is married and if he lives in Finland, print the information in the following format:
#  Asabeneh Yetayeh lives in Finland. He is married.

if (person.get("is_married")) is True and (person.get("country")) == 'Finland':
    print("{} live in Finlad. He is married".format(person.get("first_name")))



          









