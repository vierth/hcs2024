# to extract data from html we can use beautiful soup
from bs4 import BeautifulSoup


# save pages to fetch in list
sites = ["United_States_Attorney_for_the_Southern_District_of_New_York", "John_Holland_Group", "Keane_Gilford"]

for site in sites:
    # put url in variable
    with open(site+'.html', 'r', encoding='utf8') as rf:
        html = rf.read()
        soup = BeautifulSoup(html, "lxml")
    
    links = soup.find_all("a")
    for link in links:
        info = link.string
        link_url = link.get("href")
        # print(info, link_url)

    lists = soup.find_all("ul")
    # for html_list in lists:
    #     print(html_list.text)
    print(soup.getText())
    # print(soup.prettify())