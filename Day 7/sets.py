## Day 7 of 30 days of Python programming

## Day 7 Sets

## Exercise 1

## 1. Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

## 2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

## 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Intuit',"Adobe","Databricks"]) ## pass the items as a list
print(it_companies)

## 4. Remove one of the companies from the set it_companies
it_companies.remove("Databricks")
print(it_companies)

## 5. What is the difference between remove and discard
print("The difference between discard and remove is that while both remove an\nitem in the set, discard does not raise an error\nwhen an item does not exist in the set\nwhile remove raises an error")

## Exercise 2

## 1. Join A and B
C = A.union(B)
print(C)

## 2. Find A intersection B
print(A.intersection(B))

## 3. Is A subset of B
print(A.issubset(B))

## 4. Are A and B disjoint sets
print(A.isdisjoint(B))

## 5. Join A with B and B with A
print(A.union(B))
print(B.union(A))

## 6. What is the symmetric difference between A and B
print(A.symmetric_difference(B))

## 7. Delete the sets completely
del A
del B

## Exercise 3

## 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set =  set(age)
print("Is age list greater than or equal to age set?", len(age)>=len(age_set))
print(len(age_set), len(age))

## 2. Explain the difference between the following data types: string, list, tuple and set
print("\nA string is anything within \"double quotes\" or 'single quotes'")
print("While a list a collection of ordered indexed items that can store non-unique values and is mutable")
print("A tuple on the other hand cannot be changed/mutated and is also a collected of non-unique ordered indexed items")
print("A set is a mutable item but it is a collection on unqiue unordered unindexed items")

## 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

## using sets
string_val = "I am a teacher and I love to inspire and teach people."
vals = string_val.split()
print(set(vals))