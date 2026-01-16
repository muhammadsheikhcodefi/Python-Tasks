# Class Task: Introduction to Lists

'''Create a list of 6 countries and print the third one.
Example: countries = ['A', 'B', ...]'''

countries = ["Pakistan", "India", "Nepal", "China", "Russia", "Iran"]
print(countries[2])

'''Student Task 2:
Create a list of 8 numbers and print all numbers from index 2 to 6 (inclusive of start, exclusive of end as usual).'''

n = [1,2,3,4,5,6,7,8]
print(n[2:6])

'''Student Task 3:
Store 5 favorite movies in a list and change the last one to a new movie.'''

favMovies = ["John Wick", "Spider Man", "Justice League", "Home Alone", "Jurasic World"]
favMovies[-1] = "Dead Pool"
print(favMovies)

'''Student Task 4:
Create a list of 7 temperatures and print the last two using negative indexing.'''

temp = [10,20,30,40,50,60,70]
print(temp[-2:])


'''Student Task 5:
Make a nested list containing 3 lists and access the second element of the second list.'''

x = [1,2, [True, False, ["a","b","c"]]]
print(x[2][1])