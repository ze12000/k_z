from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions


@Client.on_message(filters.command(["رفع مشرف"]) & filters.group)
async def promote(client: Client, message: Message):
    chat_id = message.chat.id
    user = message.from_user
    if await client.get_chat_member(chat_id, user.id):
        await message.reply("من فضلك، قم بإرسال إيدي المستخدم أو يوزره الخاص به.")
        response = await client.listen(filters=message.from_user)
        if response.text:
            user_id = response.text.strip()
            try:
                user_id = int(user_id)
            except ValueError:
                user_info = await client.get_users(user_id)
                if user_info:
                    user_id = user_info.id
            await client.promote_chat_member(chat_id, user_id, ChatPermissions(
                can_change_info=False,
                can_post_messages=True,
                can_edit_messages=True,
                can_delete_messages=True,
                can_invite_users=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=False,
                can_manage_chat=False
            ))

            await message.reply(f"تم رفع المشرف بنجاح: {user_id}")
    else:
        await message.reply("عذرًا، هذا الأمر مخصص للمشرفين فقط ولا يمكن للمستخدمين العاديين استخدامه لرفع مشرفين.")