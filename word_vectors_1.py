import gensim, nltk, os
import logging
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def chunkify(text, length):
    chunks = []
    tokenized_text = text.split(" ")
    loops = len(tokenized_text)//length
    for i in range(0, loops):
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

        text = text[text.find("*** START OF THE PROJECT GUTENBERG EBOOK"):text.find("*** END OF THE PROJECT GUTENBERG")]


        file_info = f[:-4].split("_")
        author = file_info[0]
        title = file_info[1]

        chunks = chunkify(text, 1000)

        for chunk in chunks:
            texts.append(chunk)
            authors.append(author)
            titles.append(title)


lemmatizer = nltk.WordNetLemmatizer()

refined_texts = []

for chunk in texts:
    sentences = nltk.sent_tokenize(chunk)
    for sent in sentences:
        tokenized = nltk.word_tokenize(sent)
        refined = [lemmatizer.lemmatize(word).lower() for word in tokenized if word.isalnum()]
        refined_texts.append(refined)

print(refined_texts[0])

vec_model = gensim.models.Word2Vec(sentences=refined_texts, vector_size=100, window=5, sg=0)

words = []
vecs = []

for word in vec_model.wv.index_to_key:
    words.append(word)
    vecs.append(vec_model.wv[word])
    
pca = PCA()

my_pca = pca.fit_transform(vecs)

data = {"words":words, "pc1":my_pca[:,0], 'pc2':my_pca[:,1]}
df = pd.DataFrame(data)

fig = px.scatter(df, x="pc1", y="pc2", text="words")
fig.show()