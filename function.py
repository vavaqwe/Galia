import asyncio
import datetime
import os
import re
import webbrowser
from ctypes import cast, POINTER

import pyautogui as pg
import pyowm
import requests
from bs4 import BeautifulSoup
from comtypes import CLSCTX_ALL
from num2words import num2words
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from pyvolume import pyvolume
from pywhatkit import search
from words2numsrus import NumberExtractor

import config
import main
import voice

extractor = NumberExtractor()

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
        if i in text:
            now = datetime.datetime.now()
            text = "Сейч+ас " + num2words(now.hour, lang='ru') + " " + num2words(now.minute, lang='ru')
            voice.va_speak(text)
            print(text)

# def game(text):
#     for text1 in speak.listen():
#         print(text1)

def weather_with_city(text):
    words = text.split()
    last_word = words[-1]
    try:
        observation = config.mgr.weather_at_place(last_word)
        w = observation.weather_with_сity
        temp = w.temperature('celsius')["temp"]
        voice.va_speak('Температура ' + 'в' + last_word + '  ' + num2words(temp, lang='ru') + ' градусов')
        print('Температура ' + 'в' + last_word + '  ' + num2words(temp, lang='ru') + ' градусов')
    except pyowm.commons.exceptions.NotFoundError:
        voice.va_speak("Извините я не поняла, впишите ещё раз город в котором вы хотите узнать погоду")
        weather()

def check_weather_commands(text):
    for command in config.list_weather:
        if command in text:
            if 'погода' in text and 'погоду' in text:
                weather()
            if "в городе" in text:
                weather_with_city(text)

def weather():
    try:
        city = main.show_input_dialog()
        observation = config.mgr.weather_at_place(city)
        w = observation.weather
        temp = w.temperature('celsius')["temp"]
        voice.va_speak('Температура ' + 'в ' + city + '  ' + num2words(temp, lang='ru') + ' градусов')
        print('Температура ' + 'в ' + city + '  ' + num2words(temp, lang='ru') + ' градусов')
    except pyowm.commons.exceptions.NotFoundError:
        voice.va_speak("Извините я не поняла, напишите ещё раз")
        weather()

def internet(text):
    for i in config.list_search:
        if i in text:
            b = text.strip(str(i))
            webbrowser.open_new_tab('https://www.google.com/search?q=' + b)

    if 'нажми' in text.lower() or 'нажать' in text.lower():
        pg.click()

    if 'поищи' in text.lower or 'найди' in text.lower():
        search(str(text))

    for i in config.list_browser:
        if i in text:
            voice.va_speak("Включаю браузер")
            webbrowser.open_new_tab('https://www.google.com')

def music(text):
    for i in config.list_write:
        if i in text:
            print(text)

def get_volume():
    # Получение объекта интерфейса IAudioEndpointVolume
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Получение текущей громкости в процентах
    volume_scalar = volume.GetMasterVolumeLevelScalar()
    return int(volume_scalar * 100)


def check_sound_commands(text):
    for i in config.list_sound:
        if i in text:
            if 'на максимум' in text and 'на всю' in text:
                pyvolume(level=100)

            elif "громче" in text and "на" in text:
                replayed = extractor.replace_groups(text)
                words = replayed.split()
                num = 0
                for i in words:
                    if i.isdigit():
                        num = int(i)  # Преобразуем строку в целое число
                        if num > 100:
                            voice.va_speak("Вы сказали громкость больше 100")
                        break
                current_value = get_volume()
                pyvolume(level=current_value+num)

            elif "тише" in text and "на" in text:
                replayed = extractor.replace_groups(text)
                words = replayed.split()
                num = 0
                for i in words:
                    if i.isdigit():
                        num = int(i)
                        if num > 100:
                            voice.va_speak("Вы сказали громкость больше 100")
                        break
                current_value = get_volume()
                pyvolume(level=current_value-num)
            elif "на " in text:
                replayed = extractor.replace_groups(text)
                words = replayed.split()

                num = 0
                for i in words:
                    if i.isdigit():
                        num = int(i)  # Преобразуем строку в целое число
                        if num > 100:
                            voice.va_speak("Вы сказали громкость больше 100")
                        break
                pyvolume(level=num)
            elif 'громче' in text:
                pyvolume(level=get_volume()+10)

            elif 'потише' in text or 'тише' in text:
                pyvolume(level=get_volume()-10)

        elif 'выключи звук' in text:
            pyvolume(level=0)

def find_numbers_in_string(text):
    return re.findall(r'\d+', text)

# короче надо 1. json file 2. ко всем запросам сделать свои ответы
def reminder(text):
    for i in config.list_reminder:
        if i in text:
            if 'через' in text:
                replayed = extractor.replace_groups(text)
                words = replayed.split()
                now = datetime.datetime.now()
                print(words)
                if 'час' in words:
                    hour_ago = now + datetime.timedelta(hours=1)
                    asyncio.run(rem(hour_ago))

                elif 'полтора' in words and 'часа' in words:
                    hour_ago = now + datetime.timedelta(minutes=90)
                    asyncio.run(rem(hour_ago))

                elif ('часа' in words and 'минут' in words ) or ( 'часов' in words and 'минут' in words ) \
                        or ('час' in words and 'минут' in words ) :
                    time = find_numbers_in_string(replayed)
                    num1 = int(time[0])
                    num2 = int(time[1]) if len(time) > 1 else 1
                    hour_ago = now + datetime.timedelta(hours=num1,minutes=num2)
                    asyncio.run(rem(hour_ago))

                elif 'часа' in words or 'часов' in words :
                    time = find_numbers_in_string(replayed)
                    num1 = int(time[0])
                    hour_ago = now + datetime.timedelta(hours=num1)
                    asyncio.run(rem(hour_ago))

                elif ('минут' in words and 'секунд' in words) or ('минуту' in words and 'секунд' in words):
                    time = find_numbers_in_string(replayed)
                    num1 = int(time[0])
                    num2 = int(time[1]) if len(time) > 1 else 1
                    print(num1,num2)
                    minute_ago = now + datetime.timedelta(minutes=num1,seconds=num2)
                    asyncio.run(rem(minute_ago))

                elif 'минуту' in words:
                    minute_ago = now + datetime.timedelta(minutes=1)
                    asyncio.run(rem(minute_ago))

                elif 'минут' in words:
                    time = find_numbers_in_string(replayed)
                    num = int(time[0])
                    minute_ago = now + datetime.timedelta(minutes=num)
                    asyncio.run(rem(minute_ago))

                elif 'секунду' in words:
                    second_ago = now + datetime.timedelta(seconds=1)
                    asyncio.run(rem(second_ago))

                elif 'секунд' in words or 'секунды 'in words:
                    time = find_numbers_in_string(replayed)
                    num = int(time[0])
                    second_ago = now + datetime.timedelta(seconds=num)
                    asyncio.run(rem(second_ago))


            if 'в' in text:
                print("kk")


async def rem(time):
    while True:
        now = datetime.datetime.now()
        if time == now:
            voice.va_speak("сделать")
            break