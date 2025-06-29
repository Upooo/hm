__MODULE__ = "admin"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀᴅᴍɪɴ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :
🦠 <code>{0}kick</code>
🦠 <code>{0}ban</code> 
🦠 <code>{0}mute</code> 
🦠 <code>{0}etmin</code> 
🦠 <code>{0}ceo</code> 
🦠 <code>{0}demote</code>
🦠 <code>{0}unmute</code> 
🦠 <code>{0}unban</code></b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :
🦠 <code>{0}lock</code> 
🦠 <code>{0}unlock</code> 
🦠 <code>{0}locks</code>
🦠 ᴍᴇɴɢᴜɴᴄɪ/ᴍᴇᴍʙᴜᴋᴀ ᴅᴀɴ ʟɪsᴛ ɪᴢɪɴ ɢʀᴏᴜᴘ</b></blockquote>
<blockquote><b>🚦 ᴄᴏɴᴛᴏʜ:
🦠 <code>{0}lock msg</code> 
🦠 <code>{0}lock media</code> 
🦠 <code>{0}lock pin</code>
🦠 <code>{0}lock polls</code> 
🦠 <code>{0}lock info</code> 
🦠 <code>{0}lock invite</code>
🦠 <code>{0}lock webprev</code> 
🦠 <code>{0}lock stickers</code></b></blockquote>
"""

import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    ChatNotModified,
)

from IdolUbot import *

LCKS = ADMINCMD.k
BABUGCE = ADMINCMD.a + ADMINCMD.b + ADMINCMD.c + ADMINCMD.g + ADMINCMD.h

data = {
    "msg": "can_send_messages",
    "stickers": "can_send_other_messages",
    "gifs": "can_send_other_messages",
    "media": "can_send_media_messages",
    "games": "can_send_other_messages",
    "inline": "can_send_other_messages",
    "url": "can_add_web_page_previews",
    "polls": "can_send_polls",
    "info": "can_change_info",
    "invite": "can_invite_users",
    "pin": "can_pin_messages",
}

async def current_chat_permissions(client, chat_id):
    perms = []
    perm = (await client.get_chat(chat_id)).permissions
    if perm.can_send_messages:
        perms.append("can_send_messages")
    if perm.can_send_media_messages:
        perms.append("can_send_media_messages")
    if perm.can_send_other_messages:
        perms.append("can_send_other_messages")
    if perm.can_add_web_page_previews:
        perms.append("can_add_web_page_previews")
    if perm.can_send_polls:
        perms.append("can_send_polls")
    if perm.can_change_info:
        perms.append("can_change_info")
    if perm.can_invite_users:
        perms.append("can_invite_users")
    if perm.can_pin_messages:
        perms.append("can_pin_messages")
    return perms


async def tg_lock(
    client,
    message,
    parameter,
    permissions: list,
    perm: str,
    lock: bool,
):
    if lock:
        if perm not in permissions:
            return await message.reply(f"<blockquote><b>{parameter} ꜱᴜᴅᴀʜ ᴛᴇʀᴋᴜɴᴄɪ</b></blockquote>")
        permissions.remove(perm)
    else:
        if perm in permissions:
            return await message.reply(f"<blockquote><b>{parameter} ꜱᴜᴅᴀʜ ᴛᴇʀʙᴜᴋᴀ</b></blockquote>")
        permissions.append(perm)
    permissions = {perm: True for perm in set(permissions)}
    try:
        await client.set_chat_permissions(
            message.chat.id, ChatPermissions(**permissions)
        )
    except ChatNotModified:
        return await message.reply(
            f"<blockquote><b>{message.text.split()[0]} [type]</b></blockquote>"
        )
    except ChatAdminRequired:
        return await message.reply("<blockquote><b>ᴛɪᴅᴀᴋ ᴍᴇᴍᴘᴜɴʏᴀɪ ɪᴢɪɴ.</b></blockquote>")
    await message.reply(
        (
            f"<blockquote><b>ᴛᴇʀᴋᴜɴᴄɪ ᴜɴᴛᴜᴋ ɴᴏɴ-ᴀᴅᴍɪɴ!\nᴛɪᴘᴇ : {parameter}\nɢʀᴜᴘ : {message.chat.title}</b></blockquote>"
            if lock
            else f"<blockquote><b>ᴛᴇʀʙᴜᴋᴀ ᴜɴᴛᴜᴋ ɴᴏɴ-ᴀᴅᴍɪɴ!\nᴛɪᴘᴇ : {parameter}\nɢʀᴜᴘ : {message.chat.title}</b></blockquote>"
        )
    )
    
@PY.UBOT("lock|unlock")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    if len(message.command) != 2:
        return await message.reply(f"{message.text.split()[0]} [type]")
    chat_id = message.chat.id
    parameter = message.text.strip().split(None, 1)[1].lower()
    state = message.command[0].lower()
    if parameter not in data and parameter != "all":
        return await message.reply("NGENTOT HEHEHE")
    permissions = await current_chat_permissions(client, chat_id)
    if parameter in data:
        await tg_lock(
            client,
            message,
            parameter,
            permissions,
            data[parameter],
            bool(state == "lock"),
        )
    elif parameter == "all" and state == "lock":
        try:
            await client.set_chat_permissions(chat_id, ChatPermissions())
            await message.reply(
                f"<blockquote><b>ᴛᴇʀᴋᴜɴᴄɪ ᴜɴᴛᴜᴋ ɴᴏɴ-ᴀᴅᴍɪɴ!\nᴛɪᴘᴇ : {parameter}\nɢʀᴜᴘ : {message.chat.title}</b></blockquote>"
            )
        except ChatAdminRequired:
            return await message.reply("<blockquote><b>ᴛɪᴅᴀᴋ ᴍᴇᴍᴘᴜɴʏᴀɪ ɪᴢɪɴ.</b></blockquote>")
        except ChatNotModified:
            return await message.reply(
                f"<blockquote><b>ᴛᴇʀᴋᴜɴᴄɪ ᴜɴᴛᴜᴋ ɴᴏɴ-ᴀᴅᴍɪɴ!\nᴛɪᴘᴇ : {parameter}\nɢʀᴜᴘ : {message.chat.title}</b></blockquote>"
            )
    elif parameter == "all" and state == "unlock":
        try:
            await client.set_chat_permissions(
                chat_id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_add_web_page_previews=True,
                    can_send_polls=True,
                    can_change_info=False,
                    can_invite_users=True,
                    can_pin_messages=False,
                ),
            )
        except ChatAdminRequired:
            return await message.reply("<blockquote><b>ᴛɪᴅᴀᴋ ᴍᴇᴍᴘᴜɴʏᴀɪ ɪᴢɪɴ.</b></blockquote>")
        await message.reply(
            f"<blockquote><b>ᴛᴇʀʙᴜᴋᴀ ᴜɴᴛᴜᴋ ɴᴏɴ-ᴀᴅᴍɪɴ!\nᴛɪᴘᴇ : {parameter}\nɢʀᴜᴘ : {message.chat.title}</b></blockquote>"
        )


@PY.UBOT("locks")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    permissions = await current_chat_permissions(client, message.chat.id)
    if not permissions:
        return await message.reply("<blockquote><b>ᴛᴇʀᴋᴜɴᴄɪ ᴜɴᴛᴜᴋ ꜱᴇᴍᴜᴀ.</b></blockquote>")

    perms = " -> __**" + "\n -> __**".join(permissions) + "**__"
    await message.reply(perms)


@PY.UBOT("kick|ban|mute|unmute|unban|usir|bisu|tendang")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    bcs = await EMO.BROADCAST(client)
    tion = await EMO.MENTION(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    if message.command[0] == "kick|tendang":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text(f"<blockquote><b>{ggl}{message.text.split()[0]} [username/user_id/reply]</b></blockquote>")
        if user_id == OWNER_ID:
            return await message.reply_text(f"<blockquote><b>{ggl} ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪꜱᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ɪɴɪ.</b></blockquote>")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                f"<blockquote><b>{ggl} ꜱᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪꜱᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀᴅᴍɪɴ.</b></blockquote>"
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        msg_kick = f"""
<blockquote><b>{bcs}ᴡᴀʀɴɪɴɢ: {mention}<b>
<b>{tion}ᴀᴅᴍɪɴ: {message.from_user.mention}</b>
<b>{ktrng}ᴀʟᴀꜱᴀɴ: {reason}</b></blockquote>

