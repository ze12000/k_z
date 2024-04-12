from pyrogram import Client, filters, idle
from config import OWNER
from source.Data import (get_dev, get_userbot)
from pyrogram.types import ReplyKeyboardMarkup

@Client.on_message(filters.command("قسم التفعيل والتعطيل", ""))
async def helpercn(client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   userbot = await get_userbot(bot_username)
   me = userbot.me
   if message.chat.id == dev or message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([
["تعطيل التواصل","تفعيل التواصل"],
["تعطيل سجل التشغيل","تفعيل سجل التشغيل"],
["تفعيل اشعار الاذان","تعطيل اشعار الاذان"],
["تعطيل الاشتراك","تفعيل الاشتراك"],
["رجوع للقائمة الرئيسيه"]], resize_keyboard=True)
    await message.reply_text(f"**مرحبا بك في قسم ⟨ التفعيل والتعطيل ⟩ 🚦 .**", reply_markup=kep,quote=True)

@Client.on_message(filters.command(["قسم التعيين"], ""))
async def cast(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.id == dev or message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([
["تعين اسم البوت"],
["تعين قناة البوت","تعين مجموعة البوت"],
["تعين قناة السورس","تعين مجموعة السورس"],
["تعين لوجو السورس","تعين يوزر مطور السورس"], 
["رجوع للقائمة الرئيسيه"]], resize_keyboard=True)
    await message.reply_text("**مرحبا بك في قسم ⟨ التعيين ⟩ ⚡ .**", reply_markup=kep)

@Client.on_message(filters.command("قسم البوت", ""))
async def A_q_lp(client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  chat = message.chat.id
  uesr = message.chat.username
  if chat == dev or uesr in OWNER:
    kep = ReplyKeyboardMarkup([
["الاحصائيات","المكالمات النشطه"],
["المجموعات","المستخدمين"],
["تغير مكان سجل التشغيل"],
["رجوع للقائمة الرئيسيه"]], resize_keyboard=True)
    await message.reply_text(f"**مرحبا بك في قسم ⟨ البوت ⟩ .**", reply_markup=kep,quote=True)