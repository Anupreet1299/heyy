



import requests
from bs4 import BeautifulSoup # External Library for Parsing HTML Data

url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

tags = soup.find_all("td", class_="ratingColumn imdbRating")

ratings = []

for tag in tags:
    # print(tag.text)
    # print("------")

    data = tag.text
    ratings.append(data.strip())


for rate in ratings:
    print(rate)
    print("*******")


print("===========================================")

soup2 = BeautifulSoup(response.text, "html.parser")
tags = soup.find_all("td", class_="titleColumn")

movies = []


for tag in tags:
    # print(tag.text)
    # print("------")

    data = tag.text
    movies.append(data.strip())


for movie in movies:
    print(movie)