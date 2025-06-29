import ast
from pyrogram import Client, filters
from IdolUbot import *

__MODULE__ = "calc"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴀʟᴄᴜʟᴀᴛᴏʀ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}calc</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢʜɪᴛᴜɴɢ ᴇᴋꜱᴘʀᴇꜱɪ ᴍᴀᴛᴇᴍᴀᴛɪᴋᴀ.
🦠 ᴄᴏɴᴛᴏʜ : <code>{0}calc 5 + 10 * 2</code></b></blockquote>
"""

@PY.UBOT("calc")
@PY.TOP_CMD
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        return await message.reply("❌ Format salah! Gunakan: <code>.calc [ekspresi]</code>")

    expression = args[1]

    try:
        # Parsing ekspresi dengan AST (Agar lebih aman)
        result = eval(compile(ast.parse(expression, mode="eval"), "<string>", "eval"))
        await message.reply(f"✅ Hasil: <code>{result}</code>")
    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")