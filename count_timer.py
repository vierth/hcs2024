import time

s = time.time()
for i in range(10000):
    my_string = 'this has many ??????'
e = time.time()

print(e-s)

s= time.time()
for i in range(10000):
    qs = 0
    for char in my_string:
        if char == "?":
            qs += 1

e = time.time()

print(e-s)