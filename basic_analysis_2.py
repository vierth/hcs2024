import nltk

# we need a text to analyze
with open('analects.txt', 'r', encoding='utf8') as rf:
    analects = rf.read()

# Cut off the project gutenberg boilerplate
start_string = "*** START OF THE PROJECT"
end_string = "*** END OF THE PROJECT GUTENBERG EBOOK"
analects = analects[analects.find(start_string):analects.find(end_string)]    

# do our additional cleaning here
analects = analects.replace("\n", " ")

# break text into a tokenized form where outside lists are sentences and inside lists are words

# create a container for the sentences
# [["this", "is", "sentence"],["this", "is", "sentence"]]
sentences_words_tokenized = []

# looping through each sentence in the text
for sentence in nltk.sent_tokenize(analects):
    words = nltk.word_tokenize(sentence)
    sentences_words_tokenized.append(words)

# we can do this with a list comprehension
sentences_words_tokenized = [nltk.word_tokenize(sentence) for sentence in nltk.sent_tokenize(analects)]

print(sentences_words_tokenized[1000])