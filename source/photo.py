import random
from pyrogram import Client, filters, idle
from pyrogram import Client 
from source.info import (joinch)
from source.Data import (get_userbot)
from pyrogram import enums

lisetanme = []  
@Client.on_message(filters.command(["صور انمي", "صورة انمي", "صوره انمي", "انمي"], ""))
async def sssora(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(lisetanme) == 0:
     user = await get_userbot(client.me.username)
     async for msg in user.get_chat_history("LoreBots7"):
      if msg.media:
        lisetanme.append(msg)
  phot = random.choice(lisetanme)
  photo = f"https://t.me/LoreBots7/{phot.id}"
  await message.reply_photo(photo=photo, caption="**𝑱𝒐𝒊𝒏 ➧ @sourceav .**")

lisethazen = []  
@Client.on_message(filters.command(["المزيد من الصور","صور حزينه"], ""))
async def soorr4(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(lisethazen) == 0:
   user = await get_userbot(client.me.username)
   async for msg in user.get_chat_history("PVVVV"):
      if msg.media:
        lisethazen.append(msg)
  phot = random.choice(lisethazen)
  photo = f"https://t.me/PVVVV/{phot.id}"
  await message.reply_photo(photo=photo, caption="**𝑱𝒐𝒊𝒏 ➧ @sourceav .**")
  
lisetbnat = []
@Client.on_message(filters.command(["صور بنات", "صورة لبنت", "انمي بنات", "بنات","رمزيات بنات"], ""))
async def soora4(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(lisetbnat) == 0:
   user = await get_userbot(client.me.username)	
   async for msg in user.get_chat_history("otsoo3"):
      if msg.media:
        lisetbnat.append(msg)
  phot = random.choice(lisetbnat)
  photo = f"https://t.me/otsoo3/{phot.id}"
  await message.reply_photo(photo=photo, caption="**𝑱𝒐𝒊𝒏 ➧ @sourceav .**") 

listsoer = []  
@Client.on_message(filters.command(["صور", "صوره", "صورة", "رمزيه", "رمزية", "رمزيات"], ""))
async def sssor(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(listsoer) == 0:
   user = await get_userbot(client.me.username)
   async for msg in user.get_chat_history("Picture_elnqyb"):
      if msg.media:
        listsoer.append(msg)
  phot = random.choice(listsoer)
  photo = f"https://t.me/Picture_elnqyb/{phot.id}"
  await message.reply_photo(photo=photo, caption="**𝑱𝒐𝒊𝒏 ➧ @sourceav .**")
  
listmu = []
@Client.on_message(filters.command(["اغاني", "غنيلي", "غ", "اغنيه","اغنية عشوائية"], ""))
async def voece(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(listmu) == 0:
   user = await get_userbot(client.me.username)
   async for msg in user.get_chat_history("ELNQYBMUSIC"):
      if msg.media:
        listmu.append(msg.id)
  audi = random.choice(listmu)
  audio = f"https://t.me/ELNQYBMUSIC/{audi}"
  await message.reply_audio(audio=audio, caption="**𝑱𝒐𝒊𝒏 ➧ @sourceav .**")

listvid = []
@Client.on_message(filters.command(["ستوري","استوري","حلات واتس"], ""))
async def videoo(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(listvid) == 0:
   user = await get_userbot(client.me.username)
   async for msg in user.get_chat_history("videi_semo"):
      if msg.video:
        listvid.append(msg.id)
  id = random.choice(listvid)
  video = f"https://t.me/videi_semo/{id}"
  await message.reply_video(video=video, caption="**𝑱𝒐𝒊𝒏 ➧ @sourceav .**")

listvidquran = []
@Client.on_message(filters.command(["ستوري قران","استوري قران","حلات واتس قران"], ""))
async def qurann(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(listvidquran) == 0:
   user = await get_userbot(client.me.username)
   async for msg in user.get_chat_history("a9li91"):
      if msg.video:
        listvidquran.append(msg.id)
  id = random.choice(listvidquran)
  video = f"https://t.me/a9li91/{id}"
  await message.reply_video(video=video, caption="**𝑱𝒐𝒊𝒏 ➧ @sourceav .**")
  
listmuqurannn = []
@Client.on_message(filters.command(["ق", "قران", "قران كريم", "سوره"], ""))
async def qurann2(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(listmuqurannn) == 0:
   user = await get_userbot(client.me.username)
   async for msg in user.get_chat_history("alkoraan4000"):
      if msg.media:
        listmuqurannn.append(msg.id)
  audi = random.choice(listmuqurannn)
  audio = f"https://t.me/alkoraan4000/{audi}"
  await message.reply_audio(audio=audio, caption="**𝑱𝒐𝒊𝒏 ➧ @sourceav .**")