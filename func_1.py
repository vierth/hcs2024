# we can create custom functions to do whatever we would like
def pauls_fuction():
    # anything inside this function will run when I call the function
    print("Hello! This is a nice function")

# we can provide input to our functions easily
def whose_function(name):
    print(f"Hi, my name is {name}")

# we can have multiple inputs
def multi_input_function(name_1, name_2):
    print(f"Hi {name_1}, my name is {name_2}")

# add default values
def greeting(name_1, name_2, greeting_type="hello"):
    if greeting_type == "hello":
        print(f"Hello {name_1}, my name is {name_2}")
    elif greeting_type == "goodbye":
        print(f"Goodbye {name_1}, my name is {name_2}")

# to run the function i just call it
pauls_fuction()
whose_function("Joe")
multi_input_function("Joe", "Paul")
greeting("joe", "paul")
greeting("joe", "paul", "goodbye")
greeting("joe", "paul", greeting_type="goodbye")