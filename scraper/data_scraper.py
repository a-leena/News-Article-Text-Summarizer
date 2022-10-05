from newspaper import Article
import requests

url = 'https://timesofindia.indiatimes.com/india/modi-govt-strengthened-probe-agencies-laws-as-part-of-zero-tolerance-policy-on-terrorism-amit-shah/articleshow/93820327.cms'

article = Article(url, language='en')

article.download()
article.parse()

print(article.text)