import re, os

with open('analects.txt', 'r', encoding='utf8') as rf:
    text = rf.read()

text = re.sub("\n", " ", text)
text = re.sub("\s+", " ", text)

chapters = re.split(r'CHAP\. [IVXL]+', text)

if not os.path.isdir('analects'):
    os.mkdir('analects')
chapters = chapters[1:]

for i, chapter in enumerate(chapters):
    with open(os.path.join('analects', f'{i}.txt'), "w",encoding='utf8') as wf:
        wf.write(chapter)