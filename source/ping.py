from pyrogram import Client, filters, idle
from time import time
from source.info import (joinch)
from pyrogram.types import Message
from pyrogram import enums
import time

@Client.on_message(filters.command(["/ping", "بنج"], ""))
async def ping_pong(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    start = time()
    m_reply = await message.reply_text("**pinging...**")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")