from pyrogram import Client, filters
from youtubesearchpython.__future__ import VideosSearch 
import os
from youtube_search import YoutubeSearch
import pytgcalls
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_NAME, OWNER
from pyrogram.enums import ChatType, ChatMemberStatus
from source.info import (db, add, is_served_call, add_active_video_chat, add_served_call, add_active_chat, gen_thumb, download, remove_active, joinch)
from source.Data import (get_call, get_group, get_channel)
from source.play import (logs, join_call, seconds_to_min, )

@Client.on_message(filters.command(["• تشغيل مخصص •", "• تشغيل في قناه او مجموعه •"], ""))
async def pla1y(client: Client, message):
  if await joinch(message):
            return        
  ESLAM = message
  bot_username = client.me.username
  chat_id = message.chat.id
  user_id = message.from_user.id if message.from_user else "TR_E2S_ON_MY_MOoN"
  message_id = message.id 
  gr = await get_group(bot_username)
  ch = await get_channel(bot_username)
  if not message.reply_to_message:
     if len(message.command) == 1:
      if message.chat.type == ChatType.CHANNEL:
        return await message.reply_text("**قم كتابة شيئ لتشغيلة.**")
      try:
       ask = await client.ask(message.chat.id, "ارسل معرف المجموعه", reply_to_message_id=message.id, filters=filters.user(message.from_user.id), timeout=20)
       GUS = ask.text
       ushh = (await client.get_chat(GUS)).id
       chat_id = ushh
      except:
       return
      try:
       name = await client.ask(message.chat.id, text="**ارسل اسم او رابط الي تريد تشغيله.**", reply_to_message_id=message.id, filters=filters.user(message.from_user.id), timeout=20)
       name = name.text
       rep = await message.reply_text("**جاري التشغيل انتظر قليلا.**")
      except:
       return
     else:
       name = message.text.split(None, 1)[1]
     try:
      results = VideosSearch(name, limit=1)
     except Exception:
      return await rep.edit("**لم يتم العثور علي نتائج.**")
     for result in (await results.next())["result"]:
         title = result["title"]
         duration = result["duration"]
         videoid = result["id"]
         yturl = result["link"]
         thumbnail = result["thumbnails"][0]["url"].split("?")[0]
     if "v" in message.command[0] or "ف" in message.command[0]:
       vid = True
     else:
       vid = None
     await rep.edit("**جاري التشغيل انتظر قليلا ⚡ .**")
     results = YoutubeSearch(name, max_results=5).to_dict()
     link = f"https://youtube.com{results[0]['url_suffix']}"
     if await is_served_call(client, ushh):
         chat_id = ushh
         title = title.title()
         file_path = None
         await add(ushh, bot_username, file_path, link, title, duration, videoid, vid, user_id)
         chat = f"{bot_username}{chat_id}"
         position = len(db.get(chat)) - 1
         chatname = f"[{message.chat.title}](https://t.me/{message.chat.username})" if message.chat.username else f"{message.chat.title}"
         chatname = f"{message.author_signature}" if message.author_signature else chatname
         requester = chatname if ESLAM.views else f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
         if message.from_user:
          if message.from_user.photo:
           message.from_user.photo.big_file_id
           photo = await client.download_media(photo_id)
          elif message.chat.photo:
           photo_id = message.chat.photo.big_file_id
           photo = await client.download_media(photo_id)
          else:
           ahmed = await client.get_chat("TR_E2S_ON_MY_MOoN")
           ahmedphoto = ahmed.photo.big_file_id
         elif message.chat.photo:
          photo_id = message.chat.photo.big_file_id
          photo = await client.download_media(photo_id)
         else:
          ahmed = await client.get_chat("TR_E2S_ON_MY_MOoN")
          ahmedphoto = ahmed.photo.big_file_id
          photo = await client.download_media(ahmedphoto)
         photo = await gen_thumb(videoid, photo)
         await message.reply_photo(photo=photo, caption=f"Add Track To Playlist » {position}\n\nSong Name : {title[:18]}\nDuration Time : {duration}\nRequests By : {requester}")
         await logs(bot_username, client, message)
     else:
         chat_id = ushh
         title = title.title()
         await add_active_chat(chat_id)
         await add_served_call(client, chat_id)
         if vid:
           await add_active_video_chat(chat_id)
         file_path = await download(bot_username, link, vid)
         await add(ushh, bot_username, file_path, link, title, duration, videoid, vid, user_id)
         c = await join_call(client, message_id, chat_id, bot_username, file_path, link, vid)
         if not c:
            await remove_active(bot_username, chat_id)
            return await rep.delete()
         chatname = f"[{message.chat.title}](https://t.me/{message.chat.username})" if message.chat.username else f"{message.chat.title}"
         chatname = f"{message.author_signature}" if message.author_signature else chatname
         requester = chatname if ESLAM.views else f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
         if message.from_user:
          if message.from_user.photo:
           message.from_user.photo.big_file_id
           photo = await client.download_media(photo_id)
          elif message.chat.photo:
           photo_id = message.chat.photo.big_file_id
           photo = await client.download_media(photo_id)
          else:
           ahmed = await client.get_chat("TR_E2S_ON_MY_MOoN")
           ahmedphoto = ahmed.photo.big_file_id
         elif message.chat.photo:
          photo_id = message.chat.photo.big_file_id
          photo = await client.download_media(photo_id)
         else:
          ahmed = await client.get_chat("TR_E2S_ON_MY_MOoN")
          ahmedphoto = ahmed.photo.big_file_id
          photo = await client.download_media(ahmedphoto)
         photo = await gen_thumb(videoid, photo)
         await message.reply_photo(photo=photo, caption=f"Starting Playing Now\n\nSong Name : {title[:18]}\nDuration Time : {duration}\nRequests By : {requester}")
         await logs(bot_username, client, message)
     await rep.delete()
  button = [[InlineKeyboardButton(text="⸢ 𝙀𝙉𝘿 ⸥", callback_data=f"stop"), InlineKeyboardButton(text="⸢ 𝙍𝙀𝙎𝙐𝙈𝙀 ⸥", callback_data=f"resume"), InlineKeyboardButton(text="⸢ 𝙋𝘼𝙐𝙎𝙀 ⸥", callback_data=f"pause")], [InlineKeyboardButton(text="ᥴ𝗁ᥲ️ꪀꪀᥱᥣ", url=f"{ch}"), InlineKeyboardButton(text="ᘜᖇ᥆υρ", url=f"{gr}")], [InlineKeyboardButton(text=f"{OWNER_NAME}", url=f"https://t.me/{OWNER}")], [InlineKeyboardButton(text="✘ اضف البوت الي مجموعتك او قناتك ✘", url=f"https://t.me/{bot_username}?startgroup=True")]]
  if message.chat.type == ChatType.PRIVATE:
     if message.chat.type == ChatType.CHANNEL:
      return await message.reply_text("يمكنك التشغيل بحسابك الخاص فقط.")
  if not len(message.command) == 1:
    rep = await message.reply_text("جاري التشغيل انتظر قليلا.")
  try:
          call = await get_call(bot_username)
  except:
          await remove_active(bot_username, chat_id)
  try:
       await call.get_call(ushh)
  except pytgcalls.exceptions.GroupCallNotFound:
       await remove_active(bot_username, chat_id)
  else:
       if not message.reply_to_message.media:
         return
       rep = await message.reply_text("جاري تشغيل الملف انتظر قليلا 🚦 .") 
       photo = "Uploaded to https://telegra.ph/file/562324befcafe035436dc.jpg"
       if message.reply_to_message.video or message.reply_to_message.document:
           vid = True
       else:
           vid = None
       file_path = await message.reply_to_message.download()
       if message.reply_to_message.audio:
         file_name = message.reply_to_message.audio
       elif message.reply_to_message.voice:
         file_name = message.reply_to_message.voice
       elif message.reply_to_message.video:
         file_name = message.reply_to_message.video
       else:
         file_name = message.reply_to_message.document
         title = file_name.file_name
       duration = seconds_to_min(file_name.duration)
       link = None
       if await is_served_call(client, ushh):
         chat_id = ushh
         videoid = None
         await add(ushh, bot_username, file_path, link, title, duration, videoid, vid, user_id)
         chat = f"{bot_username}{chat_id}"
         position = len(db.get(chat)) - 1
         chatname = f"[{message.chat.title}](https://t.me/{message.chat.username})" if message.chat.username else f"{message.chat.title}"
         chatname = f"{message.author_signature}" if message.author_signature else chatname
         requester = chatname if ESLAM.views else f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
         await message.reply_photo(photo=photo, caption=f"Add Track To Playlist » {position}\n\nSong Name : {title}\nDuration Time {duration}\nRequests By : {requester}", reply_markup=InlineKeyboardMarkup(button))
         await logs(bot_username, client, message)
       else:
         chat_id = ushh
         videoid = None
         await add_active_chat(chat_id)
         await add_served_call(client, chat_id)
         if vid:
            await add_active_video_chat(chat_id)
         await add(ushh, bot_username, file_path, link, title, duration, videoid, vid, user_id)
         c = await join_call(client, message_id, chat_id, bot_username, file_path, link, vid)
         if not c:
            await remove_active(bot_username, chat_id)
            return await rep.delete()
         chatname = f"[{message.chat.title}](https://t.me/{message.chat.username})" if message.chat.username else f"{message.chat.title}"
         chatname = f"{message.author_signature}" if message.author_signature else chatname
         requester = chatname if ESLAM.views else f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
         await message.reply_photo(photo=photo, caption=f"Starting Playing Now\n\nSong Name : {title}\nDuration Time {duration}\nRequests By : {requester}", reply_markup=InlineKeyboardMarkup(button))
         await logs(bot_username, client, message)
  try:
     os.remove(file_path)
     os.remove(photo)
  except:
     pass
  await rep.delete()
