from pyrogram import Client, filters
import os
import random 
import asyncio
import pytgcalls
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import PHOTO, OWNER_NAME, OWNER
from source.info import (add, is_served_call, add_active_video_chat, add_served_call, add_active_chat, remove_active, joinch)
from source.Data import (get_userbot, get_call, get_group, get_channel)
import asyncio
from source.play import seconds_to_min, join_call, logs



@Client.on_message(filters.command(["عشوائي", "تشغيل عشوائي"], ""))
async def aii(client: Client, message):
   if await joinch(message):
            return
   try:
    chat_id = message.chat.id
    bot_username = client.me.username
    rep = await message.reply_text("**جاري تشغيل اغنية عشوائية لك انتظر قد يستغرق بعض القائق.**")
    try:
          call = await get_call(bot_username)
    except:
          await remove_active(bot_username, chat_id)
    try:
       await call.get_call(message.chat.id)
    except pytgcalls.exceptions.GroupCallNotFound:
       await remove_active(bot_username, chat_id)
    message_id = message.id
    user = await get_userbot(bot_username)
    req = message.from_user.mention if message.from_user else message.chat.title
    raw_list = []
    async for msg in user.get_chat_history("ELNQYBMUSIC"):
        if msg.audio:
          raw_list.append(msg)
    x = random.choice(raw_list)
    file_path = await x.download()
    file_name = x.audio.title
    title = file_name
    dur = x.audio.duration
    duration = seconds_to_min(dur)
    photo = PHOTO
    vid = True if x.video else None
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "R7_OX"
    videoid = None
    link = None
    await add(message.chat.id, bot_username, file_path, link, title, duration, videoid, vid, user_id)
    if not await is_served_call(client, message.chat.id): 
      await add_active_chat(chat_id)
      await add_served_call(client, chat_id)
      if vid:
        await add_active_video_chat(chat_id)
      link = None
      c = await join_call(client, message_id, chat_id, bot_username, file_path, link, vid)
      if not c:
            await remove_active(bot_username, chat_id)
            return await rep.delete()
    await rep.delete()
    gr = await get_group(bot_username)
    ch = await get_channel(bot_username)
    button = [[InlineKeyboardButton(text="𓏺 َِ𝖤َِ𝗇َِ𝖣 .", callback_data=f"stop"), InlineKeyboardButton(text="𓏺 َِ𝖱َِ𝖾َِ𝖲َِ𝗎َِ𝖬َِ𝖾 .", callback_data=f"resume"), InlineKeyboardButton(text="𓏺 َِ𝖯َِ𝖺َِ𝖴َِ𝗌َِ𝖤 .", callback_data=f"pause")], [InlineKeyboardButton(text="𓏺 َِ𝗖َِ𝗵َِ𝗔َِ𝗻َِ𝗡َِ𝗲َِ𝗟 .", url=f"{ch}"), InlineKeyboardButton(text="𓏺 َِ𝖦َِ𝗋َِ𝖮َِ𝗎َِ𝖯 .", url=f"{gr}")], [InlineKeyboardButton(text=f"{OWNER_NAME}", url=f"https://t.me/{OWNER}")], [InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك ⚡", url=f"https://t.me/{bot_username}?startgroup=True")]]
    await message.reply_photo(photo=photo, caption=f"**𓏺 َِ𝗦َِ𝘁َِ𝗔َِ𝗿َِ𝗧َِ𝗲َِ𝗗 َِ𝗦َِ𝘁َِ𝗥َِ𝗲َِ𝗔َِ𝗺 َِ𝗥َِ𝗮َِ𝗡َِ𝗱َِ𝗢َِ𝗺 . .\n\n𓏺 َِ𝗦َِ𝗼َِ𝗡َِ𝗴 َِ𝗡َِ𝗮َِ𝗠َِ𝗲 . : {title} .\n𓏺 َِ𓏺 َِ𝗗َِ𝘂َِ𝗥َِ𝗮َِ𝗧َِ𝗶َِ𝗢َِ𝗻 َِ𝗧َِ𝗶َِ𝗠َِ𝗲 . : {duration} .\n𓏺𓏺 َِ𝗥َِ𝗲َِ𝗤َِ𝘂َِ𝗘َِ𝘀َِ𝗧 َِ𝗕َِ𝘆 . : {req} .**", reply_markup=InlineKeyboardMarkup(button))
    await logs(bot_username, client, message)
    await asyncio.sleep(4)
    os.remove(file_path)
   except Exception as es:
    pass