# methods

# strings
my_string = "hello, how are youoooooooooOOOOOOOOOO"
my_string_2 = 'hello, how are  you'

# string method count()
search_term = "z"
term_count = my_string.count(search_term)

# find: python is zero indexed (first position is zero)
# will ONLY find the first instance of something
# will return -1 if it does not find anything
location = my_string.find(search_term)

print(term_count)
print(location)