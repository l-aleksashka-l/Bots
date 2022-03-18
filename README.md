# Bots
>I start use [telebot](https://github.com/eternnoir/pyTelegramBotAPI) library and wrote 5 simply bots:
## Bot-Parrot
- Hi.  
- Hi.
## Bot-Wiki (ru)
- Car
- Car - is a wheeled motor vehicle used for transportation.Most definitions of cars say that they run primarily on roads, seat one to eight people, have four wheels, and mainly transport people rather than goods.  
## Bot-Fact/Mind (ru)
- Fact (Button)
- The modern generation of processors of the Pentium D or Athlon-64 3000+ class require dissipation of about 90-100 watts of heat.
## Bot-Poster
Every 36 sec post joke in telegram channel
## Bot-Masha (ru) 
#### Quastions and answers wrote at file and limited
- Hello
- HI!
- How are u!
- Good!  
...  

---

# Folder with parsers
>I start use [telethon](https://docs.telethon.dev/en/stable/) library and write chat parser to json file. 
## Parser
Get channel (were i have administrator right) and parse to json N messages and all subscribers at this channel  
###### {"_": "Message", "id": 38, "peer_id": {"_": "PeerChannel", "channel_id": ***********}, "date": "2022-03-13T08:36:31+00:00", "message": "FULL TEXT MESSAGE", "out": true, "mentioned": false, "media_unread": false, "silent": false, "post": true, "from_scheduled": false, "legacy": false, "edit_hide": false, "pinned": false, "from_id": null, "fwd_from": null, "via_bot_id": null, "reply_to": null, "media": null, "reply_markup": null, "entities": [], "views": 1, "forwards": 0, "replies": null, "edit_date": null, "post_author": "Александр", "grouped_id": null, "restriction_reason": [], "ttl_period": null}
## Simply Parser
Forward message from channel to user (use number, link or channel/username)  
Voice and video message, photos, links, videos parsing too

---

### BOT_TELEGRAM_PARSER  
-https:tgchannel  
Send all new messages every 10 minutes  
Have little bags with MongoDB updates  
Can't deploy with Heroku because have MongoDB bags
