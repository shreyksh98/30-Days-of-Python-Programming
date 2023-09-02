## Day 3 of 30 days of python

## Exercise - Day 3

## 1. Declare your age as integer variable
age = 200

## 2. Declare your height as a float variable
height = 69.9

## 3. Declare a variable that store a complex number
complex = (3j +2)

## 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = float(input("Enter base: "))
h = float(input("Enter height: "))
print("Area of triangle is: ", (0.5*b*h))

## 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print("Perimeter of triangle is: ", (a+b+c))

## 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
l = int(input("Enter length: "))
w = int(input("Enter width: "))

print(f"The area of the rectangle is {(l*w)} and perimeter of rectangle is {(2*(l+b))}")

## 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = float(input("Enter radius: "))

print(f"The area of circle is {(3.14*(r**2))} and circumference of circle is {(3.14*2*r)}")

## 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
## to calculate the x-intercept, we assume y to be 0 first, so 
x = 2/2
y = 0-2
m_slope_8 = (0-y)/(x-0)
print(f"The x-intercept is {x}, y intercept is {y} and slope is {m_slope_8}") 

## 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1, x2, y2 = 2,2,6,10
m = (10-6)/(6-2)
d = ((((6-2)**2)+((10-6)**2))**0.5)
print(f"The slope is {m} and distance is {d}")

## 10. Compare the slopes in tasks 8 and 9.
print(f"slope of task 8 is {m_slope_8} and slope of task 9 is {m}")

## 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x1 = 1
x2 = 2
x3 = -3
x4 = -2
y1 = ((x1**2) + (6*x1) + 9)
y2 = ((x2**2) + (6*x2) + 9)
y3 = ((x3**2) + (6*x3) + 9)
y4 = ((x4**2) + (6*x4) + 9)

print(f"when x is 1, y is {y1}, when x is 2, y is {y2}, when x is -3, y is {y3} and when x is -2, y is {y4}")
print("y is 0 when x is -3")

## 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
a, b = 'python', 'dragon'
print("Is length of python and dragon same? : ", (len(a) is len(b)))

## 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("Does 'on' both in python and dragon?: ",('on' in a and 'on' in b))

## 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
s = "I hope this course is not full of jargon"
print("Is jargon in the sentence?: ",('jargon' in s))

## 15. There is no 'on' in both dragon and python
print("There is no on in python and dragon: ",('on' not in a and 'on' not in b))

## 16. Find the length of the text python and convert the value to float and convert it to string
l = len(a)
fl = float(l)
st = str(fl)

print(type(st))

## 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input("Enter a number: "))
print("Is the number even?: ",(num%2 == 0))

## 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
d = 7//3
print("Are the values same? ",(d is int(2.7)))

## 19. Check if type of '10' is equal to type of 10
print("Are they equal? ",(type('10') is type(10)))

## 20. Check if int('9.8') is equal to 10
print("Are the equal? ",int(9.8) is 10)

## 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hrs = input("Enter number of hours: ")
rate = input("Enter rate: ")
print("Total earning = ",(float(hrs)*float(rate)))

## 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
yrs = int(input("Enter number of years: "))
secs = yrs * 365 * 24 * 60 * 60
print(f"Number of seconds in {yrs} years are: ",secs) 

##23. Write a Python script that displays the following table
## 1 1 1 1 1 
## 2 1 2 4 8
## 3 1 3 9 27
## 4 1 4 16 64
## 5 1 5 25 125

print(1," ",1**0," ",1**1," ",1**2," ",1**3)
print(2," ",2**0," ",2**1," ",2**2," ",2**3)
print(3," ",3**0," ",3**1," ",3**2," ",3**3)
print(4," ",4**0," ",4**1," ",4**2," ",4**3)
print(5," ",5**0," ",5**1," ",5**2," ",5**3)

## we can write it with for loops as well

for i in range(1,6):
    print(i," ",i**0," ",i**1," ",i**2," ",i**3)



