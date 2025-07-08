from pyrogram import Client
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
    InlineQuery,
)
from IdolUbot import *

__MODULE__ = "button"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙᴜᴛᴛᴏɴ--</b></blockquote>

<blockquote>
🚦 ᴘᴇʀɪɴᴛᴀʜ: <code>{0}button Text | [Label1|https://link1] [Label2|https://link2]</code>
🦠 ᴄᴏɴᴛᴏʜ:
<code>{0}button Klik ini | [Google|https://google.com] [YT|https://youtube.com]</code>
</blockquote>
"""

# Simpan pesan yang akan diakses via inline
stored_messages = {}

def store_message(message: Message):
    stored_messages[id(message)] = {
        "text": message.text,
        "user_id": message.from_user.id if message.from_user else 0,
    }

def get_message_by_id(msg_id: int):
    return stored_messages.get(msg_id)

# Fungsi parsing tombol dari format [Label|URL]
import re
async def create_button(message: Message):
    try:
        full_text = message.text.split(None, 1)[1]
        if "|" not in full_text:
            return None, "❌ Format tidak valid. Gunakan: .button text | [Tombol|https://link]"

        main_text, *rest = full_text.split("|", 1)
        text = f"<b>{main_text.strip()}</b>"
        raw_buttons = rest[0] if rest else ""

        # Parsing tombol dengan regex
        button_matches = re.findall(r"\[([^\[\]|]+)\|([^\[\]|]+)\]", raw_buttons)
        if not button_matches:
            return None, "❌ Tidak ada tombol valid ditemukan."

        buttons = [[InlineKeyboardButton(label.strip(), url.strip())] for label, url in button_matches]
        return InlineKeyboardMarkup(buttons), text

    except Exception as e:
        return None, f"❌ Gagal parsing tombol: {e}"

# Perintah utama: .button
@PY.UBOT("button")
async def cmd_button(client: Client, message: Message):
    if len(message.command) < 2 or "|" not in message.text:
        return await message.reply(
            "📌 Format salah!\nContoh:\n<code>.button Halo | [Tombol|https://link]</code>"
        )

    # Simpan pesan
    store_message(message)
    await message.delete()

    try:
        result = await client.get_inline_bot_results(
            bot.me.username, f"get_button {id(message)}"
        )
        msg = message.reply_to_message or message
        await client.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=result.query_id,
            result_id=result.results[0].id,
            reply_to_message_id=msg.id
        )
    except Exception as e:
        await message.reply(f"❌ Gagal kirim tombol: {e}")

# Inline Handler
@PY.INLINE("^get_button")
async def inline_button(client: Client, inline_query: InlineQuery):
    try:
        get_id = int(inline_query.query.split(None, 1)[1])
        m = get_message_by_id(get_id)
        if not m:
            raise ValueError("Pesan tidak ditemukan.")

        # Buat dummy message dengan atribut text
        class DummyMessage:
            def __init__(self, text):
                self.text = text
        dm = DummyMessage(m["text"])

        buttons, text = await create_button(dm)
        if not buttons:
            raise ValueError("Gagal buat tombol.")

        await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                InlineQueryResultArticle(
                    title="✅ Tombol Siap",
                    input_message_content=InputTextMessageContent(text, parse_mode="html"),
                    reply_markup=buttons,
                )
            ],
        )
    except Exception as e:
        await client.answer_inline_query(
            inline_query.id,
            results=[],
            switch_pm_text=f"⚠️ Error: {e}",
            switch_pm_parameter="start"
        )
