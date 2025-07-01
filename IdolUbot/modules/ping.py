import os
import json
import asyncio
import psutil
# import speedtest

from datetime import datetime
from gc import get_objects
from time import time

from pyrogram.raw import *
from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from IdolUbot import *

@PY.UBOT("ping|pink")
@PY.IDOL("cpink|ceponk|sepong")
@PY.TOP_CMD
async def _(client, message):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    uptime = await get_time((time() - start_time))
    delta_ping_formatted = round((end - start).microseconds / 100000000000000, 0)
    pong = await EMO.PING(client)
    tion = await EMO.MENTION(client)
    yubot = await EMO.UBOT(client)
    pantek = await STR.PONG(client)
    ngentod = await STR.OWNER(client)
    kontol = await STR.UBOT(client)
    babi = client.me.is_premium
    if babi:
        _ping = f"""
<blockquote><b>{pong} {pantek} :</b> {str(delta_ping_formatted).replace('.', ',')} ms</blockquote>
<blockquote><b>{tion} {ngentod} :</b>  <code>{client.me.mention}</code>
<b>{yubot} {kontol} : {bot.me.mention}</b></blockquote>
"""
    else:
        _ping = f"""
<blockquote><b>{pantek} :</b> {str(delta_ping_formatted).replace('.', ',')} ms</blockquote>
<blockquote><b>{ngentod} :</b>  <code>{client.me.mention}</code>
<b>{kontol} : {bot.me.mention}</b></blockquote>
"""
    await message.reply(_ping)