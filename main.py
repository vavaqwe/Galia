import tkinter as tk
import asyncio
import asynctkinter as at

from speak import listen
from voice import va_speak

at.patch_unbind()

async def main():
    async for text in listen():
        process_text(text)
        label.config(text=text)
        await asyncio.sleep(0.1)

def process_text(text):
    print(text)

async def listen_wrapper():
    async for text in listen():
        yield text

if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root, text="Ожидание результата...")
    label.pack()

    at.start(main())
    root.mainloop()

