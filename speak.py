import asyncio
import json

from vosk import Model, KaldiRecognizer
import pyaudio

model = Model(r'./models/vosk-model-small-ru-0.22')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()


async def listen():
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and len(data) > 0:
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']
        await asyncio.sleep(0.1)
