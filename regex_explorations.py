# import libaries
import re

with open('analects.txt', 'r', encoding='utf8') as rf:
    text = rf.read()
text = text[:text.find("*** END OF THE PROJECT ")]


chapter_info = []

book_divs = re.split(r"(BOOK [IVX]+\. .+)", text)
book_divs = book_divs[1:]
# print(book_divs)
for i, book in enumerate(book_divs):
    if i % 2 == 0:
        book_title = book
        
        book_content = book_divs[i+1]
        # print(book_title, book_content)

        chapter_divs = re.split(r'((?:CHAPTER|CHAP\.) [IVXL]+)', book_content)
        # print(chapter_divs[0])
        # with no caputre groups, the matched value is deleted and you get
        # res = [text, text, text, text]

        # with capture groups you also get the matched value back
        # res = [text, match, text, match, text, match, text]

        
        chapter_divs = chapter_divs[1:]
        for j, chapter in enumerate(chapter_divs):
            if j % 2 == 0:
                chapter_title = chapter
                chapter_len = len(chapter_divs[j+1])
                chapter_info.append("\t".join([book_title, chapter_title, str(chapter_len)]))

with open('chapter_res.tsv','w',encoding='utf8') as wf:
    wf.write("BookTitle\tChapterTitle\tLength\n")
    wf.write("\n".join(chapter_info))


