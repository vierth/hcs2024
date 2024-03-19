import os

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from scipy.cluster.hierarchy import linkage, dendrogram

from sklearn.decomposition import PCA

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

ignore_files = [".DS_Store"]

titles = []
authors = []
texts = []


for root, dirs, files in os.walk('corpus'):
    files = [f for f in files if f not in ignore_files]

    for f in files:
        with open(os.path.join(root, f), 'r', encoding='utf8') as rf:
            text = rf.read()

        file_info = f[:-4].split("_")
        author = file_info[0]
        title = file_info[1]
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

vectorizer = TfidfVectorizer(use_idf=False, vocabulary = ["he", "him", "his", "her", "hers", "she","them", "they","theirs"])

frequencies = vectorizer.fit_transform(texts)

pca = PCA(n_components=2)

my_pca = pca.fit_transform(frequencies.toarray())
frequencies.toarray().shape
print(frequencies.toarray().shape, my_pca.shape)

print(my_pca)
pc1 = my_pca[:,0]
pc2 = my_pca[:,1]
print(pc1)
print(pc2)

data = {"authors":authors, "pc1": pc1, "pc2": pc2, "titles":titles}

df = pd.DataFrame(data)

sns.scatterplot(df, x='pc1', y='pc2', hue='authors')


plt.show()