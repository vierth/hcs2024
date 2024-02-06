# Reading and writing files is very important for saving results

# write to a file
# be VERY careful with this
# creates file if none exists, erases one if it does exist and writes new one

# opening a file to write to
write_file = open("demo.txt", "w", encoding='utf8')
write_file.write("This is what I want to write")
write_file.close()

# context manager closes things for you
with open("demo_2.txt", "w", encoding='utf8') as write_file:
    write_file.write("this is a second file")

# reading form files is way less dangerous
with open("demo_2.txt", "r", encoding="utf8") as rf:
    contents = rf.read()

print(contents)

# add to a file with the "a" flag
with open('demo_2.txt', 'a', encoding='utf8') as af:
    af.write("More stuff")