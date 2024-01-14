#import bibliotek
import requests
from bs4 import BeautifulSoup
#import fake_useragent
#user = fake_useragent.UserAgent().random
header = {"user agent": "ghjghjgh"}


#get data
url = "https://browser-info.ru/"
response = requests.get(url, headers=header ).text

#"get" данные получают "post" отправляют
#find data
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id='tool_padding')

#check js
check_js = block.find('div', id='javascript_check').text
result_js = check_js.find.all('span')[1].text
result_js = f'javascript: {result_js}'

#check flash
check_flash = block.find('div', id='flash_check').text
check_js = check_js.find.all('span')[1].text
check_js = f'flash: {check_js}'

#check user agent
check_user_agent = block.find('div', id='user agent').text
#check_user_agent = check_user_agent.find.all('span')[1].text
check_user_agent = f'user-agent: {check_user_agent}'

print(response)

"""""
soup = BeautifulSoup(response.text, "lxml")
data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
name = data.find("h4", class_="card-title").text.replace("\n", "")
price = data.find("h5").text
url.img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")
print(name + "\n" + price + "\n" + url)
""""""