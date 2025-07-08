from pyrogram import Client, filters
from pyrogram.errors import (
    UsernameNotOccupied,
    UserNotParticipant,
    PeerIdInvalid
)
from IdolUbot import *

__MODULE__ = "profile"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴏꜰɪʟ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}getpp</code> (ʀᴇᴘʟʏ ᴄʜᴀᴛ)
🦠 ᴋᴇᴛ : ᴍᴇɴɢᴀᴍʙɪʟ ꜰᴏᴛᴏ ᴘʀᴏꜰɪʟ ᴅᴀʀɪ sᴇsᴇᴏʀᴀɴɢ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}setpp</code> (ʀᴇᴘʟʏ ᴍᴇᴅɪᴀ)
🦠 ᴋᴇᴛ : ᴍᴇɴɢɢᴀɴᴛɪ ꜰᴏᴛᴏ ᴘʀᴏꜰɪʟ ᴀᴋᴜɴ ᴍᴜ ᴅᴇɴɢᴀɴ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ᴅɪʀᴇᴘʟʏ.</blockquote>
"""


@PY.UBOT("getpp|getprofile")
async def get_profile_pic(client, message):
    target = None

    if message.reply_to_message:
        target = message.reply_to_message.from_user.id

    elif len(message.command) > 1:
        target = message.command[1]

    else:
        target = message.chat.id
        
    if not target:
        return await message.reply_text("**__Gunakan `/getpp @username`, reply user, atau kirim `.getpp` di grup/channel untuk ambil PP.__**")

    try:
        async for photo in client.get_chat_photos(target, limit=1):  # Ambil 1 foto terbaru
            await client.send_photo(
                message.chat.id,
                photo=photo.file_id,
                caption="<pre>Done✅</pre>"
            )
            return

        await message.reply_text("**__User/grup tidak memiliki foto profil__**.")

    except (UsernameNotOccupied, UserNotParticipant, PeerIdInvalid):
        await message.reply_text("**__Akun atau grup tidak ditemukan.__**")
    except Exception as e:
        await message.reply_text(f"**__Terjadi kesalahan: {str(e)}__**")

@PY.UBOT("setpp")
async def set_profile_photo(client, message):
    if not message.reply_to_message:
        return await message.reply_text("**Balas ke foto atau media yang ingin dijadikan PP.**")

    media = message.reply_to_message

    try:
        if media.photo:
            file = await media.download()
        elif media.document and ("image" in media.document.mime_type):
            file = await media.download()
        elif media.video and media.video.thumbs:
            file = await client.download_media(media.video.thumbs[0].file_id)
        else:
            return await message.reply_text("**Media tidak valid. Balas ke foto atau file gambar.**")

        await client.set_profile_photo(photo=file)
        await message.reply_text("✅ **Foto profil berhasil diubah.**")

    except Exception as e:
        await message.reply_text(f"❌ **Gagal mengatur foto profil:** `{str(e)}`")
