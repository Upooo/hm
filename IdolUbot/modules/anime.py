__MODULE__ = "anime"
__HELP__ = f"""
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀᴅᴢᴀɴ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}wall</code> ᴀɴᴅ <code>{0}waifu</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴀɴɪᴍᴇ ʀᴀɴᴅᴏᴍ.</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}anime</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴀɴɪᴍᴇ ʀᴀɴᴅᴏᴍ.</b></blockquote>
"""

import requests

from IdolUbot import *
from pyrogram.enums import *
from pyrogram import *
from pyrogram.types import *
from io import BytesIO


URLS = {
    "keneki": "https://api.botcahx.eu.org/api/anime/keneki?apikey=moire",
    "megumin": "https://api.botcahx.eu.org/api/anime/megumin?apikey=moire",
    "yotsuba": "https://api.botcahx.eu.org/api/anime/yotsuba?apikey=moire",
    "shinomiya": "https://api.botcahx.eu.org/api/anime/shinomiya?apikey=moire",
    "yumeko": "https://api.botcahx.eu.org/api/anime/yumeko?apikey=moire",
    "tsunade": "https://api.botcahx.eu.org/api/anime/tsunade?apikey=moire",
    "kagura": "https://api.botcahx.eu.org/api/anime/kagura?apikey=moire",
    "madara": "https://api.botcahx.eu.org/api/anime/madara?apikey=moire",
    "itachi": "https://api.botcahx.eu.org/api/anime/itachi?apikey=moire",
    "akira": "https://api.botcahx.eu.org/api/anime/akira?apikey=moire",
    "toukachan": "https://api.botcahx.eu.org/api/anime/toukachan?apikey=moire",
    "cicho": "https://api.botcahx.eu.org/api/anime/chiho?apikey=moire",
    "sasuke": "https://api.botcahx.eu.org/api/anime/sasuke?apikey=moire"
}
ANMK = ANIMEK.a + ANIMEK.b

@PY.UBOT(ANMK)
async def anime_cmd(client, message):
    msg = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ...</b>", quote=True)
    if message.command[0] == "wall":
        photo = await API.wall(client)
        try:
            await photo.copy(message.chat.id, reply_to_message_id=message.id)
            return await msg.delete()
        except Exception as error:
            return await msg.edit(error)
    elif message.command[0] == "waifu":
        photo = API.waifu()
        try:
            await message.reply_photo(photo, quote=True)
            return await msg.delete()
        except Exception as error:
            return await msg.edit(error)

@PY.UBOT("anime")
@PY.TOP_CMD
async def _(client, message):
    # Extract query from message
    query = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if query not in URLS:
        valid_queries = ", ".join(URLS.keys())
        await message.reply(f"<blockquote><b>ǫᴜᴇʀʏ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ. ɢᴜɴᴀᴋᴀɴ ꜱᴀʟᴀʜ ꜱᴀᴛᴜ ᴅᴀʀɪ :</b></blockquote>\n<blockquote><b>{valid_queries}.</b></blockquote>")
        return

    processing_msg = await message.reply("<blockquote><b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ...</b></blockquote>")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query])
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'image.jpg'
        
        await client.send_photo(message.chat.id, photo)
        await processing_msg.delete()
    except requests.exceptions.RequestException as e:
        await processing_msg.edit_text(f"<blockquote><b>ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ɢᴀᴍʙᴀʀ ᴀɴɪᴍᴇ ᴇʀʀᴏʀ :</b></blockquote>\n<blockquote><b>{e}</b></blockquote>")
