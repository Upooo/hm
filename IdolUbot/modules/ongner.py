from IdolUbot import *
import os
import json
import asyncio
import psutil
import random
import requests
import re
import platform
import subprocess
import sys
import traceback
import aiohttp
import filetype
import wget
import math

from datetime import datetime
from io import BytesIO, StringIO
from IdolUbot.config import OWNER_ID
import psutil
from pyrogram.enums import UserStatus
from IdolUbot import *
from pyrogram import *
from pyrogram import Client, filters
from pyrogram.types import Message
from asyncio import get_event_loop
from functools import partial
from yt_dlp import YoutubeDL
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
from pytgcalls.types.calls import Call
from pyrogram.errors import ChatAdminRequired, UserBannedInChannel
from pytgcalls.exceptions import NotInCallError
from youtubesearchpython import VideosSearch
from datetime import timedelta
from time import time
from pyrogram.errors import FloodWait, MessageNotModified
from youtubesearchpython import VideosSearch
from pyrogram.enums import ChatType
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *
from datetime import datetime
from gc import get_objects
from time import time
from pyrogram.raw import *
from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot
from bs4 import BeautifulSoup
from io import BytesIO
from pyrogram.errors.exceptions import *
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from httpx import AsyncClient, Timeout
from IdolUbot import *

@PY.IDOL("climit")
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    pong = await EMO.PING(client)
    tion = await EMO.MENTION(client)
    yubot = await EMO.UBOT(client)
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    msg = await message.reply(f"{prs}processing . . .")
    response = await client.invoke(
        StartBot(
            bot=bot_info,
            peer=bot_info,
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    await sleep(1)
    await msg.delete()
    status = await client.get_messages("SpamBot", response.updates[1].message.id + 1) 
    if status and hasattr(status, "text"):
        pjg = len(status.text)
        print(pjg)
        if pjg <= 100:
            if client.me.is_premium:
                text = f"""
<blockquote><b>{pong} sᴛᴀᴛᴜs ᴀᴋᴜɴ ᴘʀᴇᴍɪᴜᴍ : ᴛʀᴜᴇ</b>
<b>{tion} ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ᴅɪʙᴀᴛᴀsɪ</b>
<b>{yubot} ᴜʙᴏᴛ : {bot.me.mention}</b></blockquote>
"""
            else:
                text = f"""
<blockquote><b>sᴛᴀᴛᴜs ᴀᴋᴜɴ  : ʙᴇʟɪ ᴘʀᴇᴍ ᴅᴜʟᴜ ʏᴀ</b>
<b>ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ᴅɪʙᴀᴛᴀsɪ</b>
<b>ᴜʙᴏᴛ : {bot.me.mention}</b></blockquote>
 """
            await client.send_message(message.chat.id, text)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
        else:
            if client.me.is_premium:
                text = f"""
<blockquote><b>{pong} sᴛᴀᴛᴜs ᴀᴋᴜɴ ᴘʀᴇᴍɪᴜᴍ : ᴛʀᴜᴇ</b>
<b>{tion} ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴀɴᴅᴀ ʙᴇʀᴍᴀsᴀʟᴀʜ</b> 
<b>{yubot} ᴜʙᴏᴛ : {bot.me.mention}</b></blockquote>
"""
            else:
                text = f"""
<blockquote><b>sᴛᴀᴛᴜs ᴀᴋᴜɴ  : ʙᴇʟɪ ᴘʀᴇᴍ ᴅᴜʟᴜ ʏᴀ</b>
<b>ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴀɴᴅᴀ ʙᴇʀᴍᴀsᴀʟᴀʜ</b>
<b>ᴜʙᴏᴛ : {bot.me.mention}</b></blockquote>
"""
            await client.send_message(message.chat.id, text)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
    else:
        print("Status tidak valid atau status.text tidak ada")

@PY.IDOL("HALLO")
async def padaonga(client, message):
    await message.reply(
        "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
        "██████▄▄█‡‡‡‡‡‡████████▄\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
        "█████‡‡‡‡‡‡‡██████████\n")
    
@PY.IDOL("hai")
async def moiregantenkga(client, message):
    await message.reply(
       "<blockquote><b>KENAPA GANTENG??</blockquote></b>")

@PY.IDOL("devs")
async def teson(client, message):
    await message.reply(
       "<blockquote><b>DEVS GACOL IDAMAN YA NATHAN LAHH!!</blockquote></b>")

@PY.IDOL("idol")
async def teson(client, message):
    await message.reply(
       "IDOL USERBOT MENYALA!!!")

@PY.IDOL("ubot")
async def teson(client, message):
    await message.reply(
       "<blockquote><b> USERBOT GACOL IDAMAN CUMA @v1idolubot </blockquote></b>")
       
@PY.IDOL("tes")
async def teson(client, message):
    await message.reply(
       "<blockquote><b>always on mas nathann.</blockquote></b>")
                  
@PY.IDOL("kuda")
async def _(client, message):
    await message.react("🦄")
    
@PY.IDOL("anjing")
async def _(client, message):
    await message.react("🗿")
    
@PY.IDOL("asu")
async def _(client, message):
    await message.react("😭")
    
@PY.IDOL("love")
async def _(client, message):
    await message.react("❤")

@PY.IDOL("sip")
async def _(client, message):
    await message.react("👍")

@PY.IDOL("ok")
async def _(client, message):
    await message.react("👌")

@PY.IDOL("haha")
async def _(client, message):
    await message.react("😹")

@PY.IDOL("p")
async def _(client, message):
    await message.react("👋")

@PY.IDOL("wow")
async def _(client, message):
    await message.react("😨")
