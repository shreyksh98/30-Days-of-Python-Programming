## Day 6 of 30 days of Python Programming

## Day 6 - Tuples

## Exercise: Level 1

## 1. Create an empty tuple
empty_tuple = tuple()
# or
tuple1 = ()

## 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("brother 1", "brother 2", "brother 3")
sisters = ("sister 1", "sister 2",)
print(brothers, sisters)

## 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

## 4. How many siblings do you have?
print(len(siblings))

## 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.insert(0, "father")
family_members.insert(1, "mother")
family_members = tuple(family_members)
print(family_members)

## Exercise: Level 2

## 1. Unpack siblings and parents from family_members
father, mother , *siblings = family_members
print(*siblings) 

## 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("mango", "banana", "apple")
veggies = ("okra", "cabbage", "onions")
animal_prod = ("milk", "cheese", "curd")
food_stuff_tp = fruits+veggies+animal_prod
print(food_stuff_tp)

## 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

## 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
def mid_item(lst):
    len_lst = int(len(lst))
    if len_lst%2 == 0:
        val = len(lst)/2
        return (lst[int(val)], lst[int(val+1)])
    else:
        val = (len(lst)/2)-0.5
        return(lst[int(val)])

print(mid_item(food_stuff_lt))

## 5. Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three, last_three)

## 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

## 7. Check if an item exists in tuple:
## Check if 'Estonia' is a nordic country

## Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)

