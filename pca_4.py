import os

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.decomposition import PCA

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import plotly.express as px
import plotly.graph_objs as go


def chunkify(text, length):
    chunks = []

    # split into words
    tokenized_text = text.split(" ")

    # calculate number of loops
    loops = len(tokenized_text)//length

    # split into loop number of chunks
    for i in range(0, loops):

        # loop 1 [0*length to 1*legnth]
        # loop 2 [1*length to 2*length]
        chunks.append(" ".join(tokenized_text[i*length:(i+1)*length]))
    return chunks



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

        chunks = chunkify(text, 1000)

        for chunk in chunks:
            texts.append(chunk)
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

vectorizer = TfidfVectorizer(use_idf=False, max_features=100)

frequencies = vectorizer.fit_transform(texts)

pca = PCA(n_components=2)

my_pca = pca.fit_transform(frequencies.toarray())
frequencies.toarray().shape
# print(frequencies.toarray().shape, my_pca.shape)

# print(my_pca)
pc1 = my_pca[:,0]
pc2 = my_pca[:,1]
# print(pc1)
# print(pc2)

loadings = pca.components_
vocabulary = vectorizer.get_feature_names_out()

print(vocabulary)

# need a dictionary that contains the vocabulary, the x position and the y position

loadings_data = {"vocab":[], "x":[], "y":[]}

for i, vocab in enumerate(vocabulary):
    loadings_data["vocab"].append(vocab)
    loadings_data["x"].append(loadings[0,i])
    loadings_data["y"].append(loadings[1,i])

loadings_df = pd.DataFrame(loadings_data)


data = {"authors":authors, "pc1": pc1, "pc2": pc2, "titles":titles}

df = pd.DataFrame(data)

fig = px.scatter(df, x='pc1', y='pc2', color='authors')

# fig.add_trace(go.Scatter(x=data["Time"], y=data["OD"], mode='markers', marker=dict(color=data["C-source"], size=data["C:A 1 ratio"])))
fig.add_trace(go.Scatter(x=loadings_df["x"], y=loadings_data["y"], mode="text", 
                         text=loadings_df["vocab"]))


fig.write_html('res.html')