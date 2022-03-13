from telethon import TelegramClient
import configparser
from telethon.sessions import StringSession
import asyncio



# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']



client = TelegramClient(StringSession(), api_id, api_hash)
client.start()

async def main():
    channel = await client.get_entity('https://t.me/yornikhuyornik')
    messages = await client.get_messages(channel, limit= 10) #pass your own args
    print(client.session.save())
    a = 10
    #then if you want to get all the messages text
    for x in messages:
        print(x.text) #return message.text
        destination_channel_username = 'businessaidd'
        entity = await client.get_entity(destination_channel_username)
        await client.send_message(entity=entity, message=x)
        a = a - 1
        if(a<0):
            break


loop = asyncio.get_event_loop()
loop.run_until_complete(main())