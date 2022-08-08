# ( c ) Buddhu

import pyrogram
from pyrogram import Client
from config import Config


if __name__ == "__main__" :
    plugins = dict(root="TheBot/plugins")
    app = pyrogram.Client(
        "Buddhu",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.run()
