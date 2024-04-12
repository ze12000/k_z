from pyrogram import Client, filters, idle
from source.info import (del_served_chat, is_served_chat, add_served_chat, get_served_chats)
from source.Data import (get_dev, get_groupsr)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@Client.on_message(~filters.private)
async def booot(client: Client, message: Message):
    chat_id = message.chat.id
    if not await is_served_chat(client, chat_id):
       try:
        await add_served_chat(client, chat_id)
        chats = len(await get_served_chats(client))
        bot_username = client.me.username
        dev = await get_dev(bot_username)
        gr = await get_groupsr(client.me.username)
        username = f"https://t.me/{message.chat.username}" if message.chat.username else None
        mention = message.from_user.mention if message.from_user else message.chat.title
        await client.send_message(dev, f"**تم تفعيل محادثة جديدة تلقائياً واصبحت {chats} محادثة**\nNew Group : [{message.chat.title}]({username})\nId : {message.chat.id} \nBy : {mention}", disable_web_page_preview=True)
        A_q_lp = InlineKeyboardMarkup([[InlineKeyboardButton("قناة البوت .", url="t.me/"+gr)]])
        await client.send_message(chat_id,f"**تم تفعيل البوت تلقائيا .**",reply_markup=A_q_lp)
        return 
       except:
          pass
    message.continue_propagation()

@Client.on_message(filters.left_chat_member)
async def bot_kicked(client: Client, message):
    bot = client.me
    bot_username = bot.username
    if message.left_chat_member.id == bot.id:
         logger = await get_dev(bot_username)
         chat_id = message.chat.id
         await client.send_message(logger, f"**Bot Is Kicked**\n**{message.chat.title}**\n**Id : `{message.chat.id}`**\n**By :** {message.from_user.mention}")
         return await del_served_chat(client, chat_id)