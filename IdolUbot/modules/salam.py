import asyncio
from time import sleep
from IdolUbot import *

__MODULE__ = "salam"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴀʟᴀᴍ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}p</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢɪʀɪᴍ ᴀssᴀʟᴀᴍᴜ'ᴀʟᴀɪᴋᴜᴍ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}pe</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢɪʀɪᴍ ᴀssᴀʟᴀᴍᴜ'ᴀʟᴀɪᴋᴜᴍ ᴡᴀʀᴀʜᴍᴀᴛᴜʟʟᴀʜɪ ᴡᴀʙᴀʀᴀᴋᴀᴛᴜʜ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}l</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢɪʀɪᴍ ᴡᴀ'ᴀʟᴀɪᴋᴜᴍsᴀʟᴀᴍ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}wl</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢɪʀɪᴍ ᴡᴀ'ᴀʟᴀɪᴋᴜᴍsᴀʟᴀᴍ ᴡᴀʀᴀʜᴍᴀᴛᴜʟʟᴀʜɪ ᴡᴀʙᴀʀᴀᴋᴀᴛᴜʜ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}as</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢɪʀɪᴍ ᴛᴇᴋs ᴘᴇɴᴄᴏʙᴀᴀɴ.</blockquote>
"""



@PY.UBOT("p")
async def inijugajangandiapusataudigantikrnizzyganteng(client, message):
    await message.edit(
        "Assalamu'alaikum",
    )


@PY.UBOT("pe")
async def biarpanjangajayangpentingizzyganteng(client, message):
    await message.edit(
        "Assalamualaikum Warahmatullahi Wabarakatuh",
    )


@PY.UBOT("l")
async def biarmampuslusemuakontol(client, message):
    await message.edit(
        "waalaikumsalam",
    )


@PY.UBOT("wl")
async def ularnagapanajnagnyabukankepalangtapiizzygantengamat(client, message):
    await message.edit(
        "Wa'alaikumsalam Warahmatullahi Wabarakatuh",
    )


@PY.UBOT("as")
async def pelerpelerpeler(client, message):
    await message.edit(
        "Salam dulu woy!",
    )
