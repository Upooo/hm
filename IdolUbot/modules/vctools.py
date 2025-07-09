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
from typing import Optional
from pyrogram.types import Message

from pyrogram import Client, enums
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall, EditGroupCallTitle
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
from IdolUbot.core.helpers.txt_cmd import *
from IdolUbot import *

def nat_argsvc(message):
    if len(message.command) > 1:
        return " ".join(message.command[1:])
    return None

async def get_group_call(
    client: Client, message: Message, err_msg: str = "") -> Optional[InputGroupCall]:
    
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
    await eor(message, f"<blockquote><b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴏꜱ ᴅɪ ᴛᴇᴍᴜᴋᴀɴ</b></blockquote>\n<blockquote><b>{err_msg}</b></blockquote>")
    return False

@PY.UBOT("startvc")
async def start_vctools(client, message):
    flags = " ".join(message.command[1:])
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    gcr = await EMO.ALASAN(client)
    bbo = await EMO.PUTARAN(client)
    
    mmk = await message.reply(f"<blockquote><b>{prs}ʙᴇɴᴛᴀʀ ɴɪʜ ᴏᴛᴡ...</b></blockquote>")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = (
        f"<blockquote><b>{brhsl}ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ᴀᴋᴛɪꜰ</b></blockquote>\n<blockquote><b>{gcr}ɢʀᴏᴜᴘ : </b>{message.chat.title}</blockquote>"
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
            args += f"\n{bbo}<blockquote><b>ᴛɪᴛʟᴇ : </b>{vctitle}</blockquote>"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await mmk.edit(args)
    except Exception as e:
        await mmk.edit(f"<b>INFO :\n</b> <blockquote><code>{e}</code></blockquote>")


@PY.UBOT("stopvc")
async def stop_vctools(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    gcr = await EMO.ALASAN(client)
    
    
    hi = await message.reply(f"<blockquote><b>{prs}ʙᴇɴᴛᴀʀ ɴɪʜ ᴏᴛᴡ...</b></blockquote>")
    message.chat.id
    if not (
        group_call := (await get_group_call(client, message, err_msg=", ᴋᴇꜱᴀʟᴀʜᴀɴ..."))
    ):
        return
    await client.invoke(DiscardGroupCall(call=group_call))
    await hi.edit(
        f"<blockquote><b>{brhsl}ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ᴀᴋᴛɪꜰ</b></blockquote>\n<blockquote><b>{gcr}ɢʀᴏᴜᴘ : </b>{message.chat.title}</blockquote>"
        )
    
@PY.UBOT("vctitle")
async def set_vctitle(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    gcr = await EMO.ALASAN(client)
    bbo = await EMO.PUTARAN(client)

    proses = await message.reply(
        f"<blockquote><b>{prs}ʙᴇɴᴛᴀʀ ɴɪʜ ᴏᴛᴡ...</b></blockquote>"
    )

    if len(message.command) < 2:
        return await proses.edit(
            f"<blockquote><b>{ggl} ᴍᴀꜱᴜᴋᴋᴀɴ ᴊᴜᴅᴜʟ ʙᴀʀᴜ.</b></blockquote>\n"
            f"<blockquote><b>{bbo} ᴄᴏɴᴛᴏʜ :</b> <code>.vctitle Nongkrong Malam</code></blockquote>"
        )

    new_title = " ".join(message.command[1:])

    group_call = await get_group_call(client, message, err_msg=", ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ.")
    if not group_call:
        return

    try:
        await client.invoke(EditGroupCallTitle(call=group_call, title=new_title))
        await proses.edit(
            f"<blockquote><b>{brhsl} ᴊᴜᴅᴜʟ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ᴅɪᴘᴇʀʙᴀʀᴜɪ</b></blockquote>\n"
            f"<blockquote><b>{gcr} ɢʀᴏᴜᴘ :</b> {message.chat.title}</blockquote>\n"
            f"<blockquote><b>{bbo} ᴊᴜᴅᴜʟ ʙᴀʀᴜ :</b> <code>{new_title}</code></blockquote>"
        )
    except Forbidden:
        await proses.edit(
            f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴜʙᴀʜ ᴊᴜᴅᴜʟ :</b></blockquote>\n"
            f"<blockquote><b>{bbo} ᴋᴀᴍᴜ ᴛɪᴅᴀᴋ ᴍᴇᴍɪʟɪᴋɪ ɪᴢɪɴ.</b></blockquote>"
        )
    except Exception as e:
        await proses.edit(
            f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴜʙᴀʜ ᴊᴜᴅᴜʟ :</b></blockquote>\n"
            f"<blockquote><code>{e}</code></blockquote>"
        )

    
@PY.UBOT("cekos")
async def cekos_vc(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    gcr = await EMO.ALASAN(client)
    bbo = await EMO.PUTARAN(client)

    x = await message.reply(f"<blockquote><b>{prs}ʙᴇɴᴛᴀʀ ɴɪʜ ᴏᴛᴡ...</b></blockquote>")

    chat = message.command[1] if len(message.command) > 1 else message.chat.id

    try:
        chat_info = await client.get_chat(chat)
        chat_id = chat_info.id
        title = chat_info.title or str(chat_id)
    except Exception as e:
        return await x.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ɪɴꜰᴏ ɢʀᴏᴜᴘ:</b></blockquote>\n<blockquote><code>{e}</code></blockquote>")

    group_call = await get_group_call(client, message, err_msg=", ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ.")
    if not group_call:
        return

    try:
        participants = await client.call_py.get_participants(chat_id)
        total_participants = len(participants)

        if total_participants == 0:
            return await x.edit(
                f"<blockquote><b>{ggl} ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇꜱᴇʀᴛᴀ ᴅɪ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ!</b></blockquote>"
            )

        mentions = []
        for participant in participants:
            try:
                user = await client.get_users(participant.user_id)
                mention = user.mention
                mic_status = "🎙️ Unmuted" if participant.muted else "🔇 Muted"
                volume = participant.volume
                mentions.append(f"• {mention} | {mic_status} | 🔊 {volume}%")
            except Exception as e:
                mentions.append(f"• <code>{participant.user_id}</code> | ❓ Status Unknown")

        mentions_text = "\n".join(mentions)

        text = (
            f"<blockquote><b>{brhsl} ᴘᴇꜱᴇʀᴛᴀ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ</b></blockquote>\n"
            f"<blockquote><b>{gcr} ɢʀᴏᴜᴘ :</b> {title}</blockquote>\n"
            f"<blockquote><b>{bbo} ᴛᴏᴛᴀʟ :</b> <code>{total_participants}</code> ᴏʀᴀɴɢ</blockquote>\n\n"
            f"<blockquote>{mentions_text}</blockquote>"
        )
        await x.edit(text)

    except Exception as e:
        await x.edit(f"<blockquote><b>{ggl} ᴋᴇꜱᴀʟᴀʜᴀɴ :</b></blockquote>\n<blockquote><code>{e}</code></blockquote>")

@PY.UBOT("jvc|naik|jvcs")
@PY.IDOL("cjvc|cnaik|cjvcs")
@PY.TOP_CMD
@PY.GROUP
async def join_vc(client, message: Message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    gcr = await EMO.ALASAN(client)
    bbo = await EMO.PUTARAN(client)

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
            f"<blockquote><b>{gcr} ɴᴀᴍᴀ ɢᴄ : {chat_name}\n{bbo} ɪᴅ ɢᴄ: <code>{chat_id}</code></b></blockquote>"
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
    gcr = await EMO.ALASAN(client)
    bbo = await EMO.PUTARAN(client)

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
            f"<blockquote><b>{gcr} ɴᴀᴍᴀ ɢᴄ : {chat_name}\n{bbo} ɪᴅ ɢᴄ : <code>{chat_id}</code></b></blockquote>"
        )
    except Exception as e:
        await mex.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ :</b></blockquote>\n<blockquote><code>{e}</code></blockquote>")
