'''Class Task : Introduction to Strings

1. Create a string with your full name and print first and last character.
2. Slice 'Programming' into 'Prog', 'gram', 'ing'.
3. Apply .strip(), .lower(), .replace() on ' Python is AWESOME '.
4. Take user input of favorite language and display message.
5. Count how many times 'Python' appears in 'I love Python because Python is powerful'.'''

task1 = "Muhammad Sheikh"
print(task1[0])
print(task1[-1])

task2 = 'Programming'
print(task2[0:4])
print(task2[3:7])
print(task2[8:])

task3 = ' Python is AWESOME '
print(task3.lower())
print(task3.replace("Python","Java"))
print(task3.strip())

task4 = input("Whts your fav language: ")
print(task4)

task5 = 'I love Python because Python is powerful'
print(task5.count("Python"))