import gensim, nltk, os
import logging

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
    tokenized = nltk.word_tokenize(chunk)
    refined = [lemmatizer.lemmatize(word).lower() for word in tokenized if word.isalnum()]
    refined_texts.append(refined)

corpus_dictionary = gensim.corpora.Dictionary(refined_texts)

# no below number of documents (integer)
# no above number of documents (float from 0 to 1) in percent
corpus_dictionary.filter_extremes(no_below=5, no_above=.7)

# prep corpus for gensim
processed_corpus = [corpus_dictionary.doc2bow(text) for text in refined_texts]

lda = gensim.models.ldamodel.LdaModel(processed_corpus, num_topics=10, id2word=corpus_dictionary,
                                    iterations=500, passes=50)

topics = lda.show_topics()
for topic in topics:
    print(topic)