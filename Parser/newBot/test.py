from pymongo import MongoClient
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

print('Hello world')

client = TelegramClient(StringSession(), api_id, api_hash)
client.start()
print(client.session.save())

client = MongoClient("mongodb+srv://aleksashka:JyoXzdmxx06qeAUi@cluster0.rgmqp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
dbname = client['Telegram']
collection = dbname['User']

post1 = {"tgID" : 873828, "tgChannel": "https://t.me/nemorgenshtern", "lastMessID" : 2222}
post2 = {"tgID" : 873353, "tgChannel": "https://t.me/nemorgenshtern", "lastMessID" : 3333}


results = collection.insert_many([post1,post2])
for x in collection.find({}):
    print(x["tgChannel"])

print(collection.find_one({"tgID": 873828}))

#collection.delete_one({"tgID":873828})

#for x in  collection.find({}):
#    print(x)


#collection.delete_many({})

#for x in  collection.find({}):
  #  print(x)