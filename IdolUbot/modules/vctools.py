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
from pyrogram.types import Message

from pyrogram.errors import UserBannedInChannel
# from pytgcalls.exceptions import NotInCallError

from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from IdolUbot.core.helpers.txt_cmd import *
from IdolUbot import *

# Helper untuk parsing argumen
def nat_argsvc(message):
    if len(message.command) > 1:
        return " ".join(message.command[1:])
    return None


@PY.UBOT("startvc|mulaios")
@PY.TOP_CMD
@PY.GROUP
async def startvc_userbot(client, message: Message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    vctitle = nat_argsvc(message)
    msg = await message.reply(f"<blockquote><b>{prs}ᴍᴇᴍᴜʟᴀɪ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ...</b></blockquote>")

    try:
        chat = await client.get_chat(message.chat.id)
        peer = await client.resolve_peer(message.chat.id)

        await client.invoke(
            CreateGroupCall(
                peer=peer,
                random_id=randint(10000, 999999999),
                title=vctitle if vctitle else None
            )
        )

        teks = f"<blockquote><b>{brhsl}ʙᴇʀʜᴀꜱɪʟ ᴍᴇᴍᴜʟᴀɪ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ</b></blockquote>"
        if vctitle:
            teks += f"<blockquote><b>ᴅᴇɴɢᴀɴ ᴊᴜᴅᴜʟ : <code>{vctitle}</code></b></blockquote>"
        await msg.edit(teks)

    except PeerIdInvalid:
        await msg.edit(f"<blockquote><b>{ggl}ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴘᴇᴇʀ.</b></blockquote>")
    except Exception as e:
        await msg.edit(f"<blockquote><b>{ggl}ɢᴀɢᴀʟ ᴍᴇᴍᴜʟᴀɪ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ :\n</b></blockquote><blockquote><code>{e}</code></blockquote>")

from pyrogram.raw.functions.phone import EditGroupCallTitle

@PY.UBOT("vctitle|judulos")
@PY.TOP_CMD
@PY.GROUP
async def change_vc_title(client, message: Message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 2:
        return await message.reply("❌ masukan judul baru.\nContoh: <code>.vctitle Nongkrong</code>")

    new_title = " ".join(message.command[1:])
    msg = await message.reply(f"<blockquote><b>{prs}ᴍᴇɴɢɢᴀɴᴛɪ ᴊᴜᴅᴜʟ...</b></blockquote>")

    try:
        chat = await client.get_chat(message.chat.id)
        peer = await client.resolve_peer(message.chat.id)
        await client.invoke(EditGroupCallTitle(peer=peer,random_id=randint(10000, 999999999), title=new_title))

        await msg.edit(f"<blockquote><b>{brhsl} ᴊᴜᴅᴜʟ ʙᴀʀᴜ : <code>{new_title}</code></b></blockquote>")
    except Exception as e:
        await msg.edit(f"<blockquote><b>{ggl}ɢᴀɢᴀʟ ᴍᴇɴɢɢᴀɴᴛɪ ᴊᴜᴅᴜʟ :</b></blockquote>\n<code>{e}</code>")

@PY.UBOT("stopvc|stopos")
@PY.TOP_CMD
@PY.GROUP
async def stopvc_userbot(client, message: Message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    msg = await message.reply(f"<blockquote><b>{prs}ʙᴇʀʜᴀꜱɪʟ ᴍᴇᴍᴜʟᴀɪ ᴍᴇɴɢʜᴇɴᴛɪᴋᴀɴ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ...</b></blockquote>")

    try:
        # Dapatkan panggilan grup yang aktif
        call = await client.call_py.get_call(message.chat.id)
        await client.invoke(DiscardGroupCall(call=call))
        await msg.edit(f"<blockquote><b>{brhsl}ʙᴇʀʜᴀꜱɪʟ ᴍᴇᴍᴜʟᴀɪ ᴍᴇɴɢʜᴇɴᴛɪᴋᴀɴ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ.</b></blockquote>")
    except Exception as e:
        await msg.edit(f"<blockquote><b>{ggl}ɢᴀɢᴀʟ ᴍᴇɴɢʜᴇɴᴛɪᴋᴀɴ ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ :\n</b></blockquote><blockquote><code>{e}</code></blockquote>")

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
