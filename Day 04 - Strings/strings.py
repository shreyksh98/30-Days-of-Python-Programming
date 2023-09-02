## Day 4 of 30 days of Python

##Exercise - Day 4

## 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
s1, s2, s3, s4 = "Thirty ","Days ","Of ","Python "
single_string = s1+s2+s3+s4
print(single_string)

## 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
c1, c2, c3 = "Coding ", "For ", "All"
single_string = c1+c2+c3
print(single_string)

## 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

## 4. Print the variable company using print().
print(company)

## 5. Print the length of the company string using len() method and print().
print(len(company))

## 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

## 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

## 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize(), company.title(), company.swapcase())

## 9. Cut(slice) out the first word of Coding For All string.
val = "Coding For All"
print(val[:7])

## 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
sub_string = "Coding"
print(val.index(sub_string))
print(val.rindex(sub_string))
print(val.find(sub_string))

## 11. Replace the word coding in the string 'Coding For All' to Python.
print(val.replace("Coding","Python"))

## 12. Change Python for Everyone to Python for All using the replace method or other methods.
a = "Python for All"
print(a.replace("All","Everyone"))

## 13. Split the string 'Coding For All' using space as the separator (split()) .
print("Coding For All".split(" "))

## 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

## 15. What is the character at index 0 in the string Coding For All.
print(val[0])

## 16. What is the last index of the string Coding For All.
print(val[-1])

## 17. What character is at index 10 in "Coding For All" string.
print(val[10])

## 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
words = "Python For Everyone".split()
print(words[0][2] + words[1][1] + words[2][1])

## 19. Create an acronym or an abbreviation for the name 'Coding For All'.
b = val.split()
print(b[0][0] + b[1][0] + b[2][2])

## 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(val.index('C'))

## 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(val.index('F'))

## 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(val.rfind('l'))

## 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sent = 'You cannot end a sentence with because because because is a conjunction'
print(sent.find('because'))

## 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sent.rfind('because'))

## 25.  Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sent.replace('because',''))

## 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sent.find('because'))

## 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sent.replace('because',''))

## 28. Does ''Coding For All' start with a substring Coding?
print(val.startswith('Coding'))

## 29. Does 'Coding For All' end with a substring coding?
print(val.endswith('coding'))

## 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip(" "))

## 31. Which one of the following variables return True when we use the method isidentifier():
## 30DaysOfPython
## thirty_days_of_python
a,b = "30DaysOfPython","thirty_days_of_python"
print(a.isidentifier)
print(b.isidentifier())

## 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
l = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(l))

## 33. Use the new line escape sequence to separate the following sentences. 
print("I am enjoying this challenge.\nI just wonder what is next.")

## 34. Use a tab escape sequence to write the following lines.
print("Name\tAge\tCountry\tCity\nShrey\t200\tUSA\tNYC")

## 35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

## 36. Make the following using string formatting methods:
print('8 + 6 = 14')
print('8 - 6 = 2')
print('8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144')