from pyrogram import Client, filters, idle
from config import OWNER
from source.info import (is_served_user, add_served_user, joinch)
from source.Data import (get_dev)
from pyrogram.types import Message


OFFPV = []

@Client.on_message(filters.command(["تفعيل التواصل","تعطيل التواصل"], ""))
async def byyye(client, message):
    user = message.from_user.username
    dev = await get_dev(client.me.username)
    if user in OWNER or message.from_user.id == dev:
        text = message.text
        if text == "تفعيل التواصل":
          if not client.me.username in OFFPV:
             await message.reply_text("**التواصل مفعل من قبل .**")
          try:
            OFFPV.remove(client.me.username)
            await message.reply_text("**تم تفعيل التواصل .**")
            return
          except:
             pass
        if text == "تعطيل التواصل":
          if client.me.username in OFFPV:
             await message.reply_text("**التواصل معطل من قبل .**")
          try:
            OFFPV.append(client.me.username)
            await message.reply_text("**تم تعطيل التواصل .**")
            return
          except:
             pass


@Client.on_message(filters.private)
async def botoot(client: Client, message: Message):
 if not client.me.username in OFFPV:
  if await joinch(message):
            return
  bot_username = client.me.username
  user_id = message.chat.id
  if not await is_served_user(client, user_id):
     await add_served_user(client, user_id)
  dev = await get_dev(bot_username)
  if message.from_user.id == dev or message.chat.username in OWNER or message.from_user.id == client.me.id:
    if message.reply_to_message:
     u = message.reply_to_message.forward_from
     try:
       await client.send_message(u.id, text=message.text)
       await message.reply_text(f"**تم ارسال رساتلك إلي {u.mention} بنجاح .**")
     except Exception:
         pass
  else:
   try:
    await client.forward_messages(dev, message.chat.id, message.id)
    await client.forward_messages(OWNER[0], message.chat.id, message.id)
   except Exception as e:
     pass
 message.continue_propagation()