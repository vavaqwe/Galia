# C ТРЕЕМ
import sys
import threading
import tkinter as tk
from tkinter import simpledialog

import pystray
# from voice import va_speak
from PIL import Image

import config
import speak
from function import *


# def listen():
#     while True:
#         data = stream.read(4096, exception_on_overflow=False)
#         if (rec.AcceptWaveform(data)) and len(data) > 0:
#             answer = json.loads(rec.Result())
#             if answer['text']:
#                 on_startup(answer['text'])

# def listen():
#     activation = False
#     for text in speak.listen():
#         print(text)
#         words = ()
#         if not activation:
#             for key, value in config.responses["act"]:
#                 if key.lower() in text.lower():
#                     activation = True
#                     words = text.split()
#                     break
#
#         if activation:
#             new_string = ' '.join(words[1:])
#             print(new_string)
#             news(new_string)
#             off(new_string)
#             ua(new_string)
#             time_now(new_string)
#             check_weather_commands(new_string)
#             check_sound_commands(new_string)
#             # reminder(new_string)
#             get_response(new_string)
#             activation = off(new_string)
# def listen():
#     activate = False
#     for text in speak.listen():
#
#         if not activate:
#             for key, value in config.responses["act"]:
#                 if key in text.lower():
#                     activate = True
#                     words = text.split()
#                     words.remove(key)
#                     new_string = ' '.join(words[1:])
#                     get_response(new_string)
#                     news(new_string)
#                     off(new_string)
#                     ua(new_string)
#                     time_now(new_string)
#                     check_weather_commands(new_string)
#                     check_sound_commands(new_string)
#                     # reminder(new_string)
#                     activation = off(new_string)
#                     if activation:
#                         activate = False
#
#         if activate:
#             for key, value in config.responses["act"]:
#                 words = text.split()
#                 words.remove(key)
#                 new_string = ' '.join(words[1:])
#                 news(new_string)
#                 off(new_string)
#                 ua(new_string)
#                 time_now(new_string)
#                 check_weather_commands(new_string)
#                 check_sound_commands(new_string)
#                 # reminder(new_string)
#                 get_response(new_string)
#                 activation = off(new_string)
def listen():
    activate = False

    for text in speak.listen():
        print(text)
        message = ''
        if not activate:
            for key, value in config.responses["act"]:
                if key.lower() in text.lower():
                    activate = True
                    words = text.split()
                    if key in words:
                        words.remove(key)
                    message = ' '.join(words)
                    print("Активировано:", key)
                    break

        if activate:
            if message:
                if "выключись" in text.lower() or "отключись" in text.lower():
                    print("Отключение.")
                    activate = False
                    continue
                new_string = ''
                for key, value in config.responses["act"]:
                    if key.lower() in text.lower():
                        words = text.split()
                        if key in words:
                            words.remove(key)
                            new_string = ' '.join(words)

                news(new_string)
                off(new_string)
                ua(new_string)
                time_now(new_string)
                check_weather_commands(new_string)
                check_sound_commands(new_string)
                # reminder(new_string)
                get_response(new_string)
                activation = off(new_string)

                if activation:
                    activate = False






# def start(text,act):
#     # words = text.split()
#     # words.remove(key)
#     # new_string = ' '.join(words[1:])
#     words = text.split()
#     new_string = ' '.join(words[1:])
#     news(new_string)
#     off(new_string)
#     ua(new_string)
#     time_now(new_string)
#     check_weather_commands(new_string)
#     check_sound_commands(new_string)
#     # reminder(new_string)
#     get_response(new_string)
#     activation = off(new_string)
#     if activation:
#         return

# def listen():
#     for text in speak.listen():
#         for key , value in config.responses["act"]:
#             if key.lower() in text :
#                 print(key,value)
#                 words = text.split()
#                 words.remove(key)
#                 new_string = ' '.join(words[1:])
#                 print(new_string)
#                 news(new_string)
#                 off(new_string)
#                 ua(new_string)
#                 time_now(new_string)
#                 check_weather_commands(new_string)
#                 check_sound_commands(new_string)
#                 # reminder(new_string)
#                 get_response(new_string)
#                 activation = off(new_string)
#                 if activation:
#                     break

def start_listening():
    thread = threading.Thread(target=listen)
    thread.daemon = True
    thread.start()

# def on_startup(text: str):
#     print(text)
#     words = text.split()
#     first_word = words[0]
#     for i in config.act:
#         if first_word == i:
#             new_string = ' '.join(words[1:])
#             print(new_string)
#             news(new_string)
#             off(new_string)
#             ua(new_string)
#             time_now(new_string)
#             check_weather_commands(new_string)
#             check_sound_commands(new_string)
#             exit(new_string)

def on_exit():
    print("Приложение завершено")
    tray.stop()
    sys.exit(0)


def show_input_dialog():
    root = tk.Tk()
    root.withdraw()  # Скрыть основное окно tkinter

    # Отобразить диалоговое окно с вводом текста
    user_input = simpledialog.askstring("Input", "Введите город ")

    # Обработка введенного текста
    if user_input:
        print("Введенный текст:", user_input)
    return user_input


menu = (
    pystray.MenuItem('Input Text', show_input_dialog),
    pystray.MenuItem('Выход', on_exit)
)



if __name__ == "__main__":
    image = Image.open('ico/gpng.png')
    tray = pystray.Icon("name", image, "Заголовок", menu)
    start_listening()
    tray.run()




# С ИНТЕРФейСОМ
# from  speak import *
# from voice import va_speak
#
# import tkinter as tk
# import threading
#
#
#
# def listen():
#     while True:
#         data = stream.read(4096, exception_on_overflow=False)
#         if (rec.AcceptWaveform(data)) and len(data) > 0:
#             answer = json.loads(rec.Result())
#             if answer['text']:
#                 on_startup(answer['text'])
#
# def start_listening():
#     thread = threading.Thread(target=listen)
#     thread.daemon = True
#     thread.start()
#
#
# def on_startup(text: str):
#     va_speak(text)
#
#
# if __name__ == "__main__":
#     start_listening()
#     root = tk.Tk()
#
#     root.mainloop()
