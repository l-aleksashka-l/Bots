import telebot
import time

bot_token = '5130916795:AAEAvp3rcUNOouvsyDI6J4XoVULXRrjudzo'
bot = telebot.TeleBot(token=bot_token)

CHANNEL_NAME = '@prikolchaki'
# Загружаем список шуток
f = open('data/fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()
# Пока не закончатся шутки, посылаем их в канал
for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    # Делаем паузу в один час
    time.sleep(36)
bot.send_message(CHANNEL_NAME, "Анекдоты закончились :-(")