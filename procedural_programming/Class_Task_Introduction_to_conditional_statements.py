'''Class Tasks : Introduction to conditional statements'''

'''Print 'Child' if age < 18 else 'Adult'''
age = int(input("Enter your age: "))

if age < 18:
    print('Child')
else:
    print("Adult")

'''Print "It's hot." if temperature > 30 else It's cool.'''
temp = 30

if temp > 30:
    print("Its hot")
else:
    print("It's cool")

'''Print 'Divisible by 5' or 'Not divisible by 5'''
num = int(input("Enter num: "))

if num % 5 == 0:
    print('Divisible by 5')
else:
    print('Not divisible by 5')

'''Print 'Positive' if >0 else 'Negative or Zero'''
n = int(input("Enter Number: "))

if n > 0:
    print("Positive")
else:
    print("Negative")