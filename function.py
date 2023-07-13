import requests
from bs4 import BeautifulSoup
import voice
import config


def news(text):
    for i in config.list_news:
        if i == text:
            url = 'https://mignews.com/mobile'
            page = requests.get(url)
            filteredNews = []
            soup = BeautifulSoup(page.text, "html.parser")
            allNews = soup.findAll('div', class_='text-color-dark')
            for data in allNews:
                if data.find('a') is not None:
                    filteredNews.append(data.text)
            sts = []
            site = []
            for data in filteredNews:
                sts.append(data)
            html = BeautifulSoup(page.content, 'html.parser')
            for index, el in enumerate(html.select('.text-color-dark')):
                if index == 5:
                    break
                url_more = el.select_one('a').get('href')
                site.append(url_more)
            for rw, ew in zip(sts, site):
                print(f"{rw}https://mignews.com{ew}")
                voice.va_speak(rw)
