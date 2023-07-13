import datetime
import os
import sys
# import time
# import webbrowser
#
# import pyautogui as pg
# import pyowm
import requests
from bs4 import BeautifulSoup

from num2words import num2words
import config
# import main
# import speak
import voice


def news(text):
    for i in config.list_news:
        if i == text:
            url = 'https://mignews.com/mobile'
            page = requests.get(url)
            filtered_news = []
            soup = BeautifulSoup(page.text, "html.parser")
            all_news = soup.findAll('div', class_='text-color-dark')
            for data in all_news:
                if data.find('a') is not None:
                    filtered_news.append(data.text)
            sts = []
            site = []
            for data in filtered_news:
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

def off(text):
    if ' выход' in text.lower() or ' выключись' in text.lower():
        voice.va_speak("Выключаюсь")
        sys.exit(1)

    if ' выключи компьютер' in text:
        voice.va_speak("Выключаю подождите")
        os.system("shutdown -s")
        quit()

    if ' перезапусти компьютер' in text:
        voice.va_speak("Перезапускаю подождите 10 секунд")
        os.system("shutdown /r /t 10")
        quit()

def ua(text):
    if ' слава украине' in text.lower():
        print("Героям Слава")
        voice.va_speak("Героям Слава")

def time_now(text):
    for i in config.list_time:
        if i == text:
            now = datetime.datetime.now()
            text = "Сейч+ас " + num2words(now.hour, lang='ru') + " " + num2words(now.minute, lang='ru')
            voice.va_speak(text)
            print(text)
