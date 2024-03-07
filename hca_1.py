import os, nltk

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from scipy.cluster.hierarchy import linkage, dendrogram

import matplotlib.pyplot as plt


ignore_files = [".DS_Store"]

titles = []
texts = []

for root, dirs, files in os.walk('analects'):
    files = [f for f in files if f not in ignore_files]

    for f in files:
        with open(os.path.join(root, f), 'r', encoding='utf8') as rf:
            text = rf.read()

        texts.append(text)
        titles.append(f[:-4])

vectorizer = CountVectorizer(max_features=100)
counts = vectorizer.fit_transform(texts)

distances = euclidean_distances(counts)
linkages = linkage(distances, 'ward')

dendrogram(linkages, labels=titles, orientation='right', leaf_font_size=8, leaf_rotation=45)

plt.show()