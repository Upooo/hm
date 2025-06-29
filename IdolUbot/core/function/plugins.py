import importlib
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from IdolUbot import bot, ubot
from IdolUbot.core.helpers import PY
from IdolUbot.modules import loadModule
from IdolUbot.core.database import *
from IdolUbot.config import LOGS_MAKER_UBOT
from platform import python_version
from pyrogram import __version__
HELP_COMMANDS = {}


async def loadPlugins():
    modules = loadModule()
    for mod in modules:
        imported_module = importlib.import_module(f"IdolUbot.modules.{mod}")
        module_name = getattr(imported_module, "__MODULE__", "").replace(" ", "_").lower()
        if module_name:
            HELP_COMMANDS[module_name] = imported_module
    print(f"[🤖 ᴜsᴇʀʙᴏᴛ 🤖] [💠 TELAH BERHASIL DIAKTIFKAN THAN! 💠]")
    await bot.send_message(
        LOGS_MAKER_UBOT, 
       f"""                    
<blockquote>» <b><u>[ɪᴅᴏʟ ᴜꜱᴇʀʙᴏᴛ](https://t.me/idolubot)</u></b> sᴛᴀʀᴛᴇᴅ :
     <b>ɪᴅ : 5870285414</b>
     <b>ɴᴀᴍᴇ : ɪᴅᴏʟ ᴜꜱᴇʀʙᴏᴛ
     <b>ᴛᴏᴛᴀʟ ᴍᴏᴅᴜʟᴇs : {len(HELP_COMMANDS)}</b>
     <b>ᴛᴏᴛᴀʟ ᴘᴇɴɢɢᴜɴᴀ : {len(ubot._ubot)}</b>
     <b>ᴜsᴇʀɴᴀᴍᴇ : @idolubot</b></blockquote>
""",
   reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴜsᴇʀʙᴏᴛ", url="t.me/idolubot"),
                    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/xnxxnathan"),
                ],
            ]
        ),
    )
    
@PY.CALLBACK("0_cls")
async def _(client, callback_query):
    await callback_query.message.delete()
