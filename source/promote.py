import json
from pyrogram import Client, filters
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums
import json
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ChatPrivileges, InputMediaPhoto
from pyrogram.errors.exceptions import ChatAdminRequired
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus , ChatType
from pyrogram import Client, filters
import json
import os

admin_groups = "admins_groups_rights.json"
admin_channels = "admins_channels_rights.json"
def get_admins_rights(user_id, chat_id,type):
    if type == "group":
        try:
            with open(admin_groups, "r") as file:
                settings = json.load(file)
                admin_rights = settings.get(str(chat_id))[str(user_id)]
                del admin_rights["_client"]
                if admin_rights:
                    privileges = ChatPrivileges(**admin_rights)
                    return privileges
                    
        except FileNotFoundError:
            pass
    
        return ChatPrivileges(
                can_promote_members=False,
                can_manage_video_chats=True,
                can_restrict_members=False,
                can_change_info=False,
                can_invite_users=True,
                can_delete_messages=True,
                can_pin_messages=True
            )
    else:
        try:
            with open(admin_channels, "r") as file:
                settings = json.load(file)
                admin_rights = settings.get(str(chat_id))[str(user_id)]
                del admin_rights["_client"]
                if admin_rights:
                    privileges = ChatPrivileges(**admin_rights)
                    return privileges
                    
        except FileNotFoundError:
            pass
    
        return ChatPrivileges(
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_promote_members=False,
                    can_change_info=False,
                    can_post_messages=True,
                    can_edit_messages=True,
                    can_invite_users=True)
                    
def save_admins_rights(user_id, chat_id,privileges, type):
    if type == "group":
        file_name = admin_groups
    else:
        file_name = admin_channels
    try:
        with open(file_name, "r") as file:
            settings = json.load(file)
    except FileNotFoundError:
        settings = {}

    settings[str(chat_id)] = {str(user_id): privileges.__dict__}
    
    with open(file_name, "w") as file:
        json.dump(settings, file, indent=2)
        
        
@app.on_message(filters.command("رفع مشرف", ""))
@app.on_edited_message(filters.command("رفع مشرف", ""))
async def promote_admin(client: Client, message: Message):
        global message_type
        message_type = (True if message.chat.type != ChatType.CHANNEL else False)
        if (message_type and not TOM(client, message, message) and not OWNER_ID(client, message, message) and not basic_dev(client, message, message) and not dev(client, message, message) and not owner(client, message, message) and not is_basic_creator(client, message, message) and not creator(client, message, message)):
            message.reply_text("""◍ يجب ان تكون منشئ على الاقل لكى تستطيع استخدام الأمر
√""")
            return
        
        global full_info, user_id , chat_id, member_id, message_text, chat_type
        message_text = message.text

        chat_id = message.chat.id
        bot_info = await client.get_me()
        bot_id = bot_info.id
        
        if message.reply_to_message:
            full_info = message.reply_to_message.from_user
            user_id = message.reply_to_message.from_user.id
        
        elif message_text.split()[-1].startswith("@"):
            username = message.text.split("@")[1]
            full_info = await client.get_chat(username)
            user_id = full_info.id
        
        elif int(message_text.split(" ")[-1]):
            user_id = int(message_text.split(" ")[-1])
            
        
        user = await app.get_chat_member(chat_id, user_id)
        global user_status
        user_status = user.status
        
        bot = await app.get_chat_member(chat_id, bot_id)
        bot_status = bot.status
        
        global chat_privileges
        if message_type:
            chat_type = "group"
            chat_privileges = get_admins_rights(user_id, chat_id, chat_type)
        else:
            chat_type = "channel"
            chat_privileges = get_admins_rights(user_id, chat_id, chat_type)
        
        if chat_privileges is None:
            if message_type:
                chat_privileges = ChatPrivileges(
                    can_promote_members=False,
                    can_manage_video_chats=True,
                    can_restrict_members=False,
                    can_change_info=False,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_pin_messages=True
                )
            else:
                chat_privileges= ChatPrivileges(
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_promote_members=False,
                    can_change_info=False,
                    can_post_messages=True,
                    can_edit_messages=True,
                    can_invite_users=True
                )
                
        admin_keys = InlineKeyboardMarkup([
                [InlineKeyboardButton("تعديل الصلاحيات", callback_data="edit-privileges")],
                [InlineKeyboardButton("معلومات الأدمن", callback_data="admin-info-privileges")]
                ])
        if message_type:
            
            member_id = message.from_user.id
            member = await app.get_chat_member(chat_id, member_id)
            member_status = member.status
            if bot_status == ChatMemberStatus.ADMINISTRATOR:
                try:
                        if user_status == ChatMemberStatus.OWNER:
                            await message.reply_text(
                                    "لا يمكنك التحكم  بمالك المجموعه ✨️",
                                    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("معلومات المالك", callback_data="admin-info-privileges")]])
                                )
                        elif user_status == ChatMemberStatus.ADMINISTRATOR:
                            await message.reply_text(
                                    "هذا العضو بالفعل ادمن ✨️",
                                    reply_markup = admin_keys)
                        
                        elif user_status == ChatMemberStatus.MEMBER:
                            await client.promote_chat_member(chat_id, user_id, chat_privileges)
                            global done_msg
                            done_msg = await message.reply_text(
                                    "تم رفع العضو لرتبة ادمن ✅️", 
                            reply_markup=admin_keys )
                                      
                except ChatAdminRequired:
                    await message.reply_text("ليس لدي صلاحيه الوصول للأدمنيه✨️")
            else:
                await message.reply_text("ارفع البوت ادمن أولا ليتمكن من التحكم بقائمة الأدمنيه✨️")
        else:
            if user_status == ChatMemberStatus.ADMINISTRATOR:
                save_admins_rights(user_id, chat_id, chat_privileges, chat_type)
                await message.reply_text(
                    "هذا العضو بالفعل ادمن ✨️",
                    reply_markup = admin_keys)
                        
            elif user_status == ChatMemberStatus.MEMBER:
                await client.promote_chat_member(chat_id, user_id, chat_privileges)
                save_admins_rights(user_id, chat_id, chat_privileges, chat_type)
                done_msg = await message.reply_text(
                    "تم رفع العضو لرتبة ادمن ✅️", 
                    reply_markup=admin_keys )

