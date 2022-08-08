# ( c ) Buddhu

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@Client.on_message(filters.command(["start"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>
Hello, How are You! This is @bjsodh's Bot""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "My Father", url="https://t.me/bjsodha"
                    )
                ]
            ]
        )
    )

    
# Just like Above You can Make More Custom Commands. 
