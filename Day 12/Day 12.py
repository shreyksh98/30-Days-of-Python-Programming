## Day 12 of 30 days of Programming

# Day 12 - Modules

# Exercise 1

# 1.1 Write a function which generates a six digit/character random_user_id.

# we have written a function within the modulo module and we will import and use it
from modulo import random_string
print(random_string(6))

# 1.2 Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

from modulo import user_id_gen_by_user
user_id_gen_by_user(5,10)

# 1.3 Write a function named rgb_color_gen. 
# It will generate rgb colors (3 values ranging from 0 to 255 each).

from modulo import rgb_color_gen
print(rgb_color_gen())

# Exercise 2

# 2.1
