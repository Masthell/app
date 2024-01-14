#  парсер сайтов
import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/?page=1"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
for item in data:
    print(item.text)