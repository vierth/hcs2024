import time

"""This script will calculate the most common 
character in a paragraph"""

my_paragraph = """In the year 1878 I took my degree of Doctor of Medicine of the
University of London, and proceeded to Netley to go through the course
prescribed for surgeons in the army. Having completed my studies there,
I was duly attached to the Fifth Northumberland Fusiliers as Assistant
Surgeon. The regiment was stationed in India at the time, and before I
could join it, the second Afghan war had broken out. On landing at
Bombay, I learned that my corps had advanced through the passes, and
was already deep in the enemy’s country. I followed, however, with many
other officers who were in the same situation as myself, and succeeded
in reaching Candahar in safety, where I found my regiment, and at once
entered upon my new dutiesaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa."""

# let's clean the string a little bit:
my_paragraph = my_paragraph.replace("\n", " ").lower()

# spolit paragraph into words
words = my_paragraph.split(" ")
print(words)
# get unique characters
unique_words = set(words)

# create a variable to store the most common character
most_common_word = []

# create a second variable to track how often character occurs
mcw_frequency = 0

total_loops = 0

for word in unique_words:
    total_loops += 1
    if word != " ":
        frequency = my_paragraph.count(word)

        # check if frequency i sgreater than the mcc_frequency
        # if it is, set most common character and mcc_frequency
        if frequency > mcw_frequency:
            most_common_word = [word]
            mcw_frequency = frequency

        elif frequency == mcw_frequency and word not in most_common_word:
            most_common_word.append(word)

print(f"The most common word(s) are {', '.join(most_common_word)}, which occur {mcw_frequency} times!")