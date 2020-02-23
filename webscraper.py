from bs4 import BeautifulSoup
import requests

url = "http://istanbulfilms.blogspot.com/2010/05/top-films-from-guinea-1.html"
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

for li in content.findAll("li"):
  response = requests.get(li.find("a").get("href"), timeout=5)
  content = BeautifulSoup(response.content, "html.parser")
  div = content.find(name="div", attrs={"id":"main"})
  for i, b in enumerate(content.findAll("b")):
    if i == 0:
      country = b.text.split("FROM ")[-1].capitalize().encode("utf-8")
      print(country)
      movies = []
    elif (not b.find("a")) and (b.text.strip()):
      movies.append(b.text)
  print (movies)
