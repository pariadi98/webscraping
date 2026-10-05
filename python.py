from bs4 import BeautifulSoup
import requests
 
url = 'https://www.python.org/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
latest_news = soup.find('div', attrs={'class':'medium-widget blog-widget'})
'''
#print(len(latest_news))
#print(latest_news)

titles = latest_news.find_all('a')
#print(titles)
timtes = latest_news.find_all('time')

for item in titles:
    print(item.get_text())
    print(item.get('href'))
    print('-' * 30)

for item in timtes:
    print(item.get_text())
    print('-' * 30)

latest_news2 = soup.find('div', attrs={'class':'medium-widget event-widget last'})

titles2 = latest_news2.find_all('a')
times2 = latest_news2.find_all('time')

for item in titles2:
    print(item.get_text())
    print(item.get('href'))
    print('-' * 30)

for item in times2:
    print(item.get_text())
    print('-' * 30)


latest_news3 = soup.select('div.medium-widget.event-widget.last ul.menu li a')
print(latest_news3)

for item in latest_news3:
    print(item.get_text())
'''
