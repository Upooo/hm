__MODULE__ = "adzan"
__HELP__ = f"""
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀᴅᴢᴀɴ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}adzan [nama kota]</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴡᴀᴋᴛᴜ ᴀᴅᴢᴀɴ ᴘᴀᴅᴀ ꜱᴜᴀᴛᴜ ᴡɪʟᴀʏᴀʜ.</b></blockquote>
"""

import json
import requests
from pyrogram import *
from pyrogram.types import *
from IdolUbot import *

@PY.UBOT("adzan")
async def adzan(client, message):
    lok = message.text.split(" ", 1)
    if len(lok) == 1:
        await message.reply_text("<blockquote><b>ᴍᴏʜᴏɴ ꜱᴇʀᴛᴀᴋᴀɴ ɴᴀᴍᴀ ᴋᴏᴛᴀ.</b></blockquote>")
        return
    lok = lok[1]
    url = f"http://muslimsalat.com/{lok}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    try:
        req = requests.get(url)
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        await message.reply_text(f"<blockquote><b>ᴇʀʀᴏʀ :</b>\n{e}</blockquote>")
        return
    result = req.json()
    txt = f"""
<blockquote><b>ᴊᴀᴅᴡᴀʟ ꜱʜᴀʟᴀᴛ ᴡɪʟᴀʏᴀʜ <u>{lok}</u></b></blockquote>
<blockquote><b>ᴛᴀɴɢɢᴀʟ <code>{result['items'][0]['date_for']}</code>
ᴋᴏᴛᴀ {result['query']} | {result['country']}</b></blockquote>

<blockquote><b>
ᴛᴇʀʙɪᴛ : <code>{result['items'][0]['shurooq']}</code>
ꜱᴜʙᴜʜ : <code>{result['items'][0]['fajr']}</code>
ᴢᴜʜᴜʀ : <code>{result['items'][0]['dhuhr']}</code>
ᴀꜱʜᴀʀ : <code>{result['items'][0]['asr']}</code>
ᴍᴀɢʜʀɪʙ : <code>{result['items'][0]['maghrib']}</code>
ɪꜱʏᴀ : <code>{result['items'][0]['isha']}</code>
</b></blockquote>
"""
    await message.reply_text(txt)
