## Day 5 of 30 days of Python

## Exercise: Day 5

##Exercises level 1

## 1. Declare an empty list

lst = []
print(lst)

## 2. Declare a list with more than 5 items
lst = [1,2,3,4,5,6]
print(lst)

## 3. Find the length of your list
print(len(lst))

## 4.  Get the first item, the middle item and the last item of the list
a = lst[0] #first item
b = len(lst)-1 
c = lst[b] #last item

def mid_value(input_list):
    mid_val = float(len(input_list))/2
    if mid_val%2 != 0:
        return input_list[int(mid_val-0.5)]
    else:
        return input_list[int(mid_val)], input_list[int(mid_val-1)]

print(mid_value(lst))

## 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Shrey',200,'6ft','Not Married','NYC']
print(mixed_data_types)

## 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

## 7. Print the list using print()
print(it_companies)

## 8. Print the number of companies in the list
print(len(it_companies))

## 9. Print the first, middle and last company
print(it_companies[0]) #first
print(it_companies[-1]) #last

#middle
def string_middle(input_list):
    vals = float(len(input_list))/2
    if vals%2 != 0:
        return input_list[int(vals-0.5)]
    else:
        return (input_list[vals], input_list[vals-1])

print(string_middle(it_companies))

## 10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

## 11. Add an IT company to it_companies
it_companies.append('Intuit')
print(it_companies)

## 12. Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Nvidia')
print(it_companies)

## 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0]= it_companies[0].upper()

print(it_companies)

## 14. Join the it_companies with a string '#;  '
joined_comp = '#; '.join(it_companies)
print(joined_comp)

## 15. Check if a certain company exists in the it_companies list.
print(it_companies.index('META'))

## 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

## 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

## 18. Slice out the first 3 companies from the list
print(it_companies[3:])

## 19. Slice out the last 3 companies from the list
print(it_companies[:-3])

## 20. Slice out the middle IT company or companies from the list
print(it_companies[4:5])

## 21. Remove the first IT company from the list
del it_companies[0]

## 22. Remove the first IT company from the list
del (it_companies[len(it_companies)//2])

## 23. Remove the last IT company from the list
it_companies.pop()

## 24. Remove all IT companies from the list
it_companies.clear()

## 25. Destroy the IT companies list
del it_companies

## 26.Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)

## 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end + back_end
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)

## Exercise Level 2

## 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
## Sort the list and find the min and max age
## Add the min age and the max age again to the list
## Find the median age (one middle item or two middle items divided by two)
## Find the average age (sum of all items divided by their number )
## Find the range of the ages (max minus min)
## Compare the value of (min - average) and (max - average), use abs() method

ages.sort()
print(min(ages), max(ages))

ages.append(min(ages))
ages.append(max(ages))

def string_middle(input_list):
    input_list.sort()
    vals = float(len(input_list))/2
    if vals%2 != 0:
        return input_list[int(vals-0.5)]
    else:
        return (input_list[int(vals)], input_list[int(vals-1)])

print(string_middle(ages))

print(sum(ages)/len(ages))

print(max(ages)-min(ages))

print(abs(min(ages) - (sum(ages)/len(ages))))
print(abs(max(ages) - (sum(ages)/len(ages))))

## 1. Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

print(string_middle(countries))

## 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.

def string_middle(input_list):
    input_list.sort()
    vals = float(len(input_list))/2
    if vals%2 != 0:
        return int(vals-0.5)
    else:
        return (int(vals), int(vals-1))

lst = string_middle(countries)
print(lst)

l1, l2 = [], []
if lst%2 != 0:
    l1 = countries[:lst+1]
    l2 = countries[lst+1:]
else:
    l1 = countries[:lst]
    l2 = countries[lst:]
print(l1, l2)

## 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *rest = country
print(*rest)