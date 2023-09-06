# Exercises: Level 1
# 1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py

# 2. Write a python comment saying 'Day 2: 30 Days of python programming'
    # Day 2: 30 days of python programming

# 3. Declare a first name variable and assign a value to it
first_name = 'Shrey'

# 4. Declare a last name variable and assign a value to it
last_name = 'Kshatriya'

# 5. Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name

# 6. Declare a country variable and assign a value to it
country = 'United States of America'

# 7. Declare a city variable and assign a value to it
city = 'Jersey City'

# 8. Declare an age variable and assign a value to it
age = 26

# 9. Declare a year variable and assign a value to it
year = 2023

# 10. Declare a variable is_married and assign a value to it
is_married = False

# 11. Declare a variable is_true and assign a value to it
is_true = True

# 12. Declare a variable is_light_on and assign a value to it
is_light_on = True

# 13. Declare multiple variable on one line
occupation, company_name, years_of_experience = 'Data Scientist', 'Intuit', 3

# Exercises: Level 2
# 1. Check the data type of all your variables using type() built-in function
print(f"The data type for {first_name} is: ",type(first_name))
print(f"The data type for {last_name} is: ", type(last_name))
print(f"The data type for {full_name} is: ", type(full_name))
print(f"The data type for {country} is: ", type(country))
print(f"The data type for {city} is: ", type(city))
print(f"The data type for {age} is: ", type(age))
print(f"The data type for {year} is: ", type(year))
print(f"The data type for {is_married} is: ", type(is_married))
print(f"The data type for {is_true} is: ", type(is_true))
print(f"The data type for {is_light_on} is: ", type(is_light_on))
print(f"The data type for {occupation} is: ", type(occupation))
print(f"The data type for {company_name} is: ", type(company_name))
print(f"The data type for {years_of_experience} is: ", type(years_of_experience))


# 2. Using the len() built-in function, find the length of your first name
print("The length of the variable first_name is: ", len(first_name))

# 3. Compare the length of your first name and your last name
print(f"The length of first name is {len(first_name)} and length of last name is {len(last_name)}.")

# 4. Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4
    # i. Add num_one and num_two and assign the value to a variable total
total = (num_one+num_two)
print("The addition of num one and num two is: ", total)

    # ii. Subtract num_two from num_one and assign the value to a variable diff
diff = (num_two - num_one)
print("The subtraction of num two from num one is: ", diff)

    # iii. Multiply num_two and num_one and assign the value to a variable product
product = (num_one*num_two)
print("The multiplication of num one and num two is: ", product)

    # iv. Divide num_one by num_two and assign the value to a variable division
division = (num_one/num_two)
print("The division of num one by num two is: ", division)

    # v. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = (num_two%num_one)
print("The modulus of num two divided by num one is: ", remainder)

    # vi. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = (num_one**num_two)
print("The value of num one to the power of num two is: ", exp)

    # vii. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = (num_one//num_two)
print("The floor division of num one by num two is: ", floor_division)

# 5. The radius of a circle is 30 meters.
radius = 30
    # i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14*(radius**2)
print("The area of the circle is: ", area_of_circle)

    # ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circumference_of_circle = 2*3.14*radius
print("The circumference of the circle is: ", circumference_of_circle)

    # iii. Take radius as user input and calculate the area.
user_input_radius = int(input("Enter the radius of the circle: "))
user_input_area = 3.14*(user_input_radius**2)
print("The radius of the circle with radius given by the user is: ", user_input_area)

# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
user_f_name, user_l_name, user_country, user_age = input("Enter your name: "), input("Enter your last name: "), input("Enter your country: "), input("Enter your age: ")

# 7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords