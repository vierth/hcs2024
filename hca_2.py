import os

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from scipy.cluster.hierarchy import linkage, dendrogram

import matplotlib.pyplot as plt
import jieba

def tokenize_chinese(input):
    return jieba.cut(input)

color_dict = {"doyle":"magenta", "collins":"blue"}

ignore_files = [".DS_Store"]

titles = []
authors = []
texts = []

title_to_author = {}

for root, dirs, files in os.walk('corpus'):
    files = [f for f in files if f not in ignore_files]

    for f in files:
        with open(os.path.join(root, f), 'r', encoding='utf8') as rf:
            text = rf.read()

        file_info = f[:-4].split("_")
        author = file_info[0]
        title = file_info[1]

        title_to_author[title] = author

        texts.append(text)
        authors.append(author)
        titles.append(title)


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

ax = plt.gca()
labels = ax.get_ymajorticklabels()
print(labels)

for label in labels:
    label.set_color(color_dict[title_to_author[label.get_text()]])

plt.show()