from pyrogram import Client, filters
from pyrogram import Client, filters 
from pytgcalls import StreamType
from pytgcalls.exceptions import (AlreadyJoinedError,NoActiveGroupCall,TelegramServerError)
from pytgcalls.types.input_stream import AudioPiped
from source.Data import (get_userbot, get_call)
import asyncio

@Client.on_message(filters.regex("^مين في الكول$|^مين ف الكول$|^مين في كول$"))
async def sttrcall(client, message):
    calll = await get_call(client.me.username)
    user = await get_userbot(client.me.username)
    try:
        await calll.join_group_call(message.chat.id, AudioPiped("./source/whocall.mp3"), stream_type=StreamType().pulse_stream)
        
        text = "📞 الأعضاء المتواجدين في المكالمة 📞\n\n"
        
        participants = await calll.get_participants(message.chat.id)
        k = 0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut = " يتحدث •"
            else:
                mut = " صامت •" 
            user = await client.get_users(participant.user_id)
            print(participant.user_id)
            k += 1
            text += f"👤 {k}»» {user.mention} - {mut}\n"        
        await message.reply(f"📋 {text}")       
        await asyncio.sleep(5)
        await calll.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply("❌ عذرًا، المكالمة غير مفتوحة حاليًا.")
    except AlreadyJoinedError:
        await message.reply("🔄 برجاء كتابة ريلود أو استخدام الأمر /reload.")
    except TelegramServerError:
        await message.reply("❗ حدثت مشكلة، من فضلك حاول مرة أخرى.")