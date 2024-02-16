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

my_words = my_paragraph.lower().split(" ")
print(my_words)

unique_words = set(my_words)

print(unique_words)

# lexical diversity is simply a measure of the extent of vocabulary, and is
# calculated by deviding number of unique words by total mnumber of workds
lex_div = len(unique_words)/len(my_words)
print(lex_div)