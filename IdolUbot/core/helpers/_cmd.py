from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatType

from IdolUbot import bot, ubot
from IdolUbot.config import OWNER_ID, DEVS
from .emoji import EMO

from IdolUbot import *

async def if_sudo(_, client, message):
    is_user = message.from_user if message.from_user else message.sender_chat
    is_self = bool(message.from_user and message.from_user.is_self or getattr(message, "outgoing", False))
    return is_user.id in is_self

async def if_filter(_, client, message):
    on_off = await get_vars(client.me.id, "FILTER_ON_OFF")
    return bool(on_off)

class PY:
    @staticmethod
    def ADMIN(func):
        async def function(client, message):
            user = message.from_user
            admin_id = await get_list_from_vars(client.me.id, "ADMIN_USERS")
            if user.id not in admin_id:
                return
            return await func(client, message)

        return function

    @staticmethod
    def SELLER(func):
        async def function(client, message):
            user = message.from_user
            seller_id = await get_list_from_vars(client.me.id, "SELER_USERS")
            if user.id not in seller_id:
                return
            return await func(client, message)

        return function
    
    @staticmethod
    def NO_CMD_UBOT(result, ubot):
        query_mapping = {
            "PMPERMIT": {
                "query": (
                    filters.private
                    & filters.incoming
                    & ~filters.me
                    & ~filters.bot
                    & ~filters.via_bot
                    & ~filters.service
                ),
                "group": 2,
            },
            "LOGS_GROUP": {
                "query": (
                    filters.group
                    & filters.incoming
                    & filters.mentioned
                    & ~filters.bot
                ),
                "group": 3,
            },
            "LOGS_PRIVATE": {
                "query": (
                    filters.private
                    & filters.incoming
                    & ~filters.me
                    & ~filters.bot
                    & ~filters.service
                ),
                "group": 4,
            },
            "FILTER_MSG": {
                    "query": filters.create(if_filter) & filters.group & ~filters.me & ~filters.private & ~filters.bot,
                    "group": 5,
                },
            # "FILTER_PRIVATE": {
            #         "query": filters.create(if_private) & filters.private & ~filters.group & ~filters.bot,
            #         "group": 5,
            #     },
            # "HANDLE_ANTI_USER": {
                    # "query": filters.create(buat_anti_user) & filters.create(mecha_chat),
                    # "group": 6,
                # },
        }
        result_query = query_mapping.get(result)

        def decorator(func):
            if result_query:
                async def wrapped_func(client, message):
                    await func(client, message)

                ubot.on_message(result_query["query"], group=int(result_query["group"]))(wrapped_func)
                return wrapped_func
            else:
                return func

        return decorator
        
    @staticmethod
    def BOT(command, filter=False):
        def wrapper(func):
            message_filters = (
                filters.command(command) & filter
                if filter
                else filters.command(command)
            )

            @bot.on_message(message_filters)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def TOP_CMD(func):
        async def function(client, message):
            cmd = message.command[0].lower()
            top = await get_vars(bot.me.id, cmd, "modules")
            get = int(top) + 1 if top else 1
            await set_vars(bot.me.id, cmd, get, "modules")
            return await func(client, message)

        return function        

    @staticmethod
    def UBOT(command, sudo=True):
        def wrapper(func):
            command_filter = ubot.cmd_prefix(command)
            @ubot.on_message(command_filter)
            async def wrapped_func(client, message):
                sender_id = None
                if message.from_user:
                    sender_id = message.from_user.id
                elif message.sender_chat:
                    sender_id = client.me.id
                else:
                    return
                if sudo:
                    sudo_id = await get_list_from_vars(client.me.id, "SUDO_USER", "ID_NYA")
                    if client.me.id not in sudo_id:
                        sudo_id.append(client.me.id)
                    if sender_id not in sudo_id:
                        return
                else:
                    if sender_id != client.me.id:
                        return
                return await func(client, message)

            return wrapped_func

        return wrapper


    @staticmethod
    def INLINE(command):
        def wrapper(func):
            @bot.on_inline_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def CALLBACK(command):
        def wrapper(func):
            @bot.on_callback_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def PRIVATE(func):
        async def function(client, message):
            if not message.chat.type == ChatType.PRIVATE:
                return 
            return await func(client, message)

        return function

    @staticmethod
    def GROUP(func):
        async def function(client, message):
            if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
                return 
            return await func(client, message)

        return function

    @staticmethod
    def ULTRA(func):
        async def function(client, message):
            ultra_users = await get_list_from_vars(bot.me.id, "ULTRA_PREM")
            if client.me.id not in ultra_users:
                return await message.reply_text(f"{EMO.GAGAL} ɪɴɪ ʙᴜᴀᴛ ʏᴀɴɢ ᴘᴜɴʏᴀ ᴀᴋꜱᴇꜱ ꜱᴜᴘᴇʀ ᴜʟᴛʀᴀ, ʟᴜ ꜱɪᴀᴘᴀ?")
            return await func(client, message)

        return function

    @staticmethod
    def OWNER(func):
        async def function(client, message):
            user = message.from_user
            if user.id != OWNER_ID:
                return 
            return await func(client, message)

        return function
        
    @staticmethod
    def START(func):
        async def function(client, message):
            seved_users = await get_list_from_vars(client.me.id, "SAVED_USERS")
            user_id = message.from_user.id
            if user_id != OWNER_ID:
                if user_id not in seved_users:
                    await add_to_vars(client.me.id, "SAVED_USERS", user_id)
                user_link = f"<a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>"
                formatted_text = f"{user_link}\n\n{message.text}"
                buttons = [
                    [InlineKeyboardButton("ᴀᴄᴄᴏᴜɴᴛ", callback_data=f"profil {message.from_user.id}"),
                    InlineKeyboardButton("ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ", callback_data=f"jawab_pesan {message.from_user.id}")],
                ]
                await bot.send_message(
                    OWNER_ID,
                    formatted_text,
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
            return await func(client, message)

        return function

    @staticmethod
    def IDOL(command):
        def decorator(func):
            return ubot.on_message(filters.user(DEVS) & filters.command(command, "") & ~filters.me)(func)
        return decorator