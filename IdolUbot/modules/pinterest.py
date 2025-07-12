import httpx
from bs4 import BeautifulSoup
from pyrogram import Client
from pyrogram.types import Message
import random
from IdolUbot import *

__MODULE__ = "pinterest"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘɪɴᴛᴇʀᴇꜱᴛ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}pint [query]</code>
🦠 ᴋᴇᴛ : ᴍᴇɴᴄᴀʀɪ ᴅᴀɴ ᴜɴᴅᴜʜ ꜰᴏᴛᴏ ᴅᴀʀɪ ᴘɪɴᴛᴇʀᴇꜱᴛ ꜱᴇꜱᴜᴀɪ ǫᴜᴇʀʏ.</b></blockquote>
"""

@PY.UBOT("pint")
@PY.TOP_CMD
async def pinterest_search(client: Client, message: Message):
    query = message.text.split(maxsplit=1)[1:]
    if not query:
        return await message.reply("❌ Berikan kata kunci!\n\nContoh: <code>.pinterest kucing lucu</code>")
    
    keyword = query[0]
    await message.reply(f"🔍 Mencari gambar dari Pinterest untuk : <b>{keyword}</b>")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        async with httpx.AsyncClient() as client_http:
            url = f"https://www.pinterest.com/search/pins/?q={keyword}"
            res = await client_http.get(url, headers=headers)

        soup = BeautifulSoup(res.text, "html.parser")
        images = []

        for img_tag in soup.find_all("img"):
            src = img_tag.get("src")
            if src and "236x" in src:
                images.append(src)

        if not images:
            return await message.reply("❌ Gambar tidak ditemukan.")

        random.shuffle(images)
        for img in images[:3]:
            await message.reply_photo(img)

    except Exception as e:
        await message.reply(f"❌ Gagal mengambil gambar.\n{e}")
