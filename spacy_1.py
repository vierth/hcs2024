'''
to install spacy it is
pip install spacy

to download specific models you do this:

python -m spacy download en_core_web_sm
python -m spacy download zh_core_web_sm

md (medium)
lg (large)
trf (transformer model)


https://spacy.io/models

'''
import spacy
from spacy import displacy


nlp = spacy.load('en_core_web_sm')

with open('analects.txt', 'r', encoding='utf8') as rf:
    text = rf.read()

text = text[:5000]

document = nlp(text)

# get named entities
document.ents

# get sentences
for sentence in document.sents:
    pass
    # print(sentence)

for nc in document.noun_chunks:
    pass
    # print(nc)

for word in document:
    pass
    # print(word.text, word.pos_, word.dep_, word.lemma_)

print(spacy.explain('advmod'))

displacy.serve(document, style='ent', port=8080)