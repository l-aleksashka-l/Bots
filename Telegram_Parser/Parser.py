import configparser
import json

from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']


client = TelegramClient(username, api_id, api_hash)

client.start()


async def dump_all_messages(channel):
	"""Записывает json-файл с информацией о всех сообщениях канала/чата"""
	offset_msg = 0    # номер записи, с которой начинается считывание
	limit_msg = 2  # максимальное число записей, передаваемых за один раз

	all_messages = []   # список всех сообщений
	total_messages = 0
	total_count_limit = 5  # поменяйте это значение, если вам нужны не все сообщения

	class DateTimeEncoder(json.JSONEncoder):
		'''Класс для сериализации записи дат в JSON'''
		def default(self, o):
			if isinstance(o, datetime):
				return o.isoformat()
			if isinstance(o, bytes):
				return list(o)
			return json.JSONEncoder.default(self, o)

	while True:
		history = await client(GetHistoryRequest(
			peer=channel,
			offset_id=offset_msg,
			offset_date=None, add_offset=0,
			limit=limit_msg, max_id=0, min_id=0,
			hash=0))
		if not history.messages:
			break
		messages = history.messages
		for message in messages:
			all_messages.append(message.to_dict())
			destination_channel_username = 'STePaNoNVaDiM'
			entity = client.get_entity(destination_channel_username)
			client.send_message(entity=entity, message=message)
		offset_msg = messages[len(messages) - 1].id
		total_messages = len(all_messages)
		if total_count_limit != 0 and total_messages >= total_count_limit:
			break

	with open('channel_messages.json', 'w', encoding='utf8') as outfile:
		 json.dump(all_messages, outfile, ensure_ascii=False, cls=DateTimeEncoder)


async def main():
	url = input("Введите ссылку на канал или чат: ")
	channel = await client.get_entity(url)
#dialog =  client.get_dialogs()
#print(dialog)
	await dump_all_messages(channel)


with client:
	client.loop.run_until_complete(main())

async def add_new_table(id)
  cursor = con.cursor()
  start_query = "CREATE TABLE IF NOT EXISTS "
  end_query = "(id SERIAL PRIMARY KEY, title TEXT NOT NULL, description TEXT NOT NULL, user_id INTEGER REFERENCES users(id))"
  create_posts_table = start_query + id + end_query
  cursor.execute(create_post_table)
  print("Table created successfully")
  con.commit()
  con.close()

  con = psycopg2.connect(
	  database="postgres",
	  user="postgres",
	  password="",
	  host="127.0.0.1",
	  port="5432"
  )


async def check(text):
	global target
	if text.startswith('+'):
		target = text
		destination_channel_username = target
		entity = await client.get_entity(destination_channel_username)
		await bot.send_message(entity, 'Add telegram channels to bot:')
	elif text.startswith('https'):
		entity = await client.get_entity(target)
		entChannel = await client.get_entity(text)
		await new_item(entity.id, text, entChannel.id)
		await notmain(text)






