import nltk
from nltk.stem.snowball import SnowballStemmer

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

# we creat a stemmer object
stemmer = SnowballStemmer("english")

stemmed_words = []
for word in filtered_words:
    stemmed_words.append(stemmer.stem(word))

print(stemmed_words[100:150])

lemmatizer = nltk.WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(word) for word in filtered_words]

print(lemmas[100:150])