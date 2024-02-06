# loops let you execute code over and over again

i = 0
while i < 100:
    print(f"{i} is less than 100")
    #i = i + 1
    i += 1

# for loops are less dangerous than while loops
# print 0 to 9
# range() creates iterator
for number in range(10):
    print(number)

# specify the starting place
for number in range(5,10):
    print(number)

# specify steps
for number in range(5,10,2):
    print(number)


for i in range(10):
    print(i)
    i += 10
    print(i)

my_list = ["a", "b", "c", "d"]
my_string = "chugalug"

for item in my_list:
    print(item)

for character in my_string:
    print(character)
