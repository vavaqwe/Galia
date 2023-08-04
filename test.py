# responses = {
#     "привет": "Привет! Чем я могу помочь?",
#     "как дела": "У меня всё отлично, спасибо!",
#     "погода": "Извините, я пока не умею предоставлять информацию о погоде.",
#     # Добавьте здесь другие ключевые фразы и соответствующие ответы
# }
#
# def get_response(text):
#     for key in config.responses:
#         if key in query:
#             return responses[key]
#     return "Извините, я такого ещё не умею"
#
# print(get_response("привет"))
# from googlesearch import search
# for i in search('python'):
#     print(i)
#     break
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.stem import SnowballStemmer
# from nltk.corpus import stopwords
#
# nltk.download('punkt')
# nltk.download('stopwords')
#
# stemmer = SnowballStemmer('russian')
# stop_words = set(stopwords.words('russian'))
# def process_text(text):
#     tokens = word_tokenize(text.lower())  # Разделение текста на токены (слова) и приведение к нижнему регистру
#     filtered_tokens = [token for token in tokens if token not in stop_words]  # Удаление стоп-слов
#     cleaned_tokens = [stemmer.stem(token) for token in filtered_tokens if token.isalpha()]  # Лемматизация и удаление пунктуации
#     return cleaned_tokens
#
# print(process_text("что ты умеешь"))
import webbrowser

# import nltk
# nltk.download('punkt')
#
# from nltk.tokenize import word_tokenize, sent_tokenize
#
# text = "NLTK (Natural Language Toolkit) - это библиотека для обработки естественного языка."
#
# # Токенизация по предложениям
# sentences = sent_tokenize(text)
# print(sentences)
#
# # Токенизация по словам
# words = word_tokenize(text)
# print(words)


# from nltk.stem import PorterStemmer, WordNetLemmatizer
# nltk.download('wordnet')
#
# stemmer = PorterStemmer()
# lemmatizer = WordNetLemmatizer()
#
# word = "running"
# stemmed_word = stemmer.stem(word)
# lemmatized_word = lemmatizer.lemmatize(word)
#
# print("Stemmed word:", stemmed_word)
# print("Lemmatized word:", lemmatized_word)

# from nltk.corpus import movie_reviews
# nltk.download('movie_reviews')
#
# documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
# import random
# random.shuffle(documents)
#
# all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# word_features = list(all_words)[:2000]
#
# def document_features(document):
#     document_words = set(document)
#     features = {}
#     for word in word_features:
#         features['contains({})'.format(word)] = (word in document_words)
#     return features
#
# featuresets = [(document_features(d), c) for (d, c) in documents]
# train_set, test_set = featuresets[:1600], featuresets[1600:]
#
# classifier = nltk.NaiveBayesClassifier.train(train_set)
#
# print("Accuracy:", nltk.classify.accuracy(classifier, test_set))



#
# from pymystem3 import Mystem
# m = Mystem()
# def lemmatize_sentence(text):
#     lemmas = m.lemmatize(text)
#     return "".join(lemmas).strip()
#
# print(lemmatize_sentence("ку"))


# import subprocess
#
# def play_audio_from_youtube(video_url):
#     try:
#         # Загружаем лучший аудиофайл из YouTube с помощью youtube-dl
#         command = ["youtube-dl", "-x", "--audio-format", "best", "--no-playlist", "--quiet", video_url]
#         subprocess.call(command)
#
#         # Проигрываем аудиофайл с помощью ffplay
#         command = ["ffplay", "-nodisp", "-autoexit", "output.mp3"]
#         subprocess.call(command)
#
#     except Exception as e:
#         print("Произошла ошибка:", e)
#
# # Пример использования:
# video_url = "https://www.youtube.com/watch?v=HyHNuVaZJ-k"
# play_audio_from_youtube(video_url)


# import subprocess
#
# def play_audio_with_ffmpeg(audio_file_path, ffmpeg_path):
#     try:
#         # Команда для проигрывания аудио с помощью ffmpeg
#         command = [ffmpeg_path, '-i', audio_file_path, '-nodisp', '-autoexit', '-loglevel', 'error']
#         subprocess.run(command, check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Произошла ошибка при проигрывании аудио: {e}")
#     except FileNotFoundError:
#         print("Файл ffmpeg не найден. Убедитесь, что путь к ffmpeg указан правильно.")
#
# # Пример использования:
# audio_file_path = 'https://www.youtube.com/watch?v=qKlUpmZwsyw'  # Укажите путь к аудиофайлу
# ffmpeg_path = r'bin/ffmpeg.exe'  # Укажите путь к ffmpeg, если он не находится в системном пути
#
# play_audio_with_ffmpeg(audio_file_path, ffmpeg_path)


# from pytube import YouTube , Search
# import subprocess
#
# def you(text):
#     search_results = Search(text)
#     for v in search_results.results:
#         link = f"{v.title}\n{v.watch_url}\n"
#         print(v.watch_url, type(v.watch_url))
#         return v.watch_url
#
#
# def play_audio(audio_stream_url, ffmpeg_path):
#     command = [ffmpeg_path, '-i', audio_stream_url, '-acodec', 'pcm_s16le', '-f', 's16le', '-ac', '2', '-ar', '48000', '-']
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     process.wait()
#
# # Пример использования:
# ffmpeg_path = 'bin//ffmpeg.exe'
#
# play_audio(you("feel good"), ffmpeg_path)

#
#
# from pytube import YouTube, Search
# import subprocess
#
#
# def search_youtube(text):
#     search_results = Search(text)
#     video_urls = [v.watch_url for v in search_results.results]
#     return video_urls
#
#
# def play_video(video_url, ffplay_path):
#     command = [ffplay_path, video_url]
#     subprocess.call(command)
#
#
# # Пример использования:
# ffplay_path = 'bin//ffmpeg.exe'  # Укажите путь к ffplay
# video_urls = search_youtube("feel good")
#
#
# play_video(video_urls[0], ffplay_path)  # Воспроизведение первого видео

# from pytube import YouTube
# import subprocess
#
# def play_video(video_url, ffplay_path):
#     yt = YouTube(video_url)
#     video_stream = yt.streams.get_highest_resolution()
#     video_stream.download(output_path='video_temp')
#
#     command = [ffplay_path, 'video_temp/' + video_stream.default_filename]
#     subprocess.call(command)
#
# # Example usage:
# ffplay_path = r'bin\ffmpeg.exe'  # Specify the path to ffplay
# video_url = "https://www.youtube.com/watch?v=HyHNuVaZJ-k"
# play_video(video_url, ffplay_path)
