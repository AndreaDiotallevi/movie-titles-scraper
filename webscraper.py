from bs4 import BeautifulSoup
import requests

url = "http://istanbulfilms.blogspot.com/2010/05/top-films-from-guinea-1.html"
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

print (content)
