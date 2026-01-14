'''Class Task : Print statement and variables

Task 1: Simple Print
Print your name.
Print your age.
Print your favorite color.'''

print("Muhammad Sheikh")
print(18)
print("Yellow")

'''Task 2: Variables Basics
Create a variable called name and store your name in it.
Create a variable called age and store your age in it.
Print both variables.'''

name = "Muhammad Sheikh"
age = 18
print(f'''{name} 
{age}''')

'''Task 3: Sentence with Variables
Store your city in a variable city.
Store your country in a variable country.
Print: I live in <city>, <country>.'''

city = "Karachi"
country = "Pakistan"
print(f"I live in {city}, {country}")

'''Task 4: Adding Numbers
Store two numbers in variables a and b.
Print their sum, difference, product, and division.'''

a = 1
b = 2
print(f"sum: {a+b}")
print(f"difference: {a-b}")
print(f"product: {a*b}")
print(f"division: {a/b}")

'''Task 5: Personal Introduction
Store the following in variables:
name
age
hobby
Print a full sentence like: My name is Ali, I am 20 years old, and I like cricket'''

name = "Muhammad Sheikh"
age = 18
hobby = "Coding"
print(f"My name is {name}, I am {age} years old, I like {hobby}")

''' Task 6: Swapping Values
Store two values in variables x and y.
Print them before swapping.
Swap their values.
Print them after swapping.'''

x = 0
y = 1
print("Before Swapping: ", x,y)
x,y=y,x
print("After Swapping: ", x,y)

'''Task 07: Temperature Conversion
Store temperature in Celsius in a variable celsius.
Convert it into Fahrenheit using formula:
fahrenheit = (celsius * 9/5) + 32
Print both values.'''

celsius = 10
fahrenheit = (celsius * 9/5) + 32
print("celsius", celsius)
print("fahrenheit", fahrenheit)

'''Task 08:
Create variables for 3 grocery items and their prices.
Print them like:
Apples = 120
Milk = 200
Bread = 80'''

item1 = "Apple"
item2 = "Milk"
item3 = "Bread"

price1 = "120"
price2 = "200"
price3 = "80"

print(f'''{item1} = {price1}
{item2} = {price2}
{item3} = {price3}''')

'''Task 09: Area of Rectangle
Store length and width in variables.
Calculate area = length * width.
Print the area in a sentence.'''

length = 50
width = 100
area = length * width
print("Area: ", area)