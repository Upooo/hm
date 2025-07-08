__MODULE__ = "ᴠᴄᴛᴏᴏʟꜱ"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴛᴏᴏʟꜱ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}startvc</code>
🦠 ᴋᴇᴛ : ᴍᴜʟᴀɪ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ɢʀᴏᴜᴘ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}stopvc</code>
🦠 ᴋᴇᴛ : ᴀᴋʜɪʀɪ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ɢʀᴏᴜᴘ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}jvc</code>
🦠 ᴋᴇᴛ : ʙᴇʀɢᴀʙᴜɴɢ ᴋᴇ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ɢʀᴏᴜᴘ ᴀᴛᴀᴜ ᴄʜᴀɴɴᴇʟ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}lvc</code>
🦠 ᴋᴇᴛ : ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ɢʀᴏᴜᴘ ᴀᴛᴀᴜ ᴄʜᴀɴɴᴇʟ.</b></blockquote>

<blockquote><b>❏ ɴᴀɪᴋ ᴛᴜʀᴜɴ ᴏꜱ ʙɪꜱᴀ ᴘᴀᴋᴇ :
├ ʟɪɴᴋ ɢʀᴏᴜᴘ ʟ
├ ᴜꜱᴇʀɴᴀᴍᴇ ᴄʜᴀɴɴᴇʟ
╰ ɪᴅ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇ
ᴄᴏɴᴛᴏʜ : <code>{0}jvc @xnxxnathan</code></b></blockquote>
"""

from random import randint
from asyncio import sleep
from typing import Optional
from contextlib import suppress
from pyrogram.types import Message

from pyrogram.errors import UserBannedInChannel
# from pytgcalls.exceptions import NotInCallError

from pyrogram import Client, enums
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall, EditGroupCallTitle
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
from IdolUbot.core.helpers.txt_cmd import *
from IdolUbot import *

# Helper untuk parsing argumen
def nat_argsvc(message):
    if len(message.command) > 1:
        return " ".join(message.command[1:])
    return None

async def get_group_call(

    client: Client, message: Message, err_msg: str = ""

) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await eor(message, f"**No group call Found** {err_msg}")
    return False

@PY.UBOT("startvc")
async def start_vctools(client, message):
    flags = " ".join(message.command[1:])
    ky = await message.reply("<code>Processing....</code>")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = (
        f"<b>• Obrolan Suara Aktif</b>\n<b>• Chat : </b><code>{message.chat.title}</code>"
    )
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • <b>Title : </b> <code>{vctitle}</code>"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await ky.edit(args)
    except Exception as e:
        await ky.edit(f"<b>INFO:</b> `{e}`")


@PY.UBOT("stopvc")
async def stop_vctools(client, message):
    hi = await message.reply("<code>Processing....</code>")
    message.chat.id
    if not (
        group_call := (await get_group_call(client, message, err_msg=", Kesalahan..."))
    ):
        return
    await client.invoke(DiscardGroupCall(call=group_call))
    await hi.edit(
        f"<b>• Obrolan Suara Diakhiri</b>\n<b>• Chat : </b><code>{message.chat.title}</code>")
    
@PY.UBOT("vctitle")
async def set_vctitle(client, message):
    proses = await message.reply("<code>Processing....</code>")

    if len(message.command) < 2:
        return await proses.edit("❌ Masukkan judul baru.\nContoh: <code>.vctitle Nongkrong Malam</code>")

    new_title = " ".join(message.command[1:])

    group_call = await get_group_call(client, message, err_msg=", gagal mendapatkan obrolan suara.")
    if not group_call:
        return

    try:
        await client.invoke(EditGroupCallTitle(call=group_call, title=new_title))
        await proses.edit(
            f"<b>• Judul Obrolan Suara Diperbarui</b>\n"
            f"<b>• Chat :</b> <code>{message.chat.title}</code>\n"
            f"<b>• Judul Baru :</b> <code>{new_title}</code>"
        )
    except Forbidden:
        await proses.edit("❌ Gagal mengubah judul: kamu tidak memiliki izin.")
    except Exception as e:
        await proses.edit(f"❌ Gagal mengubah judul:\n<code>{e}</code>")

    
@PY.UBOT("cekos")
async def cekos_vc(client, message):
    
    x = await message.reply("<code>Processing....</code>")

    chat = message.command[1] if len(message.command) > 1 else message.chat.id
    try:
        if isinstance(chat, int):
            chat_id = chat
        else:
            chat_info = await client.get_chat(chat)
            chat_id = chat_info.id

        try:
            info = await client.get_chat(chat_id)
            title = info.title if info.title else f"{chat_id}"
        except Exception:
            title = f"{chat_id}"
        group_call = await get_group_call(client, message, err_msg=", Error...")
        if not group_call:
            return await x.edit(
                f"<b>Voice chat group not found in {title}</b>"
            )
        try:
            participants = await client.call_py.get_participants(chat_id)
            mentions = []
            for participant in participants:
                user_id = participant.user_id
                try:
                    user = await client.get_users(user_id)
                    mention = user.mention
                    status = "Unmuted" if participant.muted else "Muted"
                    volume = participant.volume
                    mentions.append(f"{mention}|Mic: {status}|Vol: {volume}%")
                except Exception as e:
                    logger.error(f"{e}")
                    mentions.append(f"{user_id} Status Unknown")

            total_participants = len(participants)
            if total_participants == 0:
                return await x.edit(
                    f"<b>No someone in voice chat group!!</b>"
                )
            mentions_text = "\n".join(
                [
                    (f"• {mention}" if i < total_participants - 1 else f"• {mention}")
                    for i, mention in enumerate(mentions)
                ]
            )
            text = f"""
