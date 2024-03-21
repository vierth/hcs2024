import gensim, nltk, os
import logging
import pandas as pd
import plotly.express as px


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def chunkify(text, length):
    chunks = []
    tokenized_text = text.split(" ")
    loops = len(tokenized_text)//length
    for i in range(0, loops):
        chunks.append(" ".join(tokenized_text[i*length:(i+1)*length]))
    return chunks

def plot_topic(topic_number, lda_model, topn=20):
    topic_data = {"words":[], "weights":[]}

    for word, weight in lda_model.show_topic(topic_number, topn=topn):
        topic_data["words"].append(word)
        topic_data["weights"].append(weight)

    df = pd.DataFrame(topic_data)
    fig = px.bar(df, x="words", y="weights")
    fig.show()

def plot_document_topic_distribution(doc_num, processed_corpus, lda_model):
    doc_lda = lda_model.get_document_topics(
        processed_corpus[doc_num], minimum_probability=0.0
    )

    doc_data = {"topic_num": [d[0] for d in doc_lda], 
                "topic_weight":[d[1] for d in doc_lda]}
    
    df = pd.DataFrame(doc_data)
    fig = px.bar(df, x="topic_num", y="topic_weight")
    fig.show()


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
    tokenized = nltk.word_tokenize(chunk)
    refined = [lemmatizer.lemmatize(word).lower() for word in tokenized if word.isalnum()]
    refined_texts.append(refined)

corpus_dictionary = gensim.corpora.Dictionary(refined_texts)



# no below number of documents (integer)
# no above number of documents (float from 0 to 1) in percent
corpus_dictionary.filter_extremes(no_below=2, no_above=.9)

# prep corpus for gensim
processed_corpus = [corpus_dictionary.doc2bow(text) for text in refined_texts]

lda = gensim.models.ldamodel.LdaModel(processed_corpus, num_topics=10, id2word=corpus_dictionary,iterations=500, passes=50)

topics = lda.show_topics()
for topic in topics:
    print(topic)

plot_topic(3, lda, topn=30)
plot_document_topic_distribution(10, processed_corpus, lda)