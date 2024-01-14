import requests
from bs4 import BeautifulSoup

session = requests.session()
url = "https://ruforum.mybb.ru/login.php?action=in"
user = fake_useragent.UserAgent().random

header = {
    "user-agent": user
}

data = {
    "username": "admin",
    "password": "admin",
}

respone = requests.post(url, headers=header, data=data)
profil_info = "https://ruforum.mybb.ru/profile.php"
profile_respone = requests.get(profil_info)

cookie_dict = session.cookies.get_dict()

session2 = requests.session()

requests.get(profil_info, cookies=cookie_dict)

#session
#autorization
#get/set cookies
#https://ruforum.mybb.ru/
#lession test:oA9h768p