import pymongo
from pymongo import MongoClient
from telethon import TelegramClient
import configparser
from telethon.sessions import StringSession
from telethon import events
import time

config = configparser.ConfigParser()
config.read("config.ini")

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_id_bot = config['Telegram']['api_id_bot']
api_hash_bot = config['Telegram']['api_hash_bot']
session_string = config['Telegram']['session_string']
session_string_bot = config['Telegram']['session_string_bot']

client = MongoClient("mongodb+srv://aleksashka:JyoXzdmxx06qeAUi@cluster0.rgmqp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
dbname = client['Telegram']

bot_token = '5130916795:AAEAvp3rcUNOouvsyDI6J4XoVULXRrjudzo'
client = TelegramClient(StringSession(session_string), api_id, api_hash)

bot = TelegramClient(StringSession(session_string_bot), api_id_bot, api_hash_bot).start(bot_token=bot_token)

client.start()

channel = 'https://t.me/prikolchaki'
target = 'businessaid'
channels = []


@bot.on(events.NewMessage(pattern = '/start'))
async def send_welcome(event):
    await event.reply('Give a number:')


async def new_item(id, link, collection_name, last):
    if not collection_name.find({"tgChannel": link}):
        item = {"tgID" : id, "tgChannel": link, "lastMessID" : last}
        collection_name.insert_one(item)




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
        collection_name = dbname[str(entity.id)]
        messages = await client.get_messages(entChannel, limit=1)
        for x in messages[:1]:
            m = x.id
        await new_item(entity.id, text, collection_name, m)
        await notmain(collection_name, entity.id)


async def notmain(collection_name, id):

    n_last = 1
    time_wait = 10
    for tgChannel in collection_name.find({}):
        channels = await client.get_entity(tgChannel["tgChannel"])
        messages = await client.get_messages(channels, limit=10)
        for x in messages[:n_last]:
            entity = await client.get_entity(target)
            await client.forward_messages(entity, x)
            filter = {'tgID': id}
            newvalues = {"$set": {'lastMessID': x.id}}
            collection_name.update_one(filter, newvalues)
        time.sleep(time_wait)


@bot.on(events.NewMessage)
async def echo_all(event):
    await check(event.text)


bot.run_until_disconnected()
