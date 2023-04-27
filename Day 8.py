## Day 8 of 30 days of Python

# Day 8 Dictionaries

# 1. Create an empty dictionary called dog

dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary

dog = {
    'name' : 'Brownie',
    'color' : 'Golden',
    'breed' : 'Labradoodle',
    'legs' : 4,
    'age' : '2 years'
}

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    'first_name' : 'Shrey',
    'last_name' : 'Kshatriya',
    'gender' : 'Male',
    'age' : '25',
    'skills' : ['Communication', 'Data Analysis', 'Gaming', 'Cooking'],
    'country' : 'USA',
    'city' : 'New York City',
    'address' : '20 W 34th st New York, NY 10001'
}

# 4. Get the length of the student dictionary

print(len(student))

# 5. Get the value of skills and check the data type, it should be a list

print(student.get('skills'))
print(type(student['skills']))

# 6. Modify the skills values by adding one or two skills

student['skills'].append('Coding')
print(student['skills'])

# 7. Get the dictionary keys as a list

print(list(student.keys()))

# 8. Get the dictionary values as a list

print(list(student.values()))

# 9. Change the dictionary to a list of tuples using items() method

print(student.items())

# 10. Delete one of the items in the dictionary

    # 10.1 pop
student.pop('country')
    # 10.2 popitem
student.popitem()
    # 10.3 del
del student['last_name']

# 11. Delete one of the dictionaries

del student