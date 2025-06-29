from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot
from pyrogram.errors.exceptions import *

from IdolUbot import *

__MODULE__ = "limit"
__HELP__ = """
perintah : <code>{0}limit</code>
    mengecek status akun apakah terkena limit atau tidak
"""