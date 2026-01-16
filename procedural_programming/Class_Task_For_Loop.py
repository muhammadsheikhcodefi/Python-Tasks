# Class Task For Loop

# Print all numbers from 1 to 15 and show their cubes.
for i in range(1,16):
    print(f"Cube of {i}: {i*3}")


# Print only the names that start with ‘A’ from this list: ['Ali', 'Sara', 'Asad', 'Hina', 'Ahsan']
name = ['Ali', 'Sara', 'Asad', 'Hina', 'Ahsan']
for i in name:
  if i.startswith("A"):
    print(i)

# Write a loop to find the sum of all even numbers between 50 and 100.
n = 0
for i in range(50,100):
    if i % 2 == 0:
        n += i
print(n)
        
# Write a for loop to count how many uppercase letters are in 'HelloPYTHON'.
letters = 'HelloPYTHON'
count = 0
for i in letters:
    if i.upper() == i:
        count += 1
print(count)

'''Use a for loop to print this pattern:
*
**
***
****
*****'''
n = 0
for i in range(0,5):
  n += 1
  print("*"*n)

# Print numbers from 10 down to 1 using a for loop.
for i in range(1,11):
  print(-i+11)

# Create a list of marks [78, 55, 90, 67, 82] and print 'Pass' if mark ≥ 60, otherwise 'Fail'.
marks = [78, 55, 90, 67, 82]
for i in marks:
  print("pass" if i >= 60 else "fail")

# Write a program to print all elements of this list in reverse order: ['red', 'green', 'blue', 'yellow']
order = ['red', 'green', 'blue', 'yellow']
for i in order[::-1]:
  print(i)
  
# Use a nested for loop to print multiplication tables from 2 to 5.
for i in range(2,5):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")

# Write a for loop to print all characters that are not vowels from 'education'.
vowel = "education"
for i in vowel:
    print(i if i in "aeiou" else "no vowel")
