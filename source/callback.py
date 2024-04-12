from pyrogram import filters, Client 
from config import OWNER_NAME, GROUP, OWNER
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from source.Data import get_dev, get_group, get_channel, get_dev_name


@Client.on_callback_query(filters.regex("arbic"))
async def arbic(client: Client, query: CallbackQuery):
    bot = client.me
    ch = await get_channel(bot.username)
    gr = await get_group(bot.username)
    dev = await get_dev(bot.username)
    devname = await get_dev_name(client, bot.username)
    await query.answer("القائمة الرئيسية")
    await query.edit_message_text(f"**مرحبا عزيزي : {query.from_user.mention}.\n\nانا بوت تشغيل موسيقى صوتية ومرئية.\nقم بإضافة البوت إلي مجموعتك او قناتك.\nسيتم تفعيل البوت وانضمام المساعد تلقائياً.\nاستخدم الازرار لمعرفه اوامر الاستخدام.**",
        reply_markup=InlineKeyboardMarkup([
[InlineKeyboardButton("صاحب السورس 🧑‍✈️", url=f"https://t.me/TR_E2S_ON_MY_MOoN")],
[InlineKeyboardButton("طريقة التشغيل 🧠", callback_data="bcmds"),InlineKeyboardButton("طريقة التفعيل 🦸", callback_data="bhowtouse")],
[InlineKeyboardButton("جروب البوت 🤖", url=f"https://t.me/va_source"),InlineKeyboardButton("قناه التحديثات 🐉", url=f"https://t.me/sourceav")],
[InlineKeyboardButton(f"{devname}", user_id=f"{dev}")],
[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك ⚡",url=f"https://t.me/{bot.username}?startgroup=true")],]),disable_web_page_preview=True)

@Client.on_callback_query(filters.regex("english"))
async def english(client: Client, query: CallbackQuery):
    bot = client.me
    ch = await get_channel(bot.username)
    gr = await get_group(bot.username)
    dev = await get_dev(bot.username)
    devname = await get_dev_name(client, bot.username)
    await query.answer("Home Start")
    await query.edit_message_text(
    f"""ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍụѕɪᴄ ʙᴏᴛ
ᴘʟᴀʏᴇᴅ ᴍụѕɪᴄ ᴀɴᴅ ᴠɪᴅᴇᴏ ɪɴ ᴠᴄ
ʙᴏᴛ ᴏɴʟɪɴᴇ ɴᴏᴡ 
ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏụʀ ᴄʜᴀᴛ
ᴘᴏᴡᴇʀᴇᴅ ʙʏ [{OWNER_NAME}]""",

        reply_markup=InlineKeyboardMarkup([
[InlineKeyboardButton("The owner of the source 🧑‍✈️", url=f"https://t.me/TR_E2S_ON_MY_MOoN")],
[InlineKeyboardButton("Operation method 🧠", callback_data="cbcmds"),InlineKeyboardButton("Activation method 🦸", callback_data="cbhowtouse")],
[InlineKeyboardButton("Bot Group 🤖", url=f"https://t.me/va_source"),InlineKeyboardButton("Channel Updates 🐉", url=f"https://t.me/sourceav")],
[InlineKeyboardButton(f"{devname}", user_id=f"{dev}")],
[InlineKeyboardButton("Add the bot to your group or channel ⚡",url=f"https://t.me/{bot.username}?startgroup=true")],]),disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""⌯ **ʙᴀѕɪᴄ ɢụɪᴅᴇ ғᴏʀ ụѕɪɴɢ ᴛʜɪѕ ʙᴏᴛ:**
1.) ғɪʀѕᴛ, ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏụʀ ɢʀᴏụᴘ.
2.) ᴛʜᴇɴ, ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀѕ ᴀᴅᴍɪɴɪѕᴛʀᴀᴛᴏʀ ᴀɴᴅ ɢɪᴠᴇ ᴀʟʟ ᴘᴇʀᴍɪѕѕɪᴏɴѕ ᴇхᴄᴇᴘᴛ ᴀɴᴏɴʏᴍᴏụѕ ᴀᴅᴍɪɴ.
3.) ᴀғᴛᴇʀ ᴘʀᴏᴍᴏᴛɪɴɢ ᴍᴇ, ᴛʏᴘᴇ /ʀᴇʟᴏᴀᴅ ɪɴ ɢʀᴏụᴘ ᴛᴏ ʀᴇғʀᴇѕʜ ᴛʜᴇ ᴀᴅᴍɪɴ ᴅᴀᴛᴀ.
3.) ᴀᴅᴅ ᴀѕѕɪѕᴛᴀɴᴛ ᴛᴏ ʏᴏụʀ ɢʀᴏụᴘ ᴏʀ ɪɴᴠɪᴛᴇ ʜᴇʀ.
4.) ᴛụʀɴ ᴏɴ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ғɪʀѕᴛ ʙᴇғᴏʀᴇ ѕᴛᴀʀᴛ ᴛᴏ ᴘʟᴀʏ ᴠɪᴅᴇᴏ/ᴍụѕɪᴄ.
5.) ѕᴏᴍᴇᴛɪᴍᴇѕ, ʀᴇʟᴏᴀᴅɪɴɢ ᴛʜᴇ ʙᴏᴛ ʙʏ ụѕɪɴɢ /ʀᴇʟᴏᴀᴅ ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʜᴇʟᴘ ʏᴏụ ᴛᴏ ғɪх ѕᴏᴍᴇ ᴘʀᴏʙʟᴇᴍ.
📌 ɪғ ᴛʜᴇ ụѕᴇʀʙᴏᴛ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ, ᴍᴀᴋᴇ ѕụʀᴇ ɪғ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴀʟʀᴇᴀᴅʏ ᴛụʀɴᴇᴅ ᴏɴ.
💡 ɪғ ʏᴏụ ʜᴀᴠᴇ ᴀ ғᴏʟʟᴏᴡ-ụᴘ ǫụᴇѕᴛɪᴏɴѕ ᴀʙᴏụᴛ ᴛʜɪѕ ʙᴏᴛ, ʏᴏụ ᴄᴀɴ ᴛᴇʟʟ ɪᴛ ᴏɴ ᴍʏ ѕụᴘᴘᴏʀᴛ ᴄʜᴀᴛ ʜᴇʀᴇ: @va_source
⋮ __ ᴅᴇᴠᴇʟᴏᴘᴇʀ ʙʏ [{OWNER_NAME}]""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ", callback_data="english")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨ **ʜᴇʟʟᴏ [{query.message.from_user.first_name}](tg://user?id={query.message.from_user.id}) !**
» ᴘʀᴇѕѕ ᴛʜᴇ ʙụᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ʀᴇᴀᴅ ᴛʜᴇ ᴇхᴘʟᴀɴᴀᴛɪᴏɴ ᴀɴᴅ ѕᴇᴇ ᴛʜᴇ ʟɪѕᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅѕ !
⋮ __ᴘᴏᴡᴇʀᴇᴅ ʙʏ [{OWNER_NAME}] A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴀᴅᴍɪɴ ᴄᴍᴅ", callback_data="cbadmin"),
                    InlineKeyboardButton("ʙɪѕᴄ ᴄᴍᴅ", callback_data="cbbasic"),
                ],[
                    InlineKeyboardButton("ѕụᴅᴏ ᴄᴍᴅ", callback_data="cbsudo")
                ],[
                    InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ", callback_data="english")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""⋮ ʜᴇʀᴇ ɪѕ ᴛʜᴇ ʙᴀѕɪᴄ ᴄᴏᴍᴍᴀɴᴅѕ:
» /play (ѕᴏɴɢ ɴᴀᴍᴇ/ʟɪɴᴋ) - ᴘʟᴀʏ ᴍụѕɪᴄ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ
» /vplay (ᴠɪᴅᴇᴏ ɴᴀᴍᴇ/ʟɪɴᴋ) - ᴘʟᴀʏ ᴠɪᴅᴇᴏ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ
» /video (ǫụᴇʀʏ) - ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴏụᴛụʙᴇ
» /song (ǫụᴇʀʏ) - ᴅᴏᴡɴʟᴏᴀᴅ ѕᴏɴɢ ғʀᴏᴍ ʏᴏụᴛụʙᴇ
» /searq (ǫụᴇʀʏ) - ѕᴇᴀʀᴄʜ ᴀ ʏᴏụᴛụʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ
» /ping - ѕʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴘɪɴɢ ѕᴛᴀᴛụѕ
» /alive - ѕʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴀʟɪᴠᴇ ɪɴғᴏ (ɪɴ ɢʀᴏụᴘ)
◖⋮◗ __ ᴅᴇᴠᴇʟᴏᴘᴇʀ ʙʏ  [{OWNER_NAME}]""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""⋮ ʜᴇʀᴇ ɪѕ ᴛʜᴇ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅѕ:
» /pause - ᴘᴀụѕᴇ ᴛʜᴇ ѕᴛʀᴇᴀᴍ
» /resumres - ʀᴇѕụᴍᴇ ᴛʜᴇ ѕᴛʀᴇᴀᴍ
» /skip - ѕᴡɪᴛᴄʜ ᴛᴏ ɴᴇхᴛ ѕᴛʀᴇᴀᴍ
» /stop - ѕᴛᴏᴘ ᴛʜᴇ ѕᴛʀᴇᴀᴍɪɴɢ
» /loob - ʟᴏᴏᴘ ᴛʜᴇ ѕᴛʀᴇᴀᴍɪɴɢ
◖⋮◗ __ ᴅᴇᴠᴇʟᴏᴘᴇʀ ʙʏ  [{OWNER_NAME}]""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("SUDO COMMANDS")
    await query.edit_message_text(
        f"""⋮ here is the sudo commands:
» • تعين اسم البوت • : لتعين اسم جديد للبوت 
» • الاحصائيات • : لمعرفه احصائيات البوت
» • المجموعات • : لعرض قائمه المجموعات 
» • المستخدمين • : لعرض قائمه المستخدمين 
» • قسم الاذاعه • : لعرض قسم التحكمف الاذاعه والتوجيه
» • قسم التحكم في الحساب المساعد • : لعرض قائمه التحكم ف الحساب المساعد
» • تفعيل سجل التشغيل • : لتفعيل سجل التشغيل ف المجموعه 
» • تعطيل سجل التشغيل • : لتعطيل سجل التشغيل ف المجموعه
» • تغير مكان سجل التشغيل • : لتغير مجموعة السجل
⋮ __ Developer by  [{OWNER_NAME}]""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("bhowtouse"))
async def acbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" **طريقة تفعيل البوت في مجموعتك ⋮♥️:**
1.) **اولا قم بإضافة البوت اللي مجموعتك ⋮.**
2.) **قم بترقيى البوت مشرف مع الصلاحيات المطلوبة ⋮.**
3.) ** لتحديث قائمة الادمن /Reload قم بكتابة الامر ⋮.**
3.) ** قم بإضافة الحساب المساعد اللي المجموعة ⋮.**
4.) **تاكد كن تشغيل المحادثة المرئية ⋮.**
5.) **لتحديث قائمة الادمنيه /Reload اذا واجهت خطأ قم بكتابة الامر ⋮.**
📌 ** اذا لم يستطع الحساب المساعد الانضمام اللي المحادثة المرئيه قم بإعادة تشغيل المحادثه ⋮.**
💡 **في حال واجهت اي مشكلة اخري يمكنك التواصل مع المطور من هن : {GROUP} **
⋮ __ Developer by  [{OWNER_NAME}]""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="arbic")]]
        ),
    )


@Client.on_callback_query(filters.regex("bcmds"))
async def acbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" **Hello [{query.message.from_user.first_name}](tg://user?id={query.message.from_user.id}) !**
» **اتبع الازرار بالاسفل لمعرفة طريقة التشغيل ⋮**
⋮ __ Developer by  [{OWNER_NAME}]""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("اوامر التشغيل", callback_data="bbasic"),
                    InlineKeyboardButton("اوامر الادمن", callback_data="badmin"),
                ],[
                    InlineKeyboardButton("اوامر المطورين", callback_data="bsudo")
                ],[
                    InlineKeyboardButton("العودة", callback_data="arbic")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("bbasic"))
async def acbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""اوامر التشغيل ⋮:
» شغل او تشغيل - لتشغيل الموسيقى  
» فيد او فيديو  - لتشغيل مقطع فيديو 
» تشغيل عشوائي  - لتشغيل اغنيه عشوائية 
» بحث - للبحث عن نتائج في اليوتيوب
» حمل + اسم الفيديو - لتحميل مقطع فيديو
» نزل + اسم الاغنيه - لتحميل ملف صوتي 
» بنج - عرض سرعة الاستجابة
» سورس - لعرض معلومات البوت 
◖⋮◗ __ Developer by  [{OWNER_NAME}]""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="bcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("badmin"))
async def acbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""اوامر التحكم للخاصة بالادمنية:
» ايقاف مؤقت - ايقاف التشغيل موقتأ
» استكمال - لاستكمال التشغيل
» تخطي - لتخطي تشغيل الحالي
» ايقاف او اسكت - لايقاف تشغيل الحالي 
» تكرار او كررها - لتكرار التشغيل الحالي
◖⋮◗ __ Developer by  [{OWNER_NAME}]""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="bcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("bsudo"))
async def sudo_set(client: Client, query: CallbackQuery):
    await query.answer(" اوامر المطورين")
    await query.edit_message_text(
        f"""✏ اوامر المطورين.
» • تعين اسم البوت • : لتعين اسم جديد للبوت 
» • الاحصائيات • : لمعرفه احصائيات البوت
» • المجموعات • : لعرض قائمه المجموعات 
» • المستخدمين • : لعرض قائمه المستخدمين 
» • قسم الاذاعه • : لعرض قسم التحكمف الاذاعه والتوجيه
» • قسم التحكم في الحساب المساعد • : لعرض قائمه التحكم ف الحساب المساعد
» • تفعيل سجل التشغيل • : لتفعيل سجل التشغيل ف المجموعه 
» • تعطيل سجل التشغيل • : لتعطيل سجل التشغيل ف المجموعه
» • تغير مكان سجل التشغيل • : لتغير مجموعة السجل 

⋮ __ Developer by  [{OWNER_NAME}]""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="bcmds")]]
        ),
    )
