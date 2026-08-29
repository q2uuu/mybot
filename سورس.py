import os
from pyrogram import Client

# معلومات التطبيق وتوكن البوت الخاص بك
API_ID = 37134501
API_HASH = "1b2112337672599ca9265b93cb442ccd"
BOT_TOKEN = "8334243012:AAFuVHaduzy1ucnqHYFgzvR_N8qzaQit8iQ"

# تشغيل البوت المتحكم
bot = Client(
    "ControlPanelBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message()
async def control_handler(client, message):
    # مكان استقبال أوامر البوت والأزرار لتجميع بيانات المستخدمين
    pass

if __name__ == "__main__":
    print("البوت يعمل الآن...")
    bot.run()
