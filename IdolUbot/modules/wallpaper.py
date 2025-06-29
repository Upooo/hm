__MODULE__ = "wallpaper"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴡᴀʟʟᴘᴀᴘᴇʀ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}wall [query]</code>
🦠 ᴋᴇᴛ : ᴍᴇɴᴄᴀʀɪ ɪɴꜰᴏʀᴍᴀꜱɪ ᴛᴇɴᴛᴀɴɢ ʙᴇʀʙᴀɢᴀɪ ᴛᴏᴘɪᴋ, ᴍᴜʟᴀɪ ᴅᴀʀɪ ꜱᴇᴊᴀʀᴀʜ, ꜱᴀɪɴꜱ, ʙᴜᴅᴀʏᴀ, ʜɪɴɢɢᴀ ᴛᴇᴋɴᴏʟᴏɢɪ.

❏ ǫᴜᴇʀʏ :
├ ᴛᴇᴋɴᴏʟᴏɢɪ
├ ᴀᴇsᴛʜᴇᴛɪᴄ
├ ᴋᴀᴛᴀᴋᴀᴛᴀ   
├ ʜᴇᴋᴇʀ   
├ ᴛᴇᴋɴᴏʟᴏɢɪ
├ ᴀɴᴊɪɴɢ     
├ ʜᴘ 
├ ɢᴀᴍᴇʀ 
├ ᴘʀᴏɢᴀᴍɪɴɢ  
├ ᴄʜᴜᴋʏ 
╰ ᴋᴜᴄɪɴɢ</b></blockquote>
"""

from IdolUbot import *
import random
import requests
from pyrogram.enums import *
from pyrogram import *
from pyrogram.types import *
from io import BytesIO

URLS = {
    "teknologi": "https://api.botcahx.eu.org/api/wallpaper/teknologi?apikey=moire",
    "aesthetic": "https://api.botcahx.eu.org/api/wallpaper/aesthetic?apikey=moire",
    "katakata": "https://api.botcahx.eu.org/api/wallpaper/katakata?apikey=moire",
    "heker": "https://api.botcahx.eu.org/api/wallpaper/hacker?apikey=moire",
    "anjing": "https://api.botcahx.eu.org/api/wallpaper/anjing?apikey=moire",
    "hp": "https://api.botcahx.eu.org/api/wallpaper/wallhp?apikey=moire",
    "gamer": "https://api.botcahx.eu.org/api/wallpaper/gaming?apikey=moire",
    "progaming": "https://api.botcahx.eu.org/api/wallpaper/programing?apikey=moire",
    "chuky": "https://api.botcahx.eu.org/api/wallpaper/boneka-chucky?apikey=moire",
    "kucing": "https://api.botcahx.eu.org/api/wallpaper/kucing?apikey=moire",
    }


@PY.UBOT("wall")
@PY.TOP_CMD
async def _(client, message):
    # Extract query from message
    query = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if query not in URLS:
        valid_queries = ", ".join(URLS.keys())
        await message.reply(f"<blockquote><b>ǫᴜᴇʀʏ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ. ɢᴜɴᴀᴋᴀɴ ꜱᴀʟᴀʜ ꜱᴀᴛᴜ ᴅᴀʀɪ: {valid_queries}.</b></blockquote>")
        return

    processing_msg = await message.reply("ᴘʀᴏᴄᴇꜱɪɴɢ...")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query])
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'image.jpg'
        
        await client.send_photo(message.chat.id, photo)
        await processing_msg.delete()
    except requests.exceptions.RequestException as e:
        await processing_msg.edit_text(f"<blockquote><b>ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ɢᴀᴍʙᴀʀ ᴀɴɪᴍᴇ ᴇʀʀᴏʀ: {e}</b></blockquote>")
