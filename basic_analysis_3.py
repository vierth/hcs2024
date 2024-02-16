import nltk
from matplotlib import pyplot as plt

# we need a text to analyze
with open('analects.txt', 'r', encoding='utf8') as rf:
    analects = rf.read()

# Cut off the project gutenberg boilerplate
start_string = "*** START OF THE PROJECT"
end_string = "*** END OF THE PROJECT GUTENBERG EBOOK"
analects = analects[analects.find(start_string):analects.find(end_string)]    

# do our additional cleaning here
analects = analects.replace("\n", " ")

words = nltk.word_tokenize(analects)
print(words.count("Master"))
# creating an nltk text object
analects_object = nltk.Text(words)


# create a concordonce
# analects_object.concordance("rites", width=90, lines=50)

# look for similar words
# analects_object.similar("heaven")

# let's create a dispersion plot
analects_object.dispersion_plot(['rites', 'heaven', 'humanity', 'Master'])

plt.show()

analects_object.collocations()


# we can create a frequency distribution object with FreqDist
frequencies = nltk.FreqDist(analects_object)
print(frequencies['Master'])