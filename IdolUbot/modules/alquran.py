__MODULE__ = "alquran"
__HELP__ = f"""
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀʟ ǫᴜʀ'ᴀɴ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}alquran [ꜱᴜʀᴀʜ] [ᴀʏᴀᴛ]</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ꜱᴇᴀʀᴄʜ ᴀʏᴀᴛ ᴀʟ ǫᴜʀ'ᴀɴ.</b></blockquote>
<blockquote><b>ᴄᴏɴᴛᴏʜ : <code>{0}alquran 1 2</code></b></blockquote>
"""

import aiohttp
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from IdolUbot import *

async def alquran(surah, ayat):
    url = f"https://kalam.sindonews.com/ayat/{ayat}/{surah}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            if res.status != 200:
                raise Exception("Error, maybe not found?")
            text = await res.text()
            soup = BeautifulSoup(text, "html.parser")
            
            content = soup.select_one("body > main > div > div.content.clearfix > div.news > section > div.list-content.clearfix")
            surah_name = content.select_one("div.ayat-title > h1").get_text(strip=True)
            arab = content.select_one("div.ayat-detail > div.ayat-arab").get_text(strip=True)
            latin = content.select_one("div.ayat-detail > div.ayat-latin").get_text(strip=True)
            terjemahan = content.select_one("div.ayat-detail > div.ayat-detail-text").get_text(strip=True)
            tafsir = "\n".join([t.get_text(strip=True) for t in content.select("div.ayat-detail > div.tafsir-box > div")]).strip()
            keterangan = content.select_one("div.ayat-detail > div.ayat-summary").get_text(strip=True)
            audio = f"https://raw.githubusercontent.com/AyGemuy/quran-json/main/Audio/{surah:03}/{ayat:03}.mp3"
            
            return {
                "surah": surah_name,
                "arab": arab,
                "latin": latin,
                "terjemahan": terjemahan,
                "tafsir": tafsir,
                "audio": audio,
                "keterangan": keterangan
            }

@PY.UBOT("alquran")
async def send_quran(client, message):
    ggl = await EMO.GAGAL(client)
    try:
        args = message.command[1:]
        if len(args) < 2 or not args[0].isdigit() or not args[1].isdigit():
            await message.reply_text(f"<blockquote><b>{ggl} ᴄᴏɴᴛᴏʜ :\n .alquran 1 2\n\nᴍᴀᴋᴀ ʜᴀꜱɪʟɴʏᴀ ᴀᴅᴀʟᴀʜ ꜱᴜʀᴀʜ ᴀʟ-ꜰᴀᴛɪʜᴀʜ ᴀʏᴀᴛ 2</b></blockquote>")
            return
        
        surah = int(args[0])
        ayat = int(args[1])
        result = await alquran(surah, ayat)

        quran_text = f"""
<blockquote>{result['arab']}
<b>{result['latin']}</b>

<b>ᴀʀᴛɪɴʏᴀ : {result['terjemahan']}</b>

<b>( {result['surah']} )</b></blockquote>
"""
        await message.reply_text(quran_text.strip())
        
        await client.send_audio(
            chat_id=message.chat.id,
            audio=result["audio"],
            caption=f"( {result['surah']} )",
            title="Quran Audio",
            file_name="vn.mp3"
        )

    except Exception as e:
        await message.reply_text(f"ᴇʀʀᴏʀ : {str(e)}")
