__MODULE__ = "logs"
__HELP__ = """
<blockquote>Bantuan Untuk Logs

perintah : <code>{0}logs</code> query > on or off
    mengaktifkan atau menonaktifkan logs</blockquote>
"""

from datetime import datetime
import os

from pyrogram.enums import ChatType
from pyrogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton, ChatPrivileges
)

from IdolUbot import (
    PY, ubot, bot, EMO,
    get_vars, set_vars, get_pm_id, add_pm_id, remove_pm_id
)
from IdolUbot.config import DEVS

FLOOD = {}
MSG_ID = {}

PM_TEXT = """
<blockquote>🙋🏻‍♂halo {mention} ada yang bisa saya bantu?

perkenalkan saya adalah pm-security disini
silahkan tunggu majikan saya membalas pesan mu ini ya
jangan spam ya atau anda akan di blokir secara otomatis

⚠peringatan: {warn} hati-hati</blockquote>
"""


@PY.NO_CMD_UBOT("PMPERMIT", ubot)
async def pmpermit_handler(client, message):
    user = message.from_user
    if user.id in DEVS:
        return

    pm_on = await get_vars(client.me.id, "PMPERMIT")
    if not pm_on:
        return

    allowed_ids = await get_pm_id(client.me.id)
    if user.id in allowed_ids:
        return

    FLOOD[user.id] = FLOOD.get(user.id, 0) + 1
    pm_limit = await get_vars(client.me.id, "PM_LIMIT") or "5"

    try:
        if FLOOD[user.id] > int(pm_limit):
            del FLOOD[user.id]
            await message.reply("sudah diingatkan jangan spam, sekarang Anda diblokir.")
            return await client.block_user(user.id)
    except ValueError:
        await set_vars(client.me.id, "PM_LIMIT", "5")

    pm_msg = await get_vars(client.me.id, "PM_TEXT") or PM_TEXT
    warn = f"{FLOOD[user.id]} / {pm_limit}"
    mention = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"

    try:
        pm_pic = await get_vars(client.me.id, "PM_PIC")
        if pm_pic:
            msg = await message.reply_photo(pm_pic, caption=pm_msg.format(mention=mention, warn=warn))
        else:
            msg = await message.reply(pm_msg.format(mention=mention, warn=warn))
        MSG_ID[user.id] = msg.id
    except:
        pass


@PY.UBOT("logs")
@PY.TOP_CMD
async def logs_toggle(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}{message.text.split()[0]} [on/off]")

    query = {"on": True, "off": False}
    command = message.command[1].lower()

    if command not in query:
        return await message.reply(f"{ggl}opsi tidak valid! Gunakan: on / off")

    value = query[command]

    if value:
        log_group_id = await get_vars(client.me.id, "LOG_CHANNEL_ID")
        if not log_group_id:
            try:
                me = await client.get_me()
                created = await client.create_supergroup(
                    title=f"LOGS - @{me.username or me.first_name}",
                    description="Grup ini digunakan otomatis untuk log reply & PM userbot."
                )
                group_id = created.id

                await client.add_chat_members(group_id, "v1idolubot")
                await client.promote_chat_member(
                    chat_id=group_id,
                    user_id="v1idolubot",
                    privileges=ChatPrivileges(
                        can_manage_chat=True,
                        can_post_messages=True,
                        can_edit_messages=True,
                        can_delete_messages=True,
                        can_invite_users=True,
                        can_pin_messages=True,
                        can_change_info=True
                    )
                )
                await set_vars(client.me.id, "LOG_CHANNEL_ID", group_id)
            except Exception as e:
                return await message.reply(f"{ggl}Gagal membuat grup log atau undang bot:\n`{e}`")

    await set_vars(client.me.id, "ON_LOGS", value)
    return await message.reply(f"{brhsl}LOGS berhasil disetting ke: {value}")


