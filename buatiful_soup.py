from bs4 import BeautifulSoup
import requests

result = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(result.text,"html.parser")


# 1. find all names of news
# 2. all links
# 3. article upvote

# print(soup.find(name="tr", class_="athing"))
# titles = soup.select(selector="span.titleline a")
article_titles = [t.getText() for t in soup.find_all(name="span", class_="titleline")]
article_links = [x.a.get('href') for x in soup.find_all(name="span", class_="titleline")]
article_points = [y.getText().split()[0] for y in soup.find_all(name="span", class_="score")]

max_point = max(article_points)
pos = article_points.index(max_point)
print(max_point, pos)
print(article_titles[pos])
print(article_links[pos])
print(max_point, "points")







# for i in range(len(article_titles)):
#     print(f"{i + 1}. {article_titles[i].getText()} \n"
#           f"{article_titles[i].a.get(key='href')}")























# with open("website.html") as data:
#     contents = data.read()

#
# soup = BeautifulSoup(contents, "html.parser")


# print(soup.prettify())

# to get all anchor tags
# lst = soup.find_all("a")
# [print(x.string) for x in lst]

# dict_for_all_anchors = {item.getText():item.get("href") for item in lst}


# heading = soup.find(name="h3",  class_="heading")

# p = soup.select_one(selector="p em a")
# print(p)

# h3 = soup.select(selector=".heading")

#
# input = soup.find("input")
# print(input.get("maxlength"))


