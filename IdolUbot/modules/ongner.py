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

@PY.IDOL("devs")
async def teson(client, message):
    await message.reply(
       "<blockquote><b>SI GANTENG GACOL IDAMAN YA NATHAN LAHH!!</blockquote></b>")

@PY.IDOL("idolubot")
async def teson(client, message):
    await message.reply(
       "<b>MENYALA IDOL USERBOT!!!</b>")

@PY.IDOL("ubots")
async def teson(client, message):
    await message.reply(
       f"<blockquote><b> USERBOT GACOL IDAMAN CUMA @{bot.me.username} </blockquote></b>")
       
@PY.IDOL("cek")
async def teson(client, message):
    await message.reply(
       "<blockquote><b>ALWAYS ON TUAN NATHAN!!</blockquote></b>")
                  
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