@app.on_callback_query(filters.regex("privileges"))
async def handle_callback_query(client: Client, callback_query):

    chat_id = callback_query.message.chat.id
    callback_data_user = callback_query.from_user.id
    data = callback_query.data
    
    if callback_data_user == member_id:
        if data == "edit-privileges":
            global privileges
            if message_type:
                privileges = [
                    ("إضافة أدمنيه", "can_promote_members"),
                    ("التحكم في المحدثه الصوتيه", "can_manage_video_chats"),
                    ("حظر الأعضاء", "can_restrict_members"),
                    ("تغيير معلومات المجموعه", "can_change_info"),
                    ("إضافة أعضاء", "can_invite_users"),
                    ("مسح الرسائل", "can_delete_messages"),
                    ("تثبيت الرسائل", "can_pin_messages")
                ]
            else:
              privileges = [
                    ("حذف الرسائل " ,"can_delete_messages"),
                    ("التحكم في المحادثه الصوتيه ","can_manage_video_chats"),
                    ("اضافة ادمنيه " ,"can_promote_members"),
                    ("تغيير معلومات القناه " ,"can_change_info"),
                    ("النشر بالقناه " ,"can_post_messages"),
                    ("تعديل الرسائل " ,"can_edit_messages"),
                    ("إضافة اعضاء " ,"can_invite_users")
              ]           
             
            keyboard = []
            for privilege in privileges:
                privilege_name, privilege_key = privilege
                button_text = privilege_name + " ✅" if getattr(chat_privileges, privilege_key) else privilege_name + " ❌"
                boolean = "-True" if getattr(chat_privileges, privilege_key) else "-False"
                keyboard.append([InlineKeyboardButton(button_text, callback_data=f"{privilege_key}{boolean}-privileges")])
            
            keyboard.append([InlineKeyboardButton("إغلاق 🚶", callback_data="privileges-save")])
            
            reply_markup = InlineKeyboardMarkup(keyboard)
            global edit_rights
            edit_rights =  await callback_query.edit_message_text("قم بإختيار الصلاحيات المطلوبه : ", reply_markup=reply_markup)
            
        elif data.split("-")[1] in ["True", "False"]:
            
            privilege_key, privilege_name = callback_query.data.split("-", 1)
            setattr(chat_privileges, privilege_key , False if privilege_name == "True-privileges" else True)
            await client.promote_chat_member(chat_id, user_id, chat_privileges)
            save_admins_rights(user_id, chat_id, chat_privileges, chat_type)
            
            keyboard = []
            for privilege in privileges:
                privilege_name, privilege_key = privilege
                button_text = privilege_name + " ✅" if getattr(chat_privileges, privilege_key) else privilege_name + " ❌"
                boolean = "-True" if getattr(chat_privileges, privilege_key) else "-False"
                keyboard.append([InlineKeyboardButton(button_text, callback_data=f"{privilege_key}{boolean}-privileges")])
                
            keyboard.append([InlineKeyboardButton("إغلاق 🚶", callback_data="privileges-save")])
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await callback_query.edit_message_text(
                text="قم بإختيار الصلاحيات المطلوبه : ",
                reply_markup=reply_markup
            )
        
        elif data == "privileges-save":
            save_admins_rights(user_id, chat_id, chat_privileges, chat_type)
            await callback_query.edit_message_text(
                "تم حفظ الصلاحيات يمكنك إعادة تعديلها ✅️",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("تعديل الصلاحيات", callback_data="edit-privileges")],
                    [InlineKeyboardButton("معلومات الأدمن", callback_data="admin-info-privileges")]
                    ]))
       
        elif data == "admin-info-privileges":
            if message_text == "رفع مشرف" or message_text.split()[-1].startswith("@"):
                
                username =  full_info.username
                admin = await client.get_chat(username)
                nickname = admin.first_name
                admin_bio = admin.bio
                folder_path = "downloads"
                file_name = f"{admin.photo.big_file_id}.jpg"
                photo_path = None
            
                if file_name in os.listdir(folder_path):
                    photo_path = os.path.join(folder_path, file_name)
                else:
                    photo_path = await client.download_media(admin.photo.big_file_id, file_name=os.path.join(folder_path, file_name))
                    
                admin_caption =  f"● | Admin name: {nickname}\n\n● | Username : @{username}\n\n● | Bio : [{admin_bio}](https://t.me/{username})\n\n● | ID : {user_id}"
                
                global owner_message
                if callback_query.message.photo:
                    if user_status != ChatMemberStatus.OWNER:
                        await callback_query.edit_message_text(
                            text = admin_caption,
                            reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton("تعديل الصلاحيات", callback_data="edit-privileges")]
                                ]))
                    else:
                        owner_message = await callback_query.edit_message_text(
                            text = admin_caption,
                            reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton("إغلاق 🚶", callback_data="close-admin-window-privileges")
                                ]]))
                else:  
                    if user_status != ChatMemberStatus.OWNER:
                        await client.send_photo(
                            chat_id = chat_id,
                            photo = photo_path, 
                            caption = admin_caption,
                            reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton("تعديل الصلاحيات", callback_data="edit-privileges")]
                                ]))
                    else:
                        owner_message = await client.send_photo(
                            chat_id = chat_id,
                            photo = photo_path, 
                            caption = admin_caption,
                            reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton("إغلاق 🚶", callback_data="close-admin-window-privileges")
                                ]]))
                    await client.delete_messages(chat_id, callback_query.message.id)
            else:
                await callback_query.edit_message_text(
                        "عذرا هذه الميزه غير متوفره بالأيدي ✨️", 
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("إغلاق 🚶", callback_data="privileges-save")]])) 
        elif data == "close-admin-window-privileges":
            await client.delete_messages(chat_id ,owner_message.id)
    else:
        await client.answer_callback_query(callback_query.id, text="بطل لعب الرساله مش ليك 😒", show_alert=True)


