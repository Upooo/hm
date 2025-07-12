import random
from pyrogram.enums import MessagesFilter
from IdolUbot import *

__MODULE__ = "naruto"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɴᴀʀᴜᴛᴏ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}ns [query]</code>
🦠 ᴋᴇᴛ : ᴍᴇɴᴄᴀʀɪ ꜰᴏᴛᴏ ᴀɴɪᴍᴀꜱɪ ɴᴀʀᴜᴛᴏ ꜱᴇꜱᴜᴀɪ ǫᴜᴇʀʏ.</b></blockquote>
<blockquote><b>❏ ǫᴜᴇʀʏ:
├ <code>{0}ns naruto</code>
├ <code>{0}ns boruto</code>
├ <code>{0}ns hiruka</code>
├ <code>{0}ns tsunade</code>
├ <code>{0}ns sakura</code>
├ <code>{0}ns hinata</code>
├ <code>{0}ns sasuke</code>
╰ <code>{0}ns kakashi</code></b></blockquote>
"""

@PY.UBOT("ns")
@PY.TOP_CMD
async def gambar_asupan(client, message):
    query = message.text.split(maxsplit=1)
    if len(query) < 2:
        return await message.reply("<b>❌ Masukkan query anime, contoh:</b> <code>ns naruoto</code>")

    keyword = query[1].lower()

    # Mapping query ke channel-channel anime
    CHANNEL_MAP = {
        "naruto": "@narutoidol",
        "boruto": "@borutoahah",
        "hiruka": "@hirukaidol",
        "tsunade": "@tsunadebahenol",
        "sakura": "@bungasakurkur",
        "hinata": "@sexhinata",
        "sasuke": "@sasukecabul",
        "kakashi": "@kakashiQu",
    }

    if keyword not in CHANNEL_MAP:
        return await message.reply("<b>❌ Query tidak dikenali. Gunakan salah satu:</b>\n"
                                   "<code>naruoto, boruto, hiruka, tsunade, sakura, hinata, sasuke, kakashi</code>")

    channel_username = CHANNEL_MAP[keyword]
    loading = await message.reply("🖼️ Sedang mencari gambar...")

    try:
        photos = []
        async for msg in client.search_messages(channel_username, filter=MessagesFilter.PHOTO):
            photos.append(msg)

        if not photos:
            return await loading.edit("❌ Tidak ditemukan gambar di channel tersebut.")

        random_photo = random.choice(photos)
        await random_photo.copy(message.chat.id, reply_to_message_id=message.id)
        await loading.delete()

    except Exception as e:
        await loading.edit(f"❌ Terjadi kesalahan:\n<code>{e}</code>")
