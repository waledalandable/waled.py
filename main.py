import os

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
        await msg.reply("🎧 البوت يعمل بنجاح 👑")
app.star()
print("Bot Running...")
idle()
