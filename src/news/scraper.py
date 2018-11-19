import requests
from bs4 import BeautifulSoup

def scrapeTXT(url, limit):
    
    newsTxt = ''
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    articles = soup.find_all('article')

    for article in articles[0:limit]:
        title = article.find('h2').get_text()
        content = article.find('div', class_="inner").find('p').get_text()
        
        newsTxt = newsTxt + title + content
        
    return newsTxt