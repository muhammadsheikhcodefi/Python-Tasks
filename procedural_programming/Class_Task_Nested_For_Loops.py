# Class Task:

'''1. Print the following pattern:
*
* *
* * *
* * * *
* * * * *'''
for i in range(1,6): # 1 2 3 4 5
  for j in range(i): # 0 01 012 0123 0124
    print("*", end = " ")
  print()

#2. Print only odd numbers from a 2D list.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in matrix:
    for j in i:
        if j % 2 != 0:
            print(j, end = " ")
    
#3. From list of strings ['hi', 'python'], print only consonants.
con = ['hi', 'python']

for i in con:
    for j in i:
      if j not in "aeiou":
        print(j, end = "")

#4. Print all pairs (i, j) where i + j is even.
for i in range(1,5): 
  for j in range(1,6): 
    if (i+j) % 2 == 0:
      print(i,j)

'''5. Create a pattern of numbers like:
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1'''

for i in range(1,6): # 1 2 3 4 5 
  for j in range(5,5-i,-1): # 5 54 543 5432 54321
    print(j, end = " ")
  print() 

# Bonus Task:

'''1. Inverted right triangle

****
 ***
  **
   *'''

for i in range(4,0,-1): # 4 3 2 1
  for j in range(4-i): #  0 1 2 3
    print(" ", end = "")
  for k in range(i): # 4 3 2 1 
    print("*",end = "")
  print()

'''2. Diamond pattern

   *
  ***
 *****
*******
 *****
  ***
   *'''

n = 4

for i in range(1, 5): # 1 2 3 4
  for j in range(n - i): # 3 2 1 0
    print(" ", end = "")
  for k in range(i*2 - 1): #1 3 5 7 (odd)
    print("*", end = "")
  print()

for i in range(3,0,-1): # 3 2 1
  for j in range(n - i): # 1 2 3
    print(" ", end = "")
  for k in range(i * 2 - 1): # 7 5 3 1
    print("*", end = "")
  print()
  
'''3. Number pyramid
   1
  121
 12321
1234321'''

for i in range(1,5): # 1 2 3 4
  for j in range(4 - i): # 3 2 1 0
    print(" ", end = "")
  for j in range(1, i + 1): # 1 12 123 1234
    print(j, end = "")
  for j in range(i-1, 0,-1): # 0 1 21 321
    print(j, end = "")
  print() 
  
'''4. Create a pattern of numbers like:
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1'''

n = 5

for i in range(1,n+1): # 1 2 3 4 5
  for j in range(i, 0, -1): # 
    print(j, end = "")
  print()
  