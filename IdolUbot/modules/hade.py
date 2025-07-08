__MODULE__ = "remini"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʜᴅ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}hd</code> (ʀᴇᴘʟʏ ꜰᴏᴛᴏ)
🦠 ᴋᴇᴛ : ᴍᴇɴɪɴɢᴋᴀᴛᴋᴀɴ ᴋᴜᴀʟɪᴛᴀꜱ ɢᴀᴍʙᴀʀ ᴅᴇɴɢᴀɴ ᴀʟɢᴏʀɪᴛᴍᴀ ʀᴇᴍɪɴɪ / ʜᴅ.</blockquote>
"""


import requests
import os
from IdolUbot import *
from pyrogram.types import Message
from tempfile import NamedTemporaryFile

def remini(image_path, model_type="enhance"):
    valid_models = ["enhance", "recolor", "dehaze"]
    if model_type not in valid_models:
        model_type = "enhance"

    url = f"https://inferenceengine.vyro.ai/{model_type}"
    with open(image_path, "rb") as img_file:
        files = {
            "model_version": (None, "1"),
            "image": ("enhance_image_body.jpg", img_file, "image/jpeg"),
        }
        headers = {
            "User-Agent": "okhttp/4.9.3",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
        }

        try:
            response = requests.post(url, files=files, headers=headers, timeout=20)
        except requests.exceptions.Timeout:
            raise Exception("⏱️ Timeout saat menghubungi server Remini.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"🔌 Gagal menghubungi server: {e}")

    if response.status_code == 200:
        return response.content
    else:
        raise Exception(
            f"❌ Gagal: Status {response.status_code} - {response.text}"
        )

@PY.UBOT("remini|hd")
@PY.TOP_CMD
async def process_image(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.reply("📸 Balas ke gambar yang ingin di-HD-kan.")

    status_msg = await message.reply("⏳ Memproses...")

    try:
        file_path = await message.reply_to_message.download()

        enhanced_image = remini(file_path, "enhance")

        with NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
            tmp_file.write(enhanced_image)
            tmp_path = tmp_file.name

        await client.send_photo(
            chat_id=message.chat.id,
            photo=tmp_path,
            caption="✅ Selesai di-HD-kan oleh AI Remini.",
            reply_to_message_id=message.id,
        )

        await status_msg.delete()
        os.remove(tmp_path)
        os.remove(file_path)
    except Exception as e:
        await status_msg.edit(f"❌ Terjadi kesalahan:\n`{e}`")