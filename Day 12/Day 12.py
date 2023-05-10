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

# 2.1 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

from modulo import gen_hex
print(gen_hex())

# 2.2 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

from modulo import list_of_rgb_colors
print(list_of_rgb_colors(2))

# 2.3 Write a function generate_colors which can generate any number of hexa or rgb colors.

from modulo import generate_colors

print(generate_colors('rgb',2))

# Exercise 3

# 3.1 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

from modulo import shuffle_list
print(shuffle_list([1,2,3,4,5,6,7]))

# 3.2 Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

from modulo import rand_int
print(rand_int())

