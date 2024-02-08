import time

"""This script will calculate the most common 
character in a paragraph"""

my_paragraph = """In the year 1878 I took my degree of Doctor of Medicine of the
University of London, and proceeded to Netley to go through the course courses
prescribed for surgeons in the army. Having completed my studies there,
I was duly attached to the Fifth Northumberland Fusiliers as Assistant
Surgeon. The regiment was stationed in India at the time, and before I
could join it, the second Afghan war had broken out. On landing at
Bombay, I learned that my corps had advanced through the passes, and
was already deep in the enemy’s country. I followed, however, with many
other officers who were in the same situation as myself, and succeeded
in reaching Candahar in safety, where I found my regiment, and at once
entered upon my new dutiesaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa."""

delete_chars = [".", ",", "’", "?", "!"]
# let's clean the string a little bit:
my_paragraph = my_paragraph.replace("\n", " ").lower()

for char in delete_chars:
    my_paragraph = my_paragraph.replace(char,"")


# spolit paragraph into words
words = my_paragraph.split(" ")
print(words)
# get unique characters
unique_words = set(words)

# create a variable to store the word frequencies
word_frequencies = {}


total_loops = 0

for word in unique_words:
    total_loops += 1
    if word != " ":
        word_frequencies[word] = words.count(word)

print(word_frequencies)