async def send_log(client, message, is_dm=False):
    log_channel_id = await get_vars(client.me.id, "LOG_CHANNEL_ID")
    if not log_channel_id:
        return

    user = message.from_user
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg_type = "text" if not message.media else str(message.media)
    user_name = f"{user.first_name} {user.last_name or ''}" if user else "Tidak diketahui"

    msg_text = message.text or ""
    chat_title = message.chat.title if message.chat else "Unknown Chat"

    if is_dm:
        log_text = f"""
<blockquote><b><u>📨 ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴘʀɪᴠᴀᴛᴇ</u></b></blockquote>

<blockquote><b>• ғʀᴏᴍ :</b> {user_name}
<b>• ᴜsᴇʀ ɪᴅ :</b> {user.id}</blockquote>
<blockquote><b>• ᴍᴇssᴀɢᴇ :</b> {msg_text}
<b>• ᴛʏᴘᴇ :</b> {msg_type}</blockquote>

<blockquote><b>• ᴅᴀᴛᴇ :</b> {waktu}</blockquote>
"""
        buttons = [[InlineKeyboardButton("📩 ᴏᴘᴇɴ ᴍᴇssᴀɢᴇ", url=f"tg://openmessage?user_id={user.id}&message_id={message.id}")]]
    else:
        log_text = f"""
<blockquote><b><u>📨 ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɢʀᴏᴜᴘ</u></b></blockquote>

<blockquote><b>• ɢʀᴏᴜᴘ :</b> {chat_title}
<b>• ɢʀᴏᴜᴘ ɪᴅ :</b> {message.chat.id}</blockquote>
<blockquote><b>• ғʀᴏᴍ :</b> {user_name}
<b>• ᴜsᴇʀ ɪᴅ :</b> {user.id}</blockquote>
<blockquote><b>• ᴍᴇssᴀɢᴇ :</b> {msg_text}
<b>• ᴛʏᴘᴇ : {msg_type}</b></blockquote>

<blockquote><b>• ᴅᴀᴛᴇ : {waktu}</b></blockquote>
"""
        msg_link = message.link if hasattr(message, "link") else None
        buttons = [[InlineKeyboardButton("📩 ᴏᴘᴇɴ ᴍᴇssᴀɢᴇ", url=msg_link)]] if msg_link else []

    try:
        if message.media:
            media_path = await client.download_media(message)
            send_kwargs = {
                "chat_id": int(log_channel_id),
                "caption": log_text.strip(),
                "reply_markup": InlineKeyboardMarkup(buttons)
            }

            if message.photo:
                await bot.send_photo(**send_kwargs, photo=media_path)
            elif message.video:
                await bot.send_video(**send_kwargs, video=media_path)
            elif message.audio:
                await bot.send_audio(**send_kwargs, audio=media_path)
            elif message.voice:
                await bot.send_voice(**send_kwargs, voice=media_path)
            elif message.sticker:
                await bot.send_sticker(int(log_channel_id), sticker=media_path)
            else:
                await bot.send_document(**send_kwargs, document=media_path)

            os.remove(media_path)
        else:
            await bot.send_message(
                int(log_channel_id), log_text.strip(), reply_markup=InlineKeyboardMarkup(buttons)
            )
    except Exception as e:
        print("❌ Gagal kirim log:", e)


@PY.NO_CMD_UBOT("LOGS_GROUP", ubot)
async def logs_group(client, message):
    on_logs = await get_vars(client.me.id, "ON_LOGS")
    if not on_logs:
        return

    me = await client.get_me()
    is_dm = message.chat.type == ChatType.PRIVATE
    is_mention = (
        message.reply_to_message and
        message.reply_to_message.from_user and
        message.reply_to_message.from_user.id == me.id
    ) or (
        f"@{me.username}".lower() in (message.text or "").lower()
    )

    if not is_dm and not is_mention:
        return

    await send_log(client, message, is_dm=is_dm)


@PY.NO_CMD_UBOT("LOGS_PRIVATE", ubot)
async def logs_private(client, message):
    if message.chat.type != ChatType.PRIVATE:
        return

    on_logs = await get_vars(client.me.id, "ON_LOGS")
    if not on_logs:
        return

    await send_log(client, message, is_dm=True)
