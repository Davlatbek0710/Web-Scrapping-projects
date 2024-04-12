import requests
from bs4 import BeautifulSoup
import html
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
result = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(result.text, "html.parser")
all_tags = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_names = [x.getText() for x in all_tags]

with open("movies.txt", "w", encoding="UTF-8") as file:
    for name in movie_names[::-1]:
        file.write(f"{name}\n")



