import os

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from scipy.cluster.hierarchy import linkage, dendrogram

import matplotlib.pyplot as plt
import jieba

def tokenize_chinese(input):
    return jieba.cut(input)

ignore_files = [".DS_Store"]

titles = []
texts = []

for root, dirs, files in os.walk('corpus'):
    files = [f for f in files if f not in ignore_files]

    for f in files:
        with open(os.path.join(root, f), 'r', encoding='utf8') as rf:
            text = rf.read()

        texts.append(text)
        titles.append(f[:-4])


'''
Useful options for count vectorizer
max_features = 1000
vocabulary = ["he", "him", "his", "her", "she", "hers", "they", "them", "theirs"]
ngram_range = (1, 3)
tokenizer = customfunction
analyzer = "char" or "word"
'''

# vectorizer = CountVectorizer()

vectorizer = TfidfVectorizer(use_idf=False)

frequencies = vectorizer.fit_transform(texts)


# distances = euclidean_distances(frequencies)
similarties = cosine_similarity(frequencies)

print(similarties)
linkages = linkage(similarties, 'ward')

dendrogram(linkages, labels=titles, orientation='right', leaf_font_size=8, leaf_rotation=45)

plt.show()