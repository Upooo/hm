import httpx
from bs4 import BeautifulSoup
from pyrogram import Client
from pyrogram.types import Message
import random
import re
from IdolUbot import *

__MODULE__ = "pinterest"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴘɪɴᴛᴇʀᴇꜱᴛ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}pint [query]</code>
🦠 ᴋᴇᴛ : ᴍᴇɴᴄᴀʀɪ ᴅᴀɴ ᴜɴᴅᴜʜ ꜰᴏᴛᴏ ᴅᴀʀɪ ᴘɪɴᴛᴇʀᴇꜱᴛ ꜱᴇꜱᴜᴀɪ ǫᴜᴇʀʏ.</b></blockquote>
"""

IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".webp"]
EXT_REGEX = re.compile(r"https.*\.(jpg|jpeg|png|webp)")

@PY.UBOT("pint")
@PY.TOP_CMD
async def pinterest_search(client: Client, message: Message):
    query = message.text.split(maxsplit=1)[1:]
    if not query:
        return await message.reply("❌ Berikan kata kunci!\n\nContoh: <code>.pint kucing lucu</code>")
    
    keyword = query[0]
    notice = await message.reply(f"🔍 Mencari gambar Pinterest untuk: <b>{keyword}</b>")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        async with httpx.AsyncClient() as client_http:
            url = f"https://www.pinterest.com/search/pins/?q={keyword}"
            res = await client_http.get(url, headers=headers)
        
        soup = BeautifulSoup(res.text, "html.parser")
        images = []

        for img in soup.find_all("img"):
            src = img.get("src") or img.get("data-src") or ""
            if EXT_REGEX.search(src):
                images.append(src)

        if not images:
            return await notice.edit("❌ Tidak menemukan gambar yang cocok di Pinterest.")

        random.shuffle(images)
        for img in images[:5]:  # kirim 5 gambar
            await message.reply_photo(img)

        await notice.delete()

    except Exception as e:
        await notice.edit(f"❌ Gagal mengambil gambar.\n<b>{e}</b>")
