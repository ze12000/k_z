from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "mo",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    A_q_lp = "TR_E2S_ON_MY_MOoN"
    await bot.send_message(A_q_lp, "** اشتغلت . **")
    print("[INFO]:   ")
    await idle()
