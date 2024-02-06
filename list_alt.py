# mutable vs immutable
# strings are immutable, int, float, tuples 
# lists are mutable
# changing lists

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(my_list)
# add things to my list, i use append
my_list.append(10)

print(my_list)

# we can remove things from a list quite easily with pop()
deleted_num = my_list.pop()

print(my_list)
print(deleted_num)

# specify where it pops the item from
other_num = my_list.pop(2)
print(my_list, other_num)

# inserting an item with insert()
my_list.insert(2, 28)
print(my_list)

# we can change the value of an index simply
my_list[0] = 42
print(my_list)

# this happens in place