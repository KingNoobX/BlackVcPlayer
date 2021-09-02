import requests
from pyrogram import Client as Bot

from BlackVcPlayer.config import API_HASH
from BlackVcPlayer.config import API_ID
from BlackVcPlayer.config import BG_IMAGE
from BlackVcPlayer.config import BOT_TOKEN
from BlackVcPlayer.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="BlackVcPlayer.modules"),
)

bot.start()
run()
