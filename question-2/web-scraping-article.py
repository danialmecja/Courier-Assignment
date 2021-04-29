# Importing packages dam u r geh goddam u r geh fahad omg
import requests
from bs4 import BeautifulSoup

URL = "https://www.nst.com.my/news/nation/2020/12/648176/pos-malaysia-international-mail-parcel-deliveries-still-suspended"
page = requests.get(URL)



r1 = requests.get(URL)
coverpage = r1.content

soup1 = BeautifulSoup(coverpage, "html5lib")

# coverpage_news = soup1.find_all('p', id='story-body')

coverpage_news= soup1.find('p',class_='article-content')

print(coverpage_news)













