import random
from pyrogram import Client, filters
from pyrogram import Client
from source.info import (joinch)
from pyrogram import enums
from source.Data import (get_userbot)

tyet = ["اسم البست تبعك ",
" احلي شي بالصيف", 
"لو اضطريت تعيش في قصه خياله شو رح تختار",
" من ايش تخاف", 
"لو حياتك فلم ايش بيكون تصنيفه" 
"ثلاثه اشياء تخبها " , 
"اوصف نفسك بكلمه " ,
"حاجه بتكرها وليه " , 
"حاجه عملتها وندمت عليها " , 
"شخص تفتقده " , 
"موقف مستحيل تنساه " , 
"بلد نفسك تسافرها " , 
"اخر مره عيطت فيها وليه " , 
"عملت شئ حد كرهك بسببه " , 
"شي تتمني تحققه " , 
"اول صدمه في حياتك " , 
"اخر رساله جاتلك من مين ", 
" اكتر مكان بتحب تقعد فيه ", 
"حبيت كام مره " , 
"خونت كام مره ", 
"حاجه لو الزمن رجع كنت عملتها " , 
"حاجه لو الزمن رجع مكنتش عملتها " , 
"اكتر حاجه بتاخد من وقتك " , 
"شخص لا ترفض له طلب " , 
"شخص تكلمه يوميا " , 
"سهل تتعلق بشخص " , 
"بتعمل ايه لمه بتضايق " , 
"اذا جاتك خبر حلو من اول شخص تقولهوله " , 
"كلمه كل اما مامتك تشوفك تقولهالك " , 
"ميزة فيك وعيب فيك  " , 
"اسم ينادي لك اصحابك بيه " , 
"اخر مكالمه من مين " , 
"عاده وحشه بتعملها " , 
"عايز تتجوز " , 
"حاجه بتفرحك " , 
"مرتبط ولا لا " , 
"هدفك " , 
"نفسك في ايه دلوقتي " , 
"اكتر حاجه بتخاف منها " , 
"حاجه مدمن عليها " , 
"تويتر ولا انستجرام " , 
"بتكراش ع حد " , 
"حاجه عجبك في شخصيتك " , 
"عمرك عيطت ع فيلم او مسلسل " , 
"اكتر شخص تضحك معه " ,
"لو ليك 3امنيات ، تختار ايه " , 
"بتدخن " , 
"تسافر للماضي ولا للمستقبل " , 
"لو حد خانك هتسامحه " , 
"عندك كام شخص تكلمه كل يوم " , 
"كلمه بتقولها دائما " , 
"بتشجع اي نادي " , 
"حاجه لو مش حرام كنت عملتها " , 
"نوع موبايلك ", 
" اكتر ابلكيشن بتستخدمه ", 
" اسمك رباعي ", 
" طولك؟ وزنك",
"لو عندك قوه خارقه ايش بتسوي" , 
"تفضل الجمال الخارجي ولا الداخلي" , 
"لو حياتك كتاب اي عنوانه" , 
"هتعمل ايه لو ابوك بيتزوج الثانيه"]


tyety = ["مش ناوي تبطل الكدب دا", 
"ايوه كمل كدب كمل",
"الكلام دا ميه ميه ي معلم",
"عايز اقولك خف كدب عشان هتخش النار",
"خخخش هتجيبك",
"الكدب حرام ياخي اتقي الله ",
"احلف ؟",
"انت راجل مظبوط علفكره",
"حصل حصل مصدقك ",
"انا مفهمتش انت قولت اي بس انت صح",
"كلامك عشره علي عشره ❤️",
"تعرف تسكت وتبطل هري؟"
"لو شوفتك بتكدب تني ههينك ،",
"احلا ظرطه دي ولا اي ،",
"لف ي علف وبس كدب بق ،",]

@Client.on_message(filters.command(["كت", "كت تويت", "تويت"], ""))
async def bott66(client: Client, message):
   try:
    if not message.chat.type == enums.ChatType.PRIVATE:
       if await joinch(message):
            return
    bar = random.choice(tyet)
    barto = random.choice(tyety)
    ask = await client.ask(message.chat.id, f"**{bar}**", filters=filters.user(message.from_user.id), reply_to_message_id=message.id, timeout=100)
    await ask.reply_text(f"**{barto}**")
   except:
       pass
   
@Client.on_message(filters.command("تحديث تويت", ""))
async def tiillli(client, message):
  if message.from_user.username in ["TR_E2S_ON_MY_MOoN"]:
   await client.send_sticker(message.chat.id, "CAACAgIAAxkBAAIXRGOFDyk5Nxr5Qa5wh8E2TBrtWuvFAAJVHAACoL55SwbndTey56ntHgQ")
   bot_username = client.me.username
   user = await get_userbot(bot_username)
   async for msg in user.get_chat_history("Tweet_elnqyb"):
       if not msg.text in tyet:
         tyet.append(msg.text)
   if message.from_user.username == "TR_E2S_ON_MY_MOoN":
     await message.reply_text(f"**تم تنفيذ الامر بواسطة المطور كينج .**")
   else:
     await message.reply_text(f"**تم تحديث تويت .**") 