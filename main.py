from pyrogram import Client, idle
import os

print("Starting Bot...")

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def start(_, msg):
    if msg.text == "/start":
        await msg.reply("🎧 البوت يعمل 👑")

app.start()
print("Bot Running...")
idle()