<blockquote><b>ᣃᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ</b></blockquote>
            """
        try:
            await message.chat.ban_member(user_id)
            await message.reply(msg_kick)
            await asyncio.sleep(1)
            await message.chat.unban_member(user_id)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "ban|usir":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text(f"<blockquote><b>{ggl}{message.text.split()[0]} [username/user_id/reply]</b></blockquote>")
        if user_id == OWNER_ID:
            return await message.reply_text(f"<blockquote><b>{ggl} ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪꜱᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴀɴɢɢᴏᴛᴀ ɪɴɪ.</b></blockquote>")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                f"<blockquote><b>{ggl} ꜱᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪꜱᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴀᴅᴍɪɴ.</b></blockquote>"
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        msg_ban = f"""
<blockquote><b>{bcs}⎆ ᴡᴀʀɴɪɴɢ: {mention}<b>
<b>{tion}⎆ ᴀᴅᴍɪɴ: {message.from_user.mention}</b>
<b>{ktrng}⎆ ᴀʟᴀꜱᴀɴ: {reason}</b></blockquote>

<blockquote><b>ᣃᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ</b></blockquote>
            """
        try:
            await message.chat.ban_member(user_id)
            await message.reply(msg_ban)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "mute|bisu":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text(f"<blockquote><b>{ggl}{message.text.split()[0]} [username/user_id/reply]")
        if user_id == OWNER_ID:
            return await message.reply_text(f"<blockquote><b>{ggl} ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪꜱᴀ ᴍᴇᴍʙɪꜱᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪɴɪ.</b></blockquote>")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                f"<blockquote><b>{ggl} ꜱᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪꜱᴀ ᴍᴇᴍʙɪꜱᴜᴋᴀɴ ᴀᴅᴍɪɴ.</b></blockquote>"
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        msg_mute = f"""
<blockquote><b>{bcs}⎆ ᴡᴀʀɴɪɴɢ: {mention}</b>
<b>{tion}⎆ ᴀᴅᴍɪɴ: {message.from_user.mention}</b>
<b>{ktrng}⎆ ᴀʟᴀꜱᴀɴ: {reason}</blockquote></b>\n<blockquote><b>⎆ ᴋᴇᴛ: ᴍᴀᴍᴘᴜs ᴅɪ ᴍᴜᴛᴇ ᴇᴛᴍɪɴ</blockquote></b>

