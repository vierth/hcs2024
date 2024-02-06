# If statements are useful when youn want to execute code only if something is true, otherwise skip it

# we are going to use code blocks for this
# in python code blocks are formed with indendtation

if 10 < 20:
    print("exactly")

if 10 > 20:
    print("we should never encounter this code")

print('here we are')

if 30 < 20:
    print('thirty is less than twenty')
else:
    print('this is expected')


# add multiple conditions
if 10 > 10:
    a = "10 is larger than 10"
elif 10 == 10:
    a = "10 is equal to 10"
elif 10 < 10:
    a = "10 is less than 10"
else:
    a = "everythign is meaningless"

# the order matters, and this is one of the first places we can encounter runtime bugs
    
my_number = 10

if my_number > 1:
    res = "this is cloest to 1"
elif my_number > 5:
    res = "this is closest to 5"
elif my_number > 8:
    res = "this is closest to 8"
else:
    res = "unknown"

print(res)