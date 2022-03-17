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
session_test = config['Telegram']['session_test']
session_string = config['Telegram']['session_string']
session_string_bot = config['Telegram']['session_string_bot']

client = MongoClient(
    "mongodb+srv://aleksashka:JyoXzdmxx06qeAUi@cluster0.rgmqp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
dbname = client['Telegram']

bot_token = '5130916795:AAEAvp3rcUNOouvsyDI6J4XoVULXRrjudzo'
client = TelegramClient(StringSession(session_string), api_id, api_hash)

bot = TelegramClient(StringSession(session_string_bot), api_id_bot, api_hash_bot).start(bot_token=bot_token)

client.start()

channel = 'https://t.me/prikolchaki'
target = 'businessaid'
channels = []


@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
    await event.reply('Send links to telegram channel:')


async def new_item(link, collection_name, last, tgId):
    #if not collection_name.find({"tgChannel": link}):
        item = {'tgID': tgId, "tgChannel": link, "lastMessID": last}
        collection_name.insert_one(item)


async def check(link, id):
    if link.startswith('https'):
        channel = await client.get_entity(link)
        collection_name = dbname['users']
        messages = await client.get_messages(channel, limit=1)
        last = 1
        for x in messages[:1]:
            last = x.id
        await new_item(link, collection_name, last, id)
        await notmain(collection_name, id)

    elif link.startswith('/run'):
        collection_name = dbname['users']
        await notmain(collection_name, id)


async def notmain(collection_name, id):
    n_last = 50
    time_wait = 600
    while True:
        for tgChannel in collection_name.find({}):
            channels = await client.get_entity(tgChannel["tgChannel"])
            messages = await client.get_messages(channels, limit=50)
            array = []
            for x in messages[:n_last]:
                filter = {'tgID': id, "tgChannel": tgChannel["tgChannel"]}
                try:
                    if x.id > collection_name.find_one(filter)["lastMessID"]:
                        array.append(x)

                    else:
                        break
                except Exception:
                    break
            try:
                array.reverse()
                for x in array:
                    filter = {'tgID': id, "tgChannel": tgChannel["tgChannel"]}
                    await client.forward_messages(id, x)
                    newvalues = {"$set": {'lastMessID': collection_name.find_one(filter)["lastMessID"] + 1}}
                    collection_name.update_one(filter, newvalues)
            except Exception:
                continue
        time.sleep(time_wait)


@bot.on(events.NewMessage)
async def echo_all(event):
    id = await event.get_sender()
    await check(event.text, id.id)


bot.run_until_disconnected()