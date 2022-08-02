from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="""────「 [Lisa 리사](https://telegra.ph/file/6e04c75f9e5739b35d9e3.jpg) 」────
               Hey Babe✨💋
               ➖➖➖➖➖➖➖➖➖➖➖➖➖
               ❍ I Have A Sweetie Voice, You Wanna Hear That?
               ❍ Add Me To Your Group And Do /play <song_name>
               ➖➖➖➖➖➖➖➖➖➖➖➖➖
               ➛ Dont Forgot To Join @Besties_XD✨""",
        reply_to_message_id=update.message_id
    )
