import datetime
import os
import sys
import webbrowser

from pywhatkit import search
from pyvolume import pyvolume

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import pyautogui as pg

from words2numsrus import NumberExtractor
import pyowm
import requests
from bs4 import BeautifulSoup

from num2words import num2words
import config
import main
import speak
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
    if 'выход' in text.lower() or 'выключись' in text.lower():
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
    if last_word == "стоп" or last_word == "нужно":
        return
    try:
        if last_word:
            observation = config.mgr.weather_at_place(last_word.strip())
            w = observation.weather_with_сity
            temp = w.temperature('celsius')["temp"]
            voice.va_speak('Температура ' + 'в' + last_word + '  ' + num2words(temp, lang='ru') + ' градусов')
            print('Температура ' + 'в' + last_word + '  ' + num2words(temp, lang='ru') + ' градусов')
    except pyowm.commons.exceptions.NotFoundError:
        voice.va_speak("Извините я не поняла, скажите ещё раз город в котором вы хотите узнать погоду")
        weather_with_city(speak.listen())

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

# def write(text):
#     for i in config.list_write:
#         if i in text:
#             text

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

            if "громче" in text and "на" in text:
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
            elif "громче" in text:
                pyvolume(level=get_volume()+10)

            elif "потише" in text:
                pyvolume(level=get_volume()-10)

            elif "выключи звук" in text:
                pyvolume(level=0)