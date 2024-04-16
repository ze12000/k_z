import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

OWNER = ["TR_E2S_ON_MY_MOoN","L_HLN"]
OWNER_NAME = "king"
BOT_TOKEN = getenv("BOT_TOKEN")
DATABASE = getenv("MONGO_DB_URI", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
CHANNEL = "https://t.me/sourceav"
GROUP = "https://t.me/va_source"
VID_SO = "https://telegra.ph/file/4fda78aaf200bf313be62.jpg"
PHOTO = "https://telegra.ph/file/4fda78aaf200bf313be62.jpg"
LOGS = "jabababbab"
