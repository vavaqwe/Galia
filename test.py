# responses = {
#     "привет": "Привет! Чем я могу помочь?",
#     "как дела": "У меня всё отлично, спасибо!",
#     "погода": "Извините, я пока не умею предоставлять информацию о погоде.",
#     # Добавьте здесь другие ключевые фразы и соответствующие ответы
# }
#
# def get_response(query):
#     for key in responses:
#         if key in query:
#             return responses[key]
#     return "Извините, не могу понять ваш запрос."
#
# print(get_response("привет"))
from googlesearch import search
for i in search('python'):
    print(i)
    break
