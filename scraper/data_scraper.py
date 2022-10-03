from newspaper import Article
from bs4 import BeautifulSoup
import requests

url = 'http://timesofindia.indiatimes.com/world/china/chinese-expert-warns-of-troops-entering-kashmir/articleshow/59516912.cms'

article = Article(url, language='en')
reqResult = requests.get(url)
cover = reqResult.content

s = BeautifulSoup(cover,'html5lib')

article.download()
article.parse()

print(s)