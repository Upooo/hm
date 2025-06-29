from pyrogram import Client
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
    InlineQuery,
)
from IdolUbot import PY

__MODULE__ = "button"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙᴜᴛᴛᴏɴ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}button Text | [Tombol 1|https://link]</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴏᴍʙᴏʟ ɪɴʟɪɴᴇ, ɢᴜɴᴀᴋᴀɴ ꜱᴘᴀꜱɪ ᴊɪᴋᴀ ʟᴇʙɪʜ ᴅᴀʀɪ ꜱᴀᴛᴜ ᴛᴏᴍʙᴏʟ.</b></blockquote>
"""

stored_messages = []

def get_objects():
    return stored_messages

# Fungsi parsing tombol dari format [text|link]
async def create_button(message: Message):
    try:
        full_text = message.text.split(None, 1)[1]
        if "|" not in full_text:
            return None, "❌ Format tidak valid."

        main_text, raw_buttons = full_text.split("|", 1)
        text = f"<code><b>{main_text.strip()}</b></code>"

        # Parsing tombol seperti [label|url]
        buttons = []
        for btn in raw_buttons.strip().split("]["):
            btn = btn.strip("[] ")
            if "|" in btn:
                label, url = btn.split("|", 1)
                buttons.append([InlineKeyboardButton(label.strip(), url.strip())])

        return InlineKeyboardMarkup(buttons), text

    except Exception as e:
        return None, f"❌ Gagal parsing tombol: {e}"

# Perintah `.button`
@PY.UBOT("button")
async def cmd_button(client: Client, message: Message):
    if len(message.command) < 2 or "|" not in message.text:
        return await message.reply(
            "📌 Contoh:\n<code>.button ayo join | [tombol1|https://link]</code>"
        )

    stored_messages.append(message)
    await message.delete()

    try:
        result = await client.get_inline_bot_results(
            client.me.username, f"get_button {id(message)}"
        )
        msg = message.reply_to_message or message
        await client.send_inline_bot_result(
            message.chat.id,
            result.query_id,
            result.results[0].id,
            reply_to_message_id=msg.id
        )
    except Exception as error:
        await message.reply(str(error))

# Inline handler
@PY.INLINE("^get_button")
async def inline_button(client: Client, inline_query: InlineQuery):
    try:
        get_id = int(inline_query.query.split(None, 1)[1])
        m = next((obj for obj in get_objects() if id(obj) == get_id), None)
        if not m:
            raise ValueError("Message tidak ditemukan")

        buttons, text = await create_button(m)
        if not buttons:
            raise ValueError("Tombol tidak valid")

        await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                InlineQueryResultArticle(
                    title="✅ Tombol Siap",
                    input_message_content=InputTextMessageContent(text),
                    reply_markup=buttons
                )
            ]
        )
    except Exception as e:
        await client.answer_inline_query(
            inline_query.id,
            results=[],
            switch_pm_text=f"⚠️ Error: {e}",
            switch_pm_parameter="start"
        )
