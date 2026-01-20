# Class Task While Loop

'''Task 1:
Write a program using while loop to print the multiplication table of 7.'''
constant = 7
n = 0
table = 0

while n < 10:
    n += 1
    table = constant * n
    print(f"{constant} * {n} = {table}")

'''Task 2:
Write a program that asks the user to enter numbers until they enter 0. Then display the sum of all entered numbers.'''
summ = 0
while True:
    user = int(input("enter numbers until you enter 0: "))
    if user == 0:
      break
    else:
      summ += user
print(summ)

'''Task 3:
Write a program to count how many digits are in a number using a while loop.'''
n = 12
digit_sum = 0
while n > 0:
  digits = n % 10
  digit_sum += digits
  n //= 10
print(digit_sum) 

'''Task 4:
Write a program that prints all numbers divisible by 3 and 5 between 1 and 100.'''
n = 1
while n <= 100:
    if n % 3 == 0 and n % 5 == 0:
        print(n)
    else:
        pass
    n += 1

'''Task 5:
Create a simple guessing game using a while loop. Let the user guess a number until they get it right.'''
print('''Guess a Random Number
Hint: Range is (1 to 10) \n''')
n = 10
count = 1
while True:
  user = int(input("Guess now: "))
  if user >= 11:
    print("Out of Range Guess, Try Again \n")
    count += 1
  else: 
    if user == n:
      print(f'Your Guess is Correct in {count} tries')
      break
    else: 
      print("Wrong guess, Try Again \n")
      count += 1