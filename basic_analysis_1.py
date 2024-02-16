import nltk, jieba


# we need a text to analyze
with open('analects.txt', 'r', encoding='utf8') as rf:
    analects = rf.read()

# Cut off the project gutenberg boilerplate
start_string = "*** START OF THE PROJECT"
end_string = "*** END OF THE PROJECT GUTENBERG EBOOK"
analects = analects[analects.find(start_string):analects.find(end_string)]    

# do our additional cleaning here
analects = analects.replace("\n", " ")


# NLTK comes with tools that help us tokenize the text
# sentence tokenizer
sentences = nltk.sent_tokenize(analects)
print(sentences[1000:1010])

# NLTK also comes with a word tokenizer that is more sophisticated than spaces
words = nltk.word_tokenize(analects)
print(words[1000:1010])

# tokenization in Chinese requires other libraries
print(list(jieba.cut("我的名字叫李友仁")))