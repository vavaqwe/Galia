# C ТРЕЕМ
import sys
import threading
import pystray

from  speak import *
from voice import va_speak
from pystray import MenuItem as item
from PIL import Image
from function import *
import config

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
    words = text.split()  # Разделяем строку на слова
    first_word = words[0]
    for i in config.act:
        if first_word == i:
            remaining_words = text[4:]  # Присваиваем новую строку с удаленными символами переменной text
            print(remaining_words)
            news(remaining_words)
            off(remaining_words)
            ua(remaining_words)
            time_now(remaining_words)

def on_exit():
    print("Приложение завершено")
    tray.stop()
    sys.exit(0)


menu = (item('Выход', on_exit),)


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
