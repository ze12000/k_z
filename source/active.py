from pyrogram import Client, filters, idle
from source.info import (joinch)
from source.Data import (get_groupsr)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import enums

@Client.on_message(filters.command(["تفعيل"], "") & ~filters.private)
async def pipong(client: Client, message: Message):
   if len(message.command) == 1:
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    gr = await get_groupsr(client.me.username)
    A_q_lp = InlineKeyboardMarkup([[InlineKeyboardButton("قناة البوت .", url=""+gr)]])
    await message.reply_text("**تم تفعيل البوت بنجاح .**",reply_markup=A_q_lp)
    return 