<blockquote><b>ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ</b></blockquote>
            """
        try:
            await message.chat.restrict_member(user_id, ChatPermissions())
            await message.reply(msg_mute)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "unmute":
        user_id = await extract_user(message)
        if not user_id:
            return await message.reply_text(f"<blockquote><b>{ggl}{message.text.split()[0]} [username/user_id/reply]</b></blockquote>")
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        try:
            await message.chat.unban_member(user_id)
            await message.reply(f"<blockquote><>{brhsl}{mention} ꜱᴜᴅᴀʜ ʙɪꜱᴀ ᴄʜᴀᴛ ʟᴀɢɪ.</b></blockquote>")
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "unban":
        user_id = await extract_user(message)
        if not user_id:
            return await message.reply_text(f"<blockquote><b>{ggl}{message.text.split()[0]} [username/user_id/reply]</b></blockquote>")
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        try:
            await message.chat.unban_member(user_id)
            await message.reply(f"<blockquote><b>{brhsl}{mention} ꜱᴜᴅᴀʜ ʙɪꜱᴀ ᴊᴏɪɴ ʟᴀɢɪ.</b></blockquote>")
        except Exception as error:
            await message.reply(error)
            
@PY.UBOT("etmin")
@PY.TOP_CMD
async def promotte(client: Client, message: Message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    user_id = await extract_user(message)
    anu = await eor(message, f"{prs}processing...")
    if not user_id:
        return await anu.edit(f"{ggl}pengguna tidak ditemukan.")
    (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    try:
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=False,
            ),
        )
        await asyncio.sleep(1)
        umention = (await client.get_users(user_id)).mention
        return await anu.edit(f"{sks}berhasil mempromosikan : {umention} menjadi admin")
    except ChatAdminRequired:
        await anu.edit(f"{ggl}**anda bukan admin di group ini !**")

@PY.UBOT("ceo")
@PY.TOP_CMD
async def promotte(client: Client, message: Message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    user_id = await extract_user(message)
    anu = await eor(message, f"{prs}processing...")
    if not user_id:
        return await anu.edit(f"{ggl}pengguna tidak ditemukan.")
    (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    try:
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=True,
            ),
        )
        await asyncio.sleep(1)
        umention = (await client.get_users(user_id)).mention
        return await anu.edit(f"{sks}berhasil mempromosikan : {umention} menjadi ceo")
    except ChatAdminRequired:
        await anu.edit(f"{ggl}**anda bukan admin di group ini !**")

 
@PY.UBOT("demote")
@PY.TOP_CMD
async def demote(client: Client, message: Message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    user_id = await extract_user(message)
    sempak = await eor(message, f"{prs}processing...")
    if not user_id:
        return await sempak.edit(f"{ggl}pengguna tidak ditemukan")
    if user_id == client.me.id:
        return await sempak.edit(f"{ggl}tidak bisa demote diri sendiri.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    await asyncio.sleep(1)
    umention = (await client.get_users(user_id)).mention
    await sempak.edit(f"{sks}demoted : {umention}")
    await sempak.edit(sempak)
    await sempak.delete()

@PY.UBOT("getlink")
@PY.TOP_CMD
async def get_link(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    try:
        link = await client.export_chat_invite_link(message.chat.id)
        await message.reply_text(f"{sks}ini hasilnya tuan : {link}", disable_web_page_preview=True)
    except Exception as r:
        await message.reply_text(f"{ggl}terjadi error : \n {r}")
