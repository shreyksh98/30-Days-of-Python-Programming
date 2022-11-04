## Exercise  - Day 2
## Exercise: Level 1
    ## 1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
        ## ans>> this is done already in the file directory
    
    ## 2. Write a python comment saying 'Day 2: 30 Days of python programming'
        ## ans>> This is a comment that says '30 Days of python programming'
    
    ## 3. Declare a first name variable and assign a value to it

## ans>>
first_name = "Shrey"

    ## 4. Declare a last name variable and assign a value to it

## ans>>
last_name = "Kshatriya"

    ## 5. Declare a full name variable and assign a value to it

##ans>>
full_name = "Shrey Kshatriya"

    ## 6. Declare a country variable and assign a value to it

##ans>>
country = "United States of America"

    ## 7. Declare a city variable and assign a value to it

##ans>>
city = "New York City"

    ## 8. Declare an age variable and assign a value to it

##ans>>
age = 100

    ## 9. Declare a year variable and assign a value to it

##ans>>
year = 2022

    ## 10. Declare a variable is_married and assign a value to it

##ans>>
is_married = False

    ## 11. Declare a variable is_true and assign a value to it

##ans>>
is_true = False

    ## 12. Declare a variable is_light_on and assign a value to it

##ans>>
is_light_on = "No"

    ## 13. Declare multiple variable on one line

##ans>>
dec_type, fav_anime, current_movie, fav_song, games_played = "Multiple Variables", "Jujutsu Kaisen", "Wolf of the wall street", "As it was", 20


##Exercise : Level 2

    ## 1. Check the data type of all your variables using type() built-in function

##ans>>
print("The data type for variable first name is: ",type(first_name))
print("The data type for variable last name is: ",type(last_name))
print("The data type for variable full name is: ",type(full_name))
print("The data type for variable country is: ",type(country))
print("The data type for variable city is: ",type(city))
print("The data type for variable age is: ",type(age))
print("The data type for variable year is: ",type(year))
print("The data type for variable is_married is: ",type(is_married))
print("The data type for variable is_true is: ",type(is_true))
print("The data type for variable is_light_on is: ",type(is_light_on))

    ## 2. Using the len() built-in function, find the length of your first name

##ans>>
print("Length of first name is: ", len(first_name))

    ## 3. Compare the length of your first name and your last name

print(f"Length of first name is {len(first_name)} and length of last name is {len(last_name)}")

    ## 4. Declare 5 as num_one and 4 as num_two
        ## i. Add num_one and num_two and assign the value to a variable total

num_one, num_two = 5,4
total = num_one + num_two
print("Total of both variable is: ", total)

        ## ii. Subtract num_two from num_one and assign the value to a variable diff
    
diff = num_two - num_one
print("Difference of both variables is: ", diff)

        ## iii. Multiply num_two and num_one and assign the value to a variable product

product = num_one * num_two
print("Product of both variables is: ", product)

        ## iv. Divide num_one by num_two and assign the value to a variable division

division = num_one/num_two
print("Division of both variables is: ", division)

        ## v. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder

remainder = num_two % num_one
print("Remainder of both variables is: ", remainder)

        ## vi. Calculate num_one to the power of num_two and assign the value to a variable exp

exp = num_one ** num_two
print("Exponent of variable one to variable two is: ", exp)

        ## vii. Find floor division of num_one by num_two and assign the value to a variable floor_division

floor_division = num_one // num_two
print("Floor division of variable one to variable two is: ", floor_division)

    ## 5. The radius of a circle is 30 meters
        ## i. Calculate the area of a circle and assign the value to a variable name of area_of_circle

radius = 30
area_of_circle = 3.14*(radius**2)
print("The area of the circle with radius 30 is: ",area_of_circle)

        ## ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

circum_of_circle = 2*3.14*radius
print("The circumference of the circle with radius 30 is: ",circum_of_circle)

        ## iii. Take radius as user input and calculate the area.

usr_rad = int(input("Please input the radius: "))
area_circle = 3.14*(usr_rad**2)
print(f"The area of user circle with radius {usr_rad} is: ",area_circle)

    ## 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

##ans>>
first_name, last_name, country, age = input("first name: "), input("last name: "), input("country: "), input("age: ")

print("first name is", first_name, "and last name is ", last_name, "and country is ", country, "and age is ", age)

    ## 7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
        ##ans>> answer performed in command prompt