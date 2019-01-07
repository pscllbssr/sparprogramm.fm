# -*- coding: utf-8 -*-
url = "https://www.digezz.ch/wp-admin/admin-ajax.php"
baseUrl = "https://www.digezz.ch"
text = "Wir unterbrechen die Musik nun für eine wichtige Durchsage. Der im Moment beliebteste Artikel auf der Studierendenplattform Digezz trägt den Namen {} und wurde produziert {}."
text = text + " Du hörst Sparprogramm.fm und nun geht es weiter mit erstklassiger Musik."

def getMostPopularArticle():
    
    import requests
    
    article = {}
    
    params = {
        'action': 'ajax-front-page-lists',
        'type': 3,
        'pageNum': 1,
        'postTotal': 1
    }
    response = requests.post(url, data=params)
    
    json_string = response.json()
    article['title'] = json_string[0]['previewText'].encode('utf-8')
    article['url'] = baseUrl + json_string[0]['permalink']
    
    from bs4 import BeautifulSoup
    
    response = requests.get(article['url'])
    soup = BeautifulSoup(response.content, 'html.parser')
    article['author'] = soup.find('div', class_="entry-author").get_text(" ", strip=True).encode('utf-8')
    
    return text.format(article['title'], article['author'])
    
if __name__ == "__main__":
    print getMostPopularArticle()