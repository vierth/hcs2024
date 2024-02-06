one = "1"
one_int = 1
one_float = 1.0

# function to check an object's type
# type()

print(type(one)) 
print(type(one_int))    

# you can change the type of a data with type coersion
one = int(one)
print(type(one))

# change it into a float
one = float(one)
print(one)

print(int(1.5))

# turn something into a string
print(type(str(1.5)))