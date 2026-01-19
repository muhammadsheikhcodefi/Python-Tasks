# Class Task: Tuples In Python

'''Create a tuple of your 5 favorite cities and print the first and last city.
Find the maximum and minimum value in a numeric tuple (34, 7, 99, 12, 56).
Create a nested tuple that contains your name and marks in 3 subjects, then print the second subject's mark.
Convert a tuple (10, 20, 30) into a list, append 40 to the list, and convert it back into a tuple.
Write a Python program to check if the number 50 exists in the given tuple (10, 20, 30, 40, 50).'''

task1 = ("karachi","Lahore","Multan","Quetta","Hyderabad")
print(task1[0])
print(task1[-1])

task2 = (34, 7, 99, 12, 56)
print(f"Maximum Value: {max(task2)}")
print(f"Minimum Value: {min(task2)}")

task3 = ("Muhammad",(90,99,85))
print(f"Second Subject Marks: {task3[1][1]}")

task4 = [10, 20, 30]
task4.append(40)
task_4 = tuple(task4)
print(task_4)

task5 = (10, 20, 30, 40, 50)
print(50 in task5)