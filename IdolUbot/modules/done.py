import asyncio
import datetime

from IdolUbot import *

__MODULE__ = "done"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴅᴏɴᴇ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}done [nama item], [harga] [pembayaran]</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢᴋᴏɴꜰɪʀᴍᴀꜱɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ.</b></blockquote>
"""



@PY.UBOT("done")
async def done_command(client, message):
    izzy_ganteng = await message.reply("<blockquote>memproses...</blockquote>")
    await asyncio.sleep(5)
    try:
        args = message.text.split(" ", 1)
        if len(args) < 2 or "," not in args[1]:
            await message.reply_text("<blockquote>Penggunaan: .done name item,price,payment</blockquote>")
            return

        parts = args[1].split(",", 2)

        if len(parts) < 2:
            await message.reply_text("<blockquote>Penggunaan: .done name item,price,payment</blockquote>")
            return

        name_item = parts[0].strip()
        price = parts[1].strip()
        payment = parts[2].strip() if len(parts) > 2 else "Lainnya"
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = (
            f"<blockquote><b>「 ɪᴅᴏʟ ᴛʀᴀɴꜱᴀᴄᴛɪᴏɴ ꜱᴜᴄᴄᴇꜱꜱ 」</b>\n</blockquote>"
            f"<blockquote>📦 <b>ʙᴀʀᴀɴɢ : {name_item}</b>\n"
            f"💸 <b>ʜᴀʀɢᴀ : {price}</b>\n"
            f"🕰️ <b>ᴡᴀᴋᴛᴜ : {time}</b>\n"
            f"💬 <b>ᴘᴀʏᴍᴇɴᴛ : {payment}</b>\n</blockquote>"
            f"<blockquote><b>ᴛᴇʀɪᴍᴀᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴏʀᴅᴇʀ</b></blockquote>"
        )
        await izzy_ganteng.edit(response)

    except Exception as e:
        await izzy_ganteng.edit(f"error: {e}")
