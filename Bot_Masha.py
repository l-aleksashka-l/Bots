import telebot
import os
import random
import numpy as np
from fuzzywuzzy import fuzz

bot_token = '5130916795:AAEAvp3rcUNOouvsyDI6J4XoVULXRrjudzo'
bot = telebot.TeleBot(token=bot_token)

mas = []
if os.path.exists('data/boltun.txt'):
    f = open('data/boltun.txt', 'r', encoding='UTF-8')
    for x in f:
        if (len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()


def answer(text):
    try:
        text = text.lower().strip()
        if os.path.exists('data/boltun.txt'):
            n = 0
            nn = 1
            num = []
            for q in mas:
                if ('u: ' in q):
                    # С помощью fuzzywuzzy получаем, насколько похожи две строки
                    aa = (fuzz.token_sort_ratio(q.replace('u: ', ''), text))
                    if (aa > 70):
                        num.append(n)
                n = n + 1
                nn = nn + 1
            if not num:
                return 'Не понимаю тебя! Хуй вынь и скажи еще раз!'
            else:
                np.random.shuffle(num)
                print(num)
                s = mas[num[0] + 1]
                return s
        else:
            return 'Ошибка тут'
    except:
        return 'Ошибка'


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне Привет )')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Запись логов
    f = open('data/' + str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
    s = answer(message.text)
    f.write('u: ' + message.text + '\n' + s + '\n')
    f.close()
    # Отправка ответа
    bot.send_message(message.chat.id, s)


# Запускаем бота
bot.polling(none_stop=True, interval=0)


