import random
from pyrogram import Client, filters, idle
from pyrogram import Client
from config import OWNER
from source.info import (joinch)
from source.Data import (get_dev)
from pyrogram.types import Message
from pyrogram import enums


@Client.on_message(filters.command("رتبتي", ""))
async def bt(client: Client, message: Message):
  try:
     if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
     userr = message.from_user
     bot_username = client.me.username
     dev = await get_dev(bot_username)
     if userr.username in OWNER :
         await message.reply_text("**رتبتك هي : صاحب السورس .**")
         return
     if userr.username in ["TR_E2S_ON_MY_MOoN"]:
         await message.reply_text("**رتبتك هي : المطور كينج .**")
         return
     if userr.username in ["L_HLN"]:
         await message.reply_text("**رتبتك هي : المطور زين .**")
         return    
     if userr.id == dev:
        return await message.reply_text("**رتبتك هي : المطور الاساسي .**")
     user = await message._client.get_chat_member(message.chat.id, message.from_user.id)
     if user.status == enums.ChatMemberStatus.OWNER:
         await message.reply_text("**رتبتك هي : المالك .**")
         return
     if user.status == enums.ChatMemberStatus.ADMINISTRATOR:
         await message.reply_text("**رتبتك هي : الادمن .**")
         return 
     else:
         await message.reply_text("**رتبتك هي : العضو .**")
  except:
    pass