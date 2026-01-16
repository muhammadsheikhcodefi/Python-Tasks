# Class Task List Methods

'''Create a list of 5 student names.
Add a new student using append().
Insert one name at index 2.
Remove one name using remove().
Finally, sort the list.'''

stdName = ["Muhammad", "Ali", "Bilal", "Minhaj", "Majid"]
stdName.append("Abdul")
stdName.insert(2, "Alam")
stdName.remove("Majid")
stdName.sort()
print(stdName)


# Student Tasks (Without Solutions) Try these tasks on your own:

#  Create a list of numbers and use pop() to remove the last two items.
n = [1,2,3,4,5]
removedN = n.pop()
removedN = n.pop()
print(n)

#  Make a list of 5 countries. Use insert() to add one at index 3, then use count() to count a specific country.
countries = ["Pakistan","Iran","India","China","Russia"]
countries.insert(3, "Italy")
print(countries.count("Pakistan"))
print(countries)

#  Create a list of integers. Use sort() and then reverse() to show them in descending order.
n = [8,6,7,2,6]
n.sort()
print(f"Sorting Integers: {n}")
n.reverse()
print(f"Sorting Integers: {n}")

#  Use copy() to duplicate a list. Change one element in the copy and show that the original list remains unchanged.
n = [1,2,3,4,5]
copyN = n.copy()
print(f"Copy List Before Update: {copyN}")
copyN[1] = 50
print(f"Copy List After Update: {copyN}")
print(f"Original List: {n}")

#  Combine two lists of fruits and vegetables and check if 'apple' is present in the combined list.
fruits = ["apple", "banana", "orange"]
vegetables = ["okra", "potato", "onion"]

combined = fruits + vegetables
print("apple" in combined)