class ChatPermissions:
    def __init__(
        self,all_locked=False,
        chat_locked=False, photo_locked=False,
        video_locked=False, link_locked=False,sticker_locked=False,
        forward_locked=False, reply_locked=False, voice_locked=False
    ):
        self.all_locked = all_locked
        self.chat_locked = chat_locked
        self.photo_locked = photo_locked
        self.video_locked = video_locked
        self.link_locked = link_locked
        self.sticker_locked = sticker_locked
        self.forward_locked = forward_locked
        self.reply_locked = reply_locked
        self.voice_locked = voice_locked

settings_file = "group_settings.json"

def get_group_permissions(chat_id):
    try:
        with open(settings_file, "r") as file:
            settings = json.load(file)
            group_settings = settings.get(str(chat_id))

            if group_settings:
                permissions = ChatPermissions(**group_settings)
                return permissions
    except FileNotFoundError:
        pass

    return ChatPermissions()

def save_group_permissions(chat_id, permissions):
    try:
        with open(settings_file, "r") as file:
            settings = json.load(file)
    except FileNotFoundError:
        settings = {}

    settings[str(chat_id)] = permissions.__dict__

    with open(settings_file, "w") as file:
        json.dump(settings, file, indent=2)

@app.on_message()
@app.on_edited_message()
async def command_buttons(client: Client, message: Message):
  
    global member_status, chat_id
    chat_id = message.chat.id    
    user_id = message.from_user.id
    member = await app.get_chat_member(chat_id, user_id) 
    member_status = member.status
    
    if message.text == "الاوامر":
        if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message)):
            
            await message.reply_text("هذا الأمر يخص المنشئين وما اعلى ❤️✨️")
            
        else:
            global owner_id , chat_permissions
            owner_id = message.from_user.id
            chat_permissions = get_group_permissions(chat_id)
            
            if chat_permissions is None:
                chat_permissions = ChatPermissions()
               
            global permissions
            permissions = [
                ("إغلاق الكل", "all_locked"),
                ("قفل الدردشه", "chat_locked"),
                ("قفل الصور", "photo_locked"),
                ("قفل الفيديوز", "video_locked"),
                ("قفل الصوتيات", 'voice_locked'),
                ("قفل اللينكات", "link_locked"),
                ("قفل الإستيكر", "sticker_locked"),
                ("قفل التحويل", "forward_locked"),
                ("قفل الرد", "reply_locked")
            ]
                    
            keyboard = []
            for permission in permissions:
                permission_name, permission_key = permission
                button_text = permission_name + " ✅" if getattr(chat_permissions, permission_key) else permission_name + " ❌"
                boolean = "-True" if getattr(chat_permissions, permission_key) else "-False"
                keyboard.append([InlineKeyboardButton(button_text, callback_data=f"{permission_key}{boolean}-permissions")])
                    
            keyboard.append([InlineKeyboardButton("إغلاق 🚶", callback_data="permission-save")])
                    
            reply_markup = InlineKeyboardMarkup(keyboard)
            edit_rights = await message.reply_text("قم بإختيار الصلاحيات المطلوبة :", reply_markup=reply_markup)
    
    else:
        if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message) and not admin(client, message, message)):
            
            chat_permissions = get_group_permissions(chat_id)
                
            if chat_permissions.all_locked:
                await message.delete()
                
            elif (
            chat_permissions.chat_locked and message.text and not message.entities and not message.reply_to_message
            ):
                await message.delete()
                    
            elif chat_permissions.photo_locked and message.media == MessageMediaType.PHOTO:
                await message.delete()
                    
            elif (
            chat_permissions.video_locked and
            (message.media == MessageMediaType.VIDEO or message.media == MessageMediaType.ANIMATION)
            ):
                await message.delete()
                    
            elif chat_permissions.sticker_locked and message.media == MessageMediaType.STICKER:
                await message.delete()
                
            elif chat_permissions.link_locked and message.entities:
                await message.delete()
                    
            elif chat_permissions.reply_locked and message.reply_to_message:
                await message.delete()
    
            elif ((chat_permissions.forward_locked and message.forward_from) or
                    (chat_permissions.forward_locked and message.forward_from_chat)):
                await message.delete()
    
            elif chat_permissions.voice_locked and message.media == MessageMediaType.VOICE:
                await message.delete()

