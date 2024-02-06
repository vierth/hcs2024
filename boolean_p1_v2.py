# a boolean expression will return one of two values
True
False

# test if two values are the same
print(5 == 5)
# true

# test if two values are NOT the same
5 != 5

# test if one value is larger than another
5 > 6
# False

# Less than or equal to
5 <= 6

# greater than or equal to
5 >= 6

# are two strings the same?
print("a" == "b")

print("a" < "b")

# check if two things are the same object
list_one = ["hello"]
list_two = ["hello"]

print(list_one is list_two)
print(id(list_one))
print(id(list_two))
list_one = list_two
print(list_one is list_two)