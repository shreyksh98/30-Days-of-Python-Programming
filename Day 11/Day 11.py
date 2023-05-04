# Day 11 of 30 days of Python Programming

# Day 11 Functions

# Exercise 1

# 1.1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(x,y):
    return x+y
print(add_two_numbers(3,5))

# 1.2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def aoc(rad, pi = 3.14):
    return (pi*(rad**2))
print(aoc(10))

# 1.3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    total = 0
    for i in nums:
        if type(i) != int:
            return("{} is not an integer".format(i))
        else:
            total+=i
    return total

print(add_all_nums(1,2,4,5,3,10))

# 1.4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def celc_to_farh(celc):
    f = (celc*3.5)+32
    return f
print(celc_to_farh(10))

# 1.5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if month == 'September' or month == 'October' or month == 'November':
        return('Autumn')
    elif month == 'December' or month == 'January' or month == 'February':
        return('Winter')
    elif month == 'March' or month == 'April' or month == 'May':
        return('Spring')
    elif month == 'June' or month == 'July' or month == 'August':
        return('Summer')
    else:
        return('That is not a valid month')
print(check_season('April'))

# 1.6 Write a function called calculate_slope which return the slope of a linear equation y=mx+b

def slope(x1,y1,x2,y2):
    m = (y2-y1)/(x2-x1)
    return m
print(slope(1,2,3,4))

# 1.7 Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

import math
def solve_quadratic_eqn(a,b,c):
    #first we solve for the discriminant
    d = math.sqrt((b**2) - (4 * a * c))
    # then we solve for both positive and negative values of the set
    s1 = (-b + d)/(2*a)
    s2 = (-b - d)/(2*a)
    return {s1,s2}

print(solve_quadratic_eqn(1,5,3))

# 1.8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(list_val):
    for x in list_val:
        print(x)
print_list([1,2,3,4,5,5,6])

# 1.9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(reverse_lst):
    new_list = []
    for x in range(1,len(reverse_lst)+1):
        y = reverse_lst[-x]
        new_list.append(y)
    return new_list
print(reverse_list([1,2,3,4,5,6]))

# 1.10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_item(lst):
    new_lst = []
    for i in lst:
        i = i.capitalize()
        new_lst.append(i)
    return new_lst
print(capitalize_list_item(["hello",'my','name','is','shrey']))

# 1.11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

nums = [1,2,3,4,5,6]
def add_item(lst, *new_item):
    for i in new_item:
        lst.append(i)
    return lst
print(add_item(nums,1,2,3,4))

# 1.12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(lst, *rem_item):
    for i in rem_item:
        if i not in lst:
            return("This number does not exist, hence cannot be removed")
        else:
            for y in lst:
                if y == i:
                    lst.remove(i)
    return lst
print(remove_item(nums, 2,4))

# 1.13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(args):
    total = 0
    for i in range(args+1):
        total+=i
    return total
print(sum_of_numbers(5))

# 1.14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(args):
    sum = 0
    for i in range(args+1):
        if i %2 != 0:
            sum+=i
        else:
            continue
    return sum
print(sum_of_odds(10))

# 1.15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(args):
    sum = 0
    for i in range(args+1):
        if i %2 == 0:
            sum+=i
        else:
            continue
    return sum
print(sum_of_even(10))

# Exercise 2

# 2.1 Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(args):
    even_count = 0
    odd_count = 0
    if args>0:
        for i in range(args+1):
            if i%2 == 0:
                even_count+=1
            else:
                odd_count+=1
        return(even_count, odd_count)
    else:
        return("The number is not positive")
print(evens_and_odds(10))

# 2.2 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(args):
    fact = 1
    for i in range(1, args+1):
        fact*=i
    return fact
print(factorial(10))

# 2.3 Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(args):
    if len(args)==0:
        return ('Empty')
    else:
        return('Not Empty')
print(is_empty([]))

# 2.4 Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

