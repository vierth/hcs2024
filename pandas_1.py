import pandas as pd
from pandas import Series
import nltk

number_list = [1,2,3,4,5]

my_series = Series(number_list)

with open('analects.txt','r',encoding='utf8') as rf:
    text=rf.read()

words = nltk.word_tokenize(text)

word_series = Series(words)

word_counts = word_series.value_counts()
# print(word_counts)
# print(word_counts.index)
print(word_counts['humanity'])
print(word_counts[0])

print(word_counts.get('humanity'))

print(word_counts * 2)
print(word_counts + word_counts)