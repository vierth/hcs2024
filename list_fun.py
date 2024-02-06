# lists are a datatype that can contain multiple objects in a specific order

# we can create lists in two ways
my_list = []
# we can use the list function
my_list = list()

# we can create non empty lists by seperating elements with commas
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
another_list = [3, 8, 2, 1, -500]

# lists can contain ANY type of python object
third_list = ["my", "name", "is", "paul", "vierthaler"]

# we can alsdo mix datatypes
fourth_list = [1, 4, "hello"]

# we can nest lists to our hearts content
five = [[1,3], [2,7], [2,-1]]

# we get information from lists based on the index of the items in the list (just like strings)

# first item from my_list
print(my_list[0])

# last item
print(my_list[-1])

# trying to grab somethign that doesn't exist generates an error
# my_list[100]

# getting slices of lists
print(my_list[1:4])

# how many items are in our list?
print(len(five))


