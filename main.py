# C ТРЕЕМ
# import sys
import threading
import pystray
import tkinter as tk

from  speak import *
# from voice import va_speak
from PIL import Image
from function import *
import config
from tkinter import simpledialog

def listen():
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and len(data) > 0:
            answer = json.loads(rec.Result())
            if answer['text']:
                on_startup(answer['text'])

def start_listening():
    thread = threading.Thread(target=listen)
    thread.daemon = True
    thread.start()

def on_startup(text: str):
    print(text)
    words = text.split()
    first_word = words[0]
    for i in config.act:
        if first_word == i:
            new_string = ' '.join(words[1:])
            news(new_string)
            off(new_string)
            ua(new_string)
            time_now(new_string)
            check_weather_commands(text)
            exit(new_string)

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
