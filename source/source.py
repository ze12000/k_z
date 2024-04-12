from pyrogram import Client, filters
from pyrogram import Client 
from config import OWNER_NAME
from source.info import (joinch)
from source.Data import (get_dev, get_groupsr, get_channelsr, get_dev_user ,get_dev_name)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

import os


@Client.on_message(
    filters.command(["/alive", "معلومات", "سورس", "السورس", "• السورس •"], "")
)
async def alive(client: Client, message):
    chat_id = message.chat.id
    bot_username = client.me.username
    dev = await get_dev(bot_username)
    nn = await get_dev_name(client, bot_username)
    DEV_USER = await get_dev_user(bot_username)
    user = await client.get_chat(chat_id=DEV_USER)
    ch = await get_channelsr(client.me.username)
    gr = await get_groupsr(client.me.username)
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝐠𝐫𝐨𝐮𝐩", url=f"{gr}"),
                InlineKeyboardButton("𝐜𝐡𝐧𝐧𝐞𝐥", url=f"{ch}"),
            ],
            [
                 InlineKeyboardButton(f"{nn}", url=f"https://t.me/{DEV_USER}")
            ],
            [ 
                 InlineKeyboardButton("اضف البوت الي مجموعتك 💎", url="https://t.me/{app.username}?startgroup=true")
            ]
        ]
    )

    alive = f"""╭──── • ◈ • ────╮
么 [𝑫𝒆𝒗 𝒔𝒐𝒖𝒓𝒄𝒆](https://t.me/{DEV_USER}).
么 [𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝒔𝒐𝒖𝒓𝒄𝒆]({ch}).
么 [𝑮𝒓𝒐𝒖𝒑 𝒔𝒐𝒖𝒓𝒄𝒆]({gr}).
╰──── • ◈ • ────╯
🚦𝑻𝒉𝒆 𝒃𝒆𝒔𝒕 𝒔𝒐𝒖𝒓𝒄𝒆 𝒕𝒆𝒍𝒆𝒈𝒓𝒂𝒎 ."""

    await message.reply_photo(
        photo=f"https://telegra.ph/file/4fda78aaf200bf313be62.jpg",
        caption=alive,
        reply_markup=keyboard,
    )

@Client.on_message(filters.command(["المطور كينج","كينج","المبرمج كينج"], ""))
async def deev(client: Client, message: Message):
     if await joinch(message):
            return
     user = await client.get_chat(chat_id="TR_E2S_ON_MY_MOoN")
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
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور**\n{chat_title}\nChat Id : `{message.chat.id}`",
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

@Client.on_message(filters.command(["المطور زين","زين","المبرمج زين"], ""))
async def deev(client: Client, message: Message):
     if await joinch(message):
            return
     user = await client.get_chat(chat_id="L_HLN")
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
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور**\n{chat_title}\nChat Id : `{message.chat.id}`",
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
