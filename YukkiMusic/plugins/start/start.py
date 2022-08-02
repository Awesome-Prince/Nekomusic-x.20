from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="""────「 [Lisa 리사](https://telegra.ph/file/6e04c75f9e5739b35d9e3.jpg) 」────/n/nHey Babe✨💋/n/n➖➖➖➖➖➖➖➖➖➖➖➖➖/n/n❍ I Have A Sweetie Voice, You Wanna Hear That?/n/n❍ Add Me To Your Group And Do /play <song_name>/n/n➖➖➖➖➖➖➖➖➖➖➖➖➖/n/n➛ Dont Forgot To Join @Besties_XD✨""",
        reply_to_message_id=update.message_id
    )
