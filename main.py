# C ТРЕЕМ
from  speak import *
from voice import va_speak
import sys
import threading
import pystray
from pystray import MenuItem as item
from PIL import Image



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
    # сделай здесь обработку текста тоесть 1 слова это галя или нет
    va_speak(text)

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
