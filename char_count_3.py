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

# create a variable to store the most common character
most_common_character = []

# create a second variable to track how often character occurs
mcc_frequency = 0


for character in my_paragraph:
    if character != " ":
        frequency = my_paragraph.count(character)

        # check if frequency i sgreater than the mcc_frequency
        # if it is, set most common character and mcc_frequency
        if frequency > mcc_frequency:
            most_common_character = [character]
            mcc_frequency = frequency

        elif frequency == mcc_frequency and character not in most_common_character:
            most_common_character.append(character)


print(f"The most common character(s) are {', '.join(most_common_character)}, which occur {mcc_frequency} times!")