@app.on_callback_query(filters.regex("permissions"))
async def handle_callback_query(client: Client, callback_query):
    global callback_data_chat
    callback_data_user = callback_query.from_user.id
    data = callback_query.data
    callback_data_chat = callback_query.message.chat.id
    
    if ((callback_data_user in DEVELOPERS) or
         (basic_dev(client, callback_query,callback_query))or
         (callback_data_user == OWNER_BOT) or
         (dev(client, callback_query,callback_query)) or 
         (is_basic_creator(client, callback_query,callback_query)) or
         (owner(client, callback_query,callback_query)) or
         (creator(client, callback_query,callback_query))):
        if data.split("-")[-2] in ["True", "False"]:
                
            permission_name, permission_key = callback_query.data.split("-", 1)
            setattr(chat_permissions, permission_name, False if permission_key == "True-permissions" else True)
            save_group_permissions(callback_data_chat, chat_permissions)
            
            keyboard = []
            for permission in permissions:
                permission_name, permission_key = permission
                button_text = permission_name + " ✅" if getattr(chat_permissions, permission_key) else permission_name + " ❌"
                boolean = "-True" if getattr(chat_permissions, permission_key) else "-False"
                keyboard.append([InlineKeyboardButton(button_text, callback_data=f"{permission_key}{boolean}-permissions")])
                    
            keyboard.append([InlineKeyboardButton("إغلاق 🚶", callback_data="permissions-save")])
            reply_markup = InlineKeyboardMarkup(keyboard)
                
            await callback_query.edit_message_text(
                text="قم بإختيار الصلاحيات المطلوبه :" ,
                reply_markup=reply_markup
                )
        
        elif data == "permissions-save":
            save_group_permissions(callback_data_chat, chat_permissions)
            await callback_query.edit_message_text("تم حفظ الإعدادات ✅️")
    else:
        await client.answer_callback_query(callback_query.id, text="بطل لعب الرساله مش ليك 😒", show_alert=True)