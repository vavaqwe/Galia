from pyowm import OWM
from pyowm.utils.config import get_default_config

act = ['галя','галь']

list_news = ["новости", "расскажи новости", "какие новости", "что там по новостям"]

list_time = ["сколько время", "время", "который час"]

list_search = ["найди", "поищи", "кто такой", "что такое"]

list_browser = ["открой браузер", "включи браузер", "браузер"]

list_weather = ["погода", "погоду","какая сейчас погода в городе"]

list_write = ['музыку']

list_sound = ['сделай звук ','выключи звук','сделать звук']

owm = OWM('69be55df671a26b648a0b198c0739f9e')
config_dict = get_default_config()
config_dict['language'] = 'ru'
mgr = owm.weather_manager()

ffmpeg_path = r'bin\ffmpeg.exe'
