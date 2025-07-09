from pyrogram import Client
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
    InlineQuery,
)
from IdolUbot import PY, bot
import re

__MODULE__ = "button"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙᴜᴛᴛᴏɴ--</b></blockquote>

<blockquote>
🚦 ᴘᴇʀɪɴᴛᴀʜ: <code>{0}button Text | [Label1|https://link1] [Label2|https://link2]</code>
🦠 ᴄᴏɴᴛᴏʜ:
<code>{0}button Klik ini | [Google|https://google.com] [YT|https://youtube.com]</code>
</blockquote>
"""

# Simpan pesan dengan kunci (chat_id, message_id)
stored_messages = {}

def store_message(message: Message):
    key = (message.chat.id, message.id)
    stored_messages[key] = {
        "text": message.text,
        "user_id": message.from_user.id if message.from_user else 0,
    }

def get_message_by_id(chat_id: int, msg_id: int):
    return stored_messages.get((chat_id, msg_id))

# Parsing tombol dari format [Label|URL]
async def create_button(message: Message):
    try:
        full_text = message.text.split(None, 1)[1]
        if "|" not in full_text:
            return None, "❌ Format tidak valid. Gunakan: .button text | [Tombol|https://link]"

        main_text, *rest = full_text.split("|", 1)
        text = f"<b>{main_text.strip()}</b>"
        raw_buttons = rest[0] if rest else ""

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
        # Kirim query inline dengan chat_id dan message_id
        query = f"get_button {message.chat.id} {message.id}"
        result = await client.get_inline_bot_results(bot.me.username, query)

        if not result.results:
            return await message.reply("❌ Gagal kirim tombol: hasil kosong.")

        msg = message.reply_to_message or message
        await client.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=result.query_id,
            result_id=result.results[0].id,
            reply_to_message_id=msg.id
        )

    except Exception as e:
        await message.reply(f"❌ Gagal kirim tombol: {e}")

# Inline handler
@PY.INLINE("^get_button ")
async def inline_button(client: Client, inline_query: InlineQuery):
    try:
        # Ambil chat_id dan message_id dari query
        get_chat_id, get_msg_id = map(int, inline_query.query.split()[1:3])
        m = get_message_by_id(get_chat_id, get_msg_id)
        if not m:
            raise ValueError("Pesan tidak ditemukan.")

        # Dummy message untuk diparse kembali
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
