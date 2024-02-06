# here is a string
my_string = "My name is Paul Vierthaler."

new_list = list(my_string)

print(new_list)

# split a string into a list
new_list_2 = my_string.split(" ")
print(new_list_2)

# let's turn a list into a string
new_string = " ".join(new_list_2)
print(new_string)

# check the length of a list
len(new_list_2)
min(new_list)
max(new_list)

new_list.sort() # transforms list in place
print(new_list)

new_list.sort(reverse=True) # transforms list in place
print(new_list)
