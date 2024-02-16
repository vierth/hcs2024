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
analects = analects.replace("\n", " ").lower()

words = nltk.word_tokenize(analects)

filtered_words = []
for word in words:
    if word.isalnum():
        filtered_words.append(word)

filtered_words = [word for word in words if word.isalnum()]

# print lexical diversity
print(len(set(filtered_words))/len(filtered_words))

