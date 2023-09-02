# Day 13 of 30 days of Python

# Day 13 List Comprehension

# 1. Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

pos_num = [i for i in numbers if i>0]
print(pos_num)

# 2. Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

lst_flt = [i for a in list_of_lists for b in a for i in b]
print(lst_flt)

# 3. Using list comprehension create the following list of tuples:

# lst_tup = [t for t in range(11) lambda x: (x, 1, x**2, x**3, x**4, x**5, x**6)]
# print(lst_tup)

lst = []
for i in range(11):
    a = (lambda i: (i, 1, i**2, i**3, i**4, i**5, i**6))(i)
    lst.append(a)
print(lst)

# 4. Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lst = []
for i in countries:
    for j in i:
        j = [x.upper() for x in list(j)]
        city = j[0]
        new_city = city[:3]
        j.insert(1, new_city)
        lst.append(j)
print(lst)

# 5. Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_dict = {}
new_lst = []
for i in countries:
    for j in i:
        j = [x.upper() for x in j]
        new_dict['country'] = j[0]
        new_dict['city']=j[1]
        new_lst.append(new_dict)
print(new_lst)

# 6. Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_lst = []
for i in names:
    for j in i:
        a,b = j
        new_name = a + " " + b
        # print(new_name)
        new_lst.append(new_name)
print(new_lst)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.

x = lambda y1,y2,x1,x2: (y2-y1)/(x2-x1)

print(x(1,2,3,4))