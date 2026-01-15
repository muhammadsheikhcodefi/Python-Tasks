# Class Task Python String Slicing

'''From 'DataScience', extract 'Data', 'Science', 'ataSci'.
From 'Programming', extract 'ing' and 'gram' using negative indexing.
From 'ABCDEFGHIJ', print every 2nd char, every 3rd char, and reverse.
Take user input and print first 3, last 3, and middle part.
Reverse each word in 'Python is fun' → 'nohtyP si nuf'.'''


task1 = 'DataScience'
print(task1[0:4])
print(task1[4:])
print(task1[1:7])

task2 = 'Programming'
print(task2[-3:])
print(task2[-8:-4])

task3 = 'ABCDEFGHIJ'
print(task3[1::2])
print(task3[2::3])
print(task3[::-1])

task4 = (input(": "))
print(task4[0:3])
print(task4[-3:])
# for mid:
mid = len(task4)//2
if len(task4) % 2 == 0:
  print(task4[mid-1:mid+1])
else:
  print(task4[mid])

task5 = 'Python is fun'
print(task5[::-1])
