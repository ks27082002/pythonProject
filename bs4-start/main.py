from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website = response.text
soup = BeautifulSoup(website, "html.parser")
movies = soup.find_all(name="h3", class_="title")
names = []
for movie in movies:
    names.append(movie.get_text())
names.reverse()
print(names)
with open("movie.txt", mode="w") as file:
    for movie in names:
        file.write(f"{str(movie)}\n")




















# response = requests.get("https://news.ycombinator.com/news")
#
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
#
# articles = soup.find_all(name="a", rel="noreferrer")
# texts, links = [], []
# for article in articles:
#     texts.append(article.get_text())
#     links.append(article.get("href"))
#
# upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]
# max_up = max(upvotes)
# max_ind = upvotes.index(max_up)
# print(texts[max_ind])
# print(links[max_ind])






























#
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.string)
# all_Anchor_tags = soup.find_all(name="a")
# # for tag in all_Anchor_tags:
# #     print(tag.get_text())
# #     print(tag.get("href"))
#
# # print(soup.find(name="h1", id="name").get("class"))
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)