<b>Voice Chat Listener:</b>
Chat: <code>{title}</code>.
Total: <code>{total_participants}</code> Listener.

<b>People:</b>
{mentions_text}
"""
            return await x.edit(f"<blockquote><b>{text}</b></blockquote>")
        except Exception as e:
            return await x.edit(f"EROR : {e}")
    except Exception as e:
        return await x.edit(f"EROR : {e}")

@PY.UBOT("jvc|naik|jvcs")
@PY.IDOL("cjvc|cnaik|cjvcs")
@PY.TOP_CMD
@PY.GROUP
async def join_vc(client, message: Message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    try:
        mex = await message.reply(f"<blockquote><b>{prs}ʙᴇɴᴛᴀʀ ɴɪʜ ᴏᴛᴡ ɴᴀɪᴋ...</b></blockquote>")

        if len(message.command) > 1:
            target = message.command[1]

            if target.startswith("https://t.me/+"):
                chat = await client.get_chat(target)

            elif target.startswith("https://t.me/"):
                username = target.replace("https://t.me/", "").strip("/")
                chat = await client.get_chat(username)

            elif target.startswith("@"):
                chat = await client.get_chat(target)

            else:
                try:
                    chat_id = int(target)
                    chat = await client.get_chat(chat_id)
                except ValueError:
                    return await mex.edit(f"<blockquote><b>{ggl} ɪᴅ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ.</b></blockquote>")
        else:
            chat = await client.get_chat(message.chat.id)

        chat_id = chat.id
        chat_name = chat.title

        await client.call_py.play(chat_id)
        await client.call_py.mute_stream(chat_id)

        await mex.edit(
            f"<blockquote><b>{brhsl} ʙᴇʀʜᴀꜱɪʟ ɴᴀɪᴋ ᴋᴇ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ.</b></blockquote>\n"
            f"<blockquote><b>ɴᴀᴍᴀ ɢᴄ : {chat_name}\nɪᴅ ɢᴄ: <code>{chat_id}</code></b></blockquote>"
        )

    except Exception as e:
        await mex.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ :</b></blockquote>\n<blockquote><code>{e}</code></blockquote>")

@PY.UBOT("lvc|turun|lvcs")
@PY.IDOL("clvc|cturun|clvcs")
@PY.TOP_CMD
@PY.GROUP
async def leave_vc(client, message: Message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    try:
        mex = await message.reply(f"<blockquote><b>{prs}ʙᴇɴᴛᴀʀ ɴɪʜ ᴏᴛᴡ ᴛᴜʀᴜɴ...</b></blockquote>")

        if len(message.command) > 1:
            target = message.command[1]

            if target.startswith("https://t.me/"):
                username = target.replace("https://t.me/", "").strip("/")
                chat = await client.get_chat(username)
            elif target.startswith("@"):
                chat = await client.get_chat(target)
            else:
                chat_id = int(target)
                chat = await client.get_chat(chat_id)
        else:
            chat = await client.get_chat(message.chat.id)

        chat_id = chat.id
        chat_name = chat.title

        await client.call_py.leave_call(chat_id)

        await mex.edit(
            f"<blockquote><b>{brhsl} ʙᴇʀʜᴀꜱɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ.</b></blockquote>"
            f"<blockquote><b>ɴᴀᴍᴀ ɢᴄ : {chat_name}\nɪᴅ ɢᴄ : <code>{chat_id}</code></b></blockquote>"
        )
    except Exception as e:
        await mex.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ :</b></blockquote>\n<blockquote><code>{e}</code></blockquote>")
