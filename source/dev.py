import random
from pyrogram import Client, filters, idle
from source.info import (joinch)
from source.Data import (get_dev, get_bot_name, set_bot_name, set_dev_user, get_dev_user, set_video_source)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import os
from source.start import selections

@Client.on_message(filters.command(["المطور", "مطور","مطور البوت"], ""))
async def dev(client: Client, message: Message):
     if await joinch(message):
            return
     bot_username = client.me.username
     dev = await get_dev(bot_username)
     user = await client.get_chat(chat_id=dev)
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور الأساسي**\n{chat_title}\nChat Id : `{message.chat.id}`",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
        pass
     await message.reply_photo(
     photo=photo,
     caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass
       

@Client.on_message(filters.command(["مطور السورس"], ""))
async def debsu(client: Client, message: Message):
     if await joinch(message):
            return
     bot_username = client.me.username
     dev = await get_dev(bot_username)
     DEV_USER = await get_dev_user(bot_username)
     user = await client.get_chat(chat_id=DEV_USER)
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"هناك شخص بالحاجه اليك عزيزي المطور الأساسي\n{chat_title}\nChat Id : {message.chat.id}",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
        pass
     await message.reply_photo(
     photo=photo,
     caption=f"Developer Name : {name} \nDevloper Username : @{username}\n{bio}",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass

@Client.on_message(filters.command("تعين اسم البوت", ""))
async def set_bot(client: Client, message):
   NAME = await client.ask(message.chat.id,"**ارسل اسم البوت الجديد .**", filters=filters.text, timeout=30)
   BOT_NAME = NAME.text
   bot_username = client.me.username
   await set_bot_name(bot_username, BOT_NAME)
   await message.reply_text("**تم تعين اسم البوت بنجاح .**")


@Client.on_message(filters.command(["بوت", "البوت"], ""))
async def bottttt(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    bar = random.choice(selections).format(BOT_NAME)
    await message.reply_text(f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**", disable_web_page_preview=True)
    
@Client.on_message(filters.command("تعين لوجو السورس", ""))
async def set_vi_so(client: Client, message):
   NAME = await client.ask(message.chat.id,"**ارسل رابط لوجو السورس .\nمثال ⟨ https://telegra.ph/file/fa5a2ef2f3d5b516a7499.mp4 ⟩ .**", filters=filters.text, timeout=30)
   VID_SO = NAME.text
   bot_username = client.me.username
   await set_video_source(bot_username, VID_SO)
   await message.reply_text("**تم تعين لوجو السورس  بنجاح .**")
   
   
   
@Client.on_message(filters.command("تعين يوزر مطور السورس", ""))
async def set_dev_username(client: Client, message):
   NAME = await client.ask(message.chat.id,"**ارسل معرف المطور الجديد .**", filters=filters.text, timeout=300)
   CH_DEV_USER = NAME.text
   bot_username = client.me.username
   await set_dev_user(bot_username, CH_DEV_USER)
   await message.reply_text("**تم تعين المطور بنجاح .**")