# key errors are when we look for a key in a dictionary that doesn't exit
my_dict = {'run':15, 'walk':30}

try:
    print(my_dict['amble'])
except KeyError:
    my_dict['amble'] = 20

print(my_dict)