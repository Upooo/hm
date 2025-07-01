__MODULE__ = "animasi"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɴɪᴍᴀsɪ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b>
🦠 <code>{0}dinoo</code>
🦠 <code>{0}awk</code>
🦠 <code>{0}loveyou</code>
🦠 <code>{0}ange</code>
🦠 <code>{0}hmm</code>
🦠 <code>{0}lipkol</code>
🦠 <code>{0}kntl</code>
🦠 <code>{0}ajg</code>
🦠 <code>{0}kocok</code>
🦠 <code>{0}heli</code>
🦠 <code>{0}y</code>
🦠 <code>{0}nakal</code>
🦠 <code>{0}tank</code>
🦠 <code>{0}nah</code>
🦠 <code>{0}tembak</code>
🦠 <code>{0}piss</code>
🦠 <code>{0}bundir</code>
🦠 <code>{0}bot</code>
🦠 <code>{0}sepongebob</code>
🦠 <code>{0}dino</code>
🦠 <code>{0}hack</code>
🦠 <code>{0}gabut</code>
🦠 <code>{0}loveyou</code>
🦠 <code>{0}bomb</code>
🦠 <code>{0}charge</code>
🦠 <code>{0}fadmin</code>
🦠 <code>{0}fleave</code>
🦠 <code>{0}tupload</code>
🦠 <code>{0}hadiah</code>
🦠 <code>{0}polisi</code></blockquote>
"""


import asyncio
import random

import requests
from pyrogram import *
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *

from IdolUbot import *

DEFAULTUSER = "nathan"
NOBLE = [
    "╲╲╲┏┓╭╮╱╱╱\n╲╲╲┗┓┏┛┃╭╮┃╱╱╱\n╲╲╲╲┃┃┏┫┃╭┻┻┓╱╱\n╱╱╱┏╯╰╯┃╰┫┏╯╱╱\n╱╱┏┻┳┳┻┫┗┓╱╱╱\n╱╱╰┓┃┃╲┏┫┏┛╲╲╲\n╱╱╱╱┃╰╯╲┃┃┗╮╲╲\n╱╱╱╱╰╯╰┛╲╲",
    "┏╮\n┃▔┃▂▂┏┓┏┳┓\n┃▂┣┻╮┃┃▂┃▂┏╯\n┃▔┃▔╭╮▔┃┃┃▔┃▔┗┓\n┃▂┃▂╰╯▂┃┗╯▂┃▂▂▂┃\n┃▔┗╮┃▔▔▔┃▔┏╯\n┃▂▂▂▂▂┣╯▂▂▂┃▂┗╮\n┗┻┻┛",
    "┏┓┏┳┳┳┓\n┃┗┫╋┣┓┃┏┫┻┫\n┗┻┛┗┛┗┛\n­­­­­­­­­YOU",
    "╦╔╗╗╔╔ \n║║║║║╠ \n╚═╚╝╚╝╚ \n╦╦╔╗╦╦   \n╚╦╝║║║║ \n╩╚╝╚╝",
    "╔══╗....<3 \n╚╗╔╝..('\\../') \n╔╝╚╗..( . ) \n╚══╝..(,,)(,,) \n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "░I░L░O░V░E░Y░O░U░",
    "┈┈╭╱▔▔▔▔╲╮┈┈┈\n┈┈╰╱╭▅╮╭▅╮╲╯┈┈┈\n╳┈┈▏╰┈▅▅┈╯▕┈┈┈┈\n┈┈┈╲┈╰╯┈╱┈┈╳┈\n┈┈┈╱╱▔╲╱▔╲╲┈┈┈┈\n┈╭╮▔▏┊┊▕▔╭╮┈╳\n┈┃┊┣▔╲┊┊╱▔┫┊┃┈┈\n┈╰╲╱╯┈╳",
    "╔ღ═╗╔╗\n╚╗╔╝║║ღ═╦╦╦═ღ\n╔╝╚╗ღ╚╣║║║║╠╣\n╚═ღ╝╚═╩═╩ღ╩═╝",
    "╔══╗ \n╚╗╔╝ \n╔╝(¯'v'¯) \n╚══'.¸./\n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "╔╗ \n║║╔═╦═╦═╦═╗ ╔╦╗ \n║╚╣╬╠╗║╔╣╩╣ ║║║ \n╚═╩═╝╚═╝╚═╝ ╚═╝ \n╔═╗ \n║═╬═╦╦╦═╦═╦═╦═╦═╗ \n║╔╣╬║╔╣╩╬╗║╔╣╩╣╔╝ \n╚╝╚═╩╝╚═╝╚═╝╚═╩╝",
    "╔══╗ \n╚╗╔╝ \n╔╝╚╗ \n╚══╝ \n╔╗ \n║║╔═╦╦╦═╗ \n║╚╣║║║║╚╣ \n╚═╩═╩═╩═╝ \n╔╗╔╗ ♥️ \n║╚╝╠═╦╦╗ \n╚╗╔╣║║║║ \n═╚╝╚═╩═╝",
    "╔══╗╔╗  ♡ \n╚╗╔╝║║╔═╦╦╦╔╗ \n╔╝╚╗║╚╣║║║║╔╣ \n╚══╝╚═╩═╩═╩═╝\n­­­­­­­­­­­­YOU",
    "╭╮╭╮╮╭╮╮╭╮╮╭╮╮ \n┃┃╰╮╯╰╮╯╰╮╯╰╮╯ \n┃┃╭┳┳╮╭┳╮ \n┃┃┃┃╭╮┣╮┃┃╭┫╭╮┃ \n┃╰╯┃╰╯┃┃╰╯┃┃╰┻┻╮ \n╰┻╯╰╯╰╯",
    "┊┊╭╮┊┊┊┊┊┊┊┊┊┊┊ \n╋╯┊┊┊┊┊┊┊┊┊┊┊ \n┊┊┃┊╭┳╮╭┓┊╭╮╭╮ \n╭╋╋╯┣╯┃┊┃╰╋╯ \n╰╯┊╰╯┊╰┛┊╰",
]
SLEEP = 1

@PY.UBOT("loveyou")
@PY.TOP_CMD
async def lopeyo(client, message):
    noble = random.randint(1, len(NOBLE) - 2)
    reply_text = NOBLE[noble]
    await message.reply(reply_text)


@PY.UBOT("hmm")
@PY.TOP_CMD
async def hmmm(client, message):
    mg = await message.reply(
        "┈┈╱▔▔▔▔▔╲┈┈┈HM┈HM\n┈╱┈┈╱▔╲╲╲▏┈┈┈HMMM\n╱┈┈╱╱▔▔▔▔▔╲╮┈┈\n▏┈▕┃▕╱▔╲╱▔╲▕╮┃┈┈\n▏┈▕╰▏▊▕▕▋▕▕╯┈┈\n╲┈┈╲╱▔╭╮▔▔┳╲╲┈┈┈\n┈╲┈┈▏╭╯▕▕┈┈┈\n┈┈╲┈╲▂▂▂▂▂▂╱╱┈┈┈\n┈┈┈┈▏┊┈┈┈┈┊┈┈┈╲\n┈┈┈┈▏┊┈┈┈┈┊▕╲┈┈╲\n┈╱▔╲▏┊┈┈┈┈┊▕╱▔╲▕\n┈▏┈┈┈╰┈┈┈┈╯┈┈┈▕▕\n┈╲┈┈┈╲┈┈┈┈╱┈┈┈╱┈╲\n┈┈╲┈┈▕▔▔▔▔▏┈┈╱╲╲╲▏\n┈╱▔┈┈▕┈┈┈┈▏┈┈▔╲▔▔\n┈╲▂▂▂╱┈┈┈┈╲▂▂▂╱┈ ",
    )


@PY.UBOT("ktl")
@PY.TOP_CMD
async def kntl(client, message):
    emoji = get_text(message)
    kontol = MEMES.GAMBAR_KONTOL
    if emoji:
        kontol = kontol.replace("⡀", emoji)
    await message.reply(kontol)


@PY.UBOT("penis")
@PY.TOP_CMD
async def pns(client, message):
    emoji = get_text(message)
    titid = MEMES.GAMBAR_TITIT
    if emoji:
        titid = titid.replace("😋", emoji)
    await message.reply(titid)


@PY.UBOT("heli")
@PY.TOP_CMD
async def helikopter(client, message):
    await message.reply(
        "▬▬▬.◙.▬▬▬ \n"
        "═▂▄▄▓▄▄▂ \n"
        "◢◤ █▀▀████▄▄▄▄◢◤ \n"
        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
        "◥█████◤ \n"
        "══╩══╩══ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ Hallo Semuanya :) \n"
        "╬═╬☻/ \n"
        "╬═╬/▌ \n"
        "╬═╬/ \\ \n",
    )


@PY.UBOT("tembak")
@PY.TOP_CMD
async def dornembak(client, message):
    await message.reply(
        "_/﹋\\_\n" "(҂`_´)\n" "<,︻╦╤ ҉\n" r"_/﹋\_" "\nMau Jadi Pacarku Gak?!",
    )


@PY.UBOT("bundir")
@PY.TOP_CMD
async def ngebundir(client, message):
    await message.reply(
        "`Dadah Semuanya...`          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )


@PY.UBOT("awk")
@PY.TOP_CMD
async def awikwok(client, message):
    await message.reply(
        "██▀▀▀██\n"
        "▄▀█▄▄▄▄▀█▄▄▄\n"
        "▄▀█▄▄██▄▄\n"
        "▄▄▄▀▀▄▄▄▄▀▀▄\n"
        "▀▀▀▀▀▀\n`Awkwokwokwok..`",
    )


@PY.UBOT("ya")
@PY.TOP_CMD
async def ysaja(client, message):
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
        "█████‡‡‡‡‡‡‡██████████\n",
    )
@PY.UBOT("bot")
@PY.TOP_CMD
async def bot(client, message):
    await message.reply(
       "╔╗╔╦══╦═╦═╦══╦═╦══╗\n"
       "║║║║══╣╦╣╬║╔╗║║╠╗╔╝\n"
       "║╚╝╠══║╩╣╗╣╔╗║║║║║\n"
       "╚══╩══╩═╩╩╩══╩═╝╚╝\n", 
    ) 


@PY.UBOT("tank")
async def tank(client, message):
    await message.reply(
        "█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
        "▂▄▅█████████▅▄▃▂…\n"
        "[███████████████████]\n"
        "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n",
    )


@PY.UBOT("babi")
@PY.TOP_CMD
async def babi(client, message):
    await message.reply(
        "┈┈┏╮╭┓┈╭╮\n"
        "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
        "┈┈╰┓▋▋┏╯╯╰╯\n"
        "┈╭┻╮╲┗╮╭╮┈\n"
        "┈┃▎▎┃╲╲╲╲╲╲┣╯┈\n"
        "┈╰┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈┈╰┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n",
    )


@PY.UBOT("ange")
@PY.TOP_CMD
async def piciieess(client, message):
    e = await message.edit("Ayanggg 😖")
    await asyncio.sleep(2)
    await e.edit("Aku Ange 😫")
    await asyncio.sleep(2)
    await e.edit("Ayuukk Picies Yang 🤤")


@PY.UBOT("lipkol")
@PY.TOP_CMD
async def lipkoll(client, message):
    e = await message.edit("Ayanggg 😖")
    await asyncio.sleep(2)
    await e.edit("Kangeeen 👉👈")
    await asyncio.sleep(2)
    await e.edit("Pingiinn Slipkool Yaaang 🥺👉👈")


@PY.UBOT("nakal")
@PY.TOP_CMD
async def nakall(client, message):
    e = await message.edit("Ayanggg ih🥺")
    await asyncio.sleep(2)
    await e.edit("Nakal Banget Dah Ayang 🥺")
    await asyncio.sleep(2)
    await e.edit("Aku Gak Like Ayang 😠")
    await asyncio.sleep(2)
    await e.edit("Pokoknya Aku Gak Like Ih 😠")


@PY.UBOT("piss")
@PY.TOP_CMD
async def peace(client: Client, message: Message):
    await message.reply(
        "┈┈┈┈PEACE MAN┈┈┈┈\n"
        "┈┈┈┈┈┈╭╮╭╮┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┃┃┃┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┃┃┃┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┗┛┣┳╮┈┈┈┈\n"
        "┈┈┈┈┈╭┻┓┃┃┈┈┈┈\n"
        "┈┈┈┈┈┃╲┏╯┻┫┈┈┈┈\n"
        "┈┈┈┈┈╰╮╯┊┊╭╯┈┈┈┈\n",
    )


@PY.UBOT("spongebob")
@PY.TOP_CMD
async def spongebobss(client: Client, message: Message):
    await message.reply(
        "╲┏┳┓╲╲\n"
        "╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲\n"
        "╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲\n"
        "╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲\n"
        "╲┃◯┃╭╮╰╯┏┳╯╲\n"
        "╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲\n"
        "╲┃╰┃◯╰┗┛┗┛╯╭┃╲╲\n",
    )



@PY.UBOT("kocok")
@PY.TOP_CMD
async def kocokk(client, message):
    e = await message.edit("KOCOKINNNN DONG SAYANKKKKK🤤🤤🥵🥵")
    await asyncio.sleep(0.2)
    await e.edit("8✊====D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8====✊D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8✊====D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8====✊D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8✊====D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8====✊D💦")
    await asyncio.sleep(0.2)
    await e.edit("8===✊=D💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8==✊==D💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8=✊===D💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8✊====D💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8=✊====D💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8==✊==D💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8===✊=D💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8====✊D💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("**CROOTTTT**")
    await asyncio.sleep(0.2)
    await e.edit("**CROOTTTT AAAHHH BASAHH.....**")
    await asyncio.sleep(0.2)
    await e.edit("**AHHH ENAKKKKK SAYANGGGG🤤🤤🥵🥵**")


@PY.UBOT("dinoo")
@PY.TOP_CMD
async def adadino(client: Client, message: Message):
    typew = await message.edit("`DIN DINNN.....`")
    await asyncio.sleep(1)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    await asyncio.sleep(1)
    await typew.edit("`🏃                        🦖`")
    await typew.edit("`🏃                       🦖`")
    await typew.edit("`🏃                      🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃   `LARII`          🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃WOARGH!   🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                    🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃  Huh-Huh           🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃          🦖`")
    await typew.edit("`🏃         🦖`")
    await typew.edit("`DIA SEMAKIN MENDEKAT!!!`")
    await asyncio.sleep(1)
    await typew.edit("`🏃       🦖`")
    await typew.edit("`🏃      🦖`")
    await typew.edit("`🏃     🦖`")
    await typew.edit("`🏃    🦖`")
    await typew.edit("`Dahlah Pasrah Aja`")
    await asyncio.sleep(1)
    await typew.edit("`🧎🦖`")
    await asyncio.sleep(2)
    await typew.edit("`-TAMAT-`")


@PY.UBOT("ajg")
@PY.TOP_CMD
async def anjg(client, message):
    await message.reply(
        "╥╭╮┳\n"
        "╢╭╮╭┫┃▋▋▅┣\n"
        "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
        "╢╰┫┈┈┈┈┈╰╯╰┳╯┣\n"
        "╢┊┊┃┏┳┳┓┏┳┫┊┊┣\n"
        "╨┗┛┗┛┗┛┗┛┻\n",
    )


@PY.UBOT("nah")
@PY.TOP_CMD
async def nahlove(client, message):
    typew = await message.reply("`\n(\\_/)`" "`\n(●_●)`" "`\n />💖 *Ini Buat Kamu`")
    await asyncio.sleep(2)
    await typew.edit("`\n(\\_/)`" "`\n(●_●)`" "`\n💖<\\  *Tapi Bo'ong`")

@PY.UBOT("loveyou")
@PY.TOP_CMD
async def hearts(client: Client, message: Message):
    await asyncio.sleep(SLEEP * 3)
    await message.edit("❤️ I")
    await asyncio.sleep(0.5)
    await message.edit("❤️ I Love")
    await asyncio.sleep(0.5)
    await message.edit("❤️ I Love You")
    await asyncio.sleep(3)
    await message.edit("❤️ I Love You <3")

@PY.UBOT("bomb")
@PY.TOP_CMD
async def gahite(client: Client, message: Message):
    if message.forward_from:
        return
    for i in range(5):
        await message.edit("▪️▪️▪️▪️ \n" * (i) + "💣💣💣💣 \n" + "▪️▪️▪️▪️ \n" * (4-i))
        await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n" * 4 + "💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n" * 3 + "💥💥💥💥 \n" * 2)
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n" * 4 + "😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await message.edit("`RIP PLOXXX......`")
    await asyncio.sleep(2)

@PY.UBOT("charge")
@PY.TOP_CMD
async def timer_blankx(client: Client, msg: Message):
    txt = (
        msg.text[8:]
        + "\n\n`Tesla Wireless Charging (beta) Started...\nDevice Detected: Nokia 1100\nBattery Percentage:` "
    )
    for j in range(10, 101, 10):
        await msg.edit_text(txt + str(j))
        await asyncio.sleep(1)
    await asyncio.sleep(1)
    await msg.edit_text(
        "`Tesla Wireless Charging (beta) Completed...\nDevice Detected: Nokia 1100 (Space Grey Varient)\nBattery Percentage:` [100%](https://telegra.ph/file/a45aa7450c8eefed599d9.mp4)",
        disable_web_page_preview=False,
    )

@PY.UBOT("hack")
@PY.TOP_CMD
async def hak(client: Client, message: Message):
    hacking_steps = [
        ("Looking for Telegram databases in targeted person...", 2),
        (" User online: True\nTelegram access: True\nRead Storage: True ", 2),
        ("Hacking... 0%\n[░░░░░░░░░░░░░░░░░░░░]\n`Looking for Telegram...`\nETA: 0m, 20s", 2),
        ("Hacking... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\n`Looking for Telegram...`\nETA: 0m, 18s", 2),
        ("Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]\n`Found folder C:/Telegram`\nETA: 0m, 16s", 2),
        ("Hacking... 34.42%\n[█████░░░░░░░░░░░░░░░]\n`Found folder C:/Telegram`\nETA: 0m, 14s", 2),
        ("Hacking... 42.17%\n[███████░░░░░░░░░░░░░]\n`Searching for databases`\nETA: 0m, 12s", 2),
        ("Hacking... 55.30%\n[█████████░░░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s", 2),
        ("Hacking... 64.86%\n[███████████░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s", 2),
        ("Hacking... 74.02%\n[█████████████░░░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 06s", 2),
        ("Hacking... 86.21%\n[███████████████░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 04s", 2),
        ("Hacking... 93.50%\n[█████████████████░░░]\n`Decryption successful!`\nETA: 0m, 02s", 2),
        ("Hacking... 100%\n[████████████████████]\n`Scanning file...`\nETA: 0m, 00s", 2),
        ("Hacking complete!\nUploading file...", 2),
        ("Targeted Account Hacked...!\n\n ✅ File has been successfully uploaded to my server.\nTelegram Database:\n`./DOWNLOADS/msgstore.db.crypt12`", 2),
    ]
    for step, delay in hacking_steps:
        await message.edit(step)
        await asyncio.sleep(delay)


# Define the edit_or_reply function
async def edit_or_reply(message: Message, text: str):
    if message.from_user.is_self:
        return await message.edit_text(text)
    else:
        return await message.reply_text(text)

@PY.UBOT("dino")
@PY.TOP_CMD
async def adadino(client: Client, message: Message):
    typew = await edit_or_reply(message, "`DIN DINNN.....`")
    await asyncio.sleep(1)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    await asyncio.sleep(1)

    dino_chase_frames = [
        "`🏃                        🦖`",
        "`🏃                       🦖`",
        "`🏃                      🦖`",
        "`🏃                     🦖`",
        "`🏃   `Lari uus`          🦖`",
        "`🏃                   🦖`",
        "`🏃                  🦖`",
        "`🏃                 🦖`",
        "`🏃                🦖`",
        "`🏃               🦖`",
        "`🏃              🦖`",
        "`🏃             🦖`",
        "`🏃            🦖`",
        "`🏃           🦖`",
        "`🏃WOARGH!   🦖`",
        "`🏃           🦖`",
        "`🏃            🦖`",
        "`🏃             🦖`",
        "`🏃              🦖`",
        "`🏃               🦖`",
        "`🏃                🦖`",
        "`🏃                 🦖`",
        "`🏃                  🦖`",
        "`🏃                   🦖`",
        "`🏃                    🦖`",
        "`🏃                     🦖`",
        "`🏃  Huh-Huh           🦖`",
        "`🏃                   🦖`",
        "`🏃                  🦖`",
        "`🏃                 🦖`",
        "`🏃                🦖`",
        "`🏃               🦖`",
        "`🏃              🦖`",
        "`🏃             🦖`",
        "`🏃            🦖`",
        "`🏃           🦖`",
        "`🏃          🦖`",
        "`🏃         🦖`",
        "`HE WAS GETTING CLOSER!!!`",
        "`🏃       🦖`",
        "`🏃      🦖`",
        "`🏃     🦖`",
        "`🏃    🦖`",
        "`Just give up`",
        "`🧎🦖`",
        "`-DIED-`"
    ]

    for frame in dino_chase_frames:
        await typew.edit(frame)
        await asyncio.sleep(0.5)

@PY.UBOT("gabut")
@PY.TOP_CMD
async def menggabut(client: Client, message: Message):
    e = await edit_or_reply(message, "`GABUT`")
    await asyncio.sleep(1)
    
    gabut_frames = [
        "`G A B U T`",
        "`G  A  B  U  T`",
        "`G   A   B   U   T`",
        "`G    A    B    U    T`",
        "`G   A   B   U   T`",
        "`G  A  B  U  T`",
        "`G A B U T`",
        "`GABUT`",
        "🙈🙈🙈🙈",
        "🙉🙉🙉🙉",
        "🙈🙈🙈🙈",
        "🙉🙉🙉🙉",
        "`GABUT NJINK`",
        "🙉🙉🙉🙉",
        "🐢                       🚶",
        "🐢                      🚶",
        "🐢                     🚶",
        "🐢                    🚶",
        "🐢                   🚶",
        "🐢                  🚶",
        "🐢                 🚶",
        "🐢                🚶",
        "🐢               🚶",
        "🐢              🚶",
        "🐢             🚶",
        "🐢            🚶",
        "🐢           🚶",
        "🐢          🚶",
        "🐢         🚶",
        "🐢        🚶",
        "🐢       🚶",
        "🐢      🚶",
        "🐢     🚶",
        "🐢    🚶",
        "🐢   🚶",
        "🐢  🚶",
        "🐢 🚶",
        "🐢🚶",
        "🚶🐢",
        "🚶 🐢",
        "🚶  🐢",
        "🚶   🐢",
        "🚶    🐢",
        "🚶     🐢",
        "🚶      🐢",
        "🚶       🐢",
        "🚶        🐢",
        "🚶         🐢",
        "🚶          🐢",
        "🚶           🐢",
        "🚶            🐢",
        "🚶             🐢",
        "🚶              🐢",
        "🚶               🐢",
        "🚶                🐢",
        "🚶                 🐢",
        "🚶                  🐢",
        "🚶                   🐢",
        "🚶                    🐢",
        "🚶                     🐢",
        "🚶                      🐢",
        "🚶                       🐢",
        "🚶                        🐢",
        "🚶                         🐢",
        "🚶                          🐢",
        "🚶                           🐢",
        "🚶                            🐢",
        "🚶                             🐢",
        "🚶                              🐢",
        "🚶                               🐢",
        "🚶                                🐢",
        "`GABUT NJIR`",
        "🙉",
        "🙈",
        "🙉",
        "🙈",
        "🙉",
        "😂",
        "🐢                       🚶",
        "🐢                      🚶",
        "🐢                     🚶",
        "🐢                    🚶",
        "🐢                   🚶",
        "🐢                  🚶",
        "🐢                 🚶",
        "🐢                🚶",
        "🐢               🚶",
        "🐢              🚶",
        "🐢             🚶",
        "🐢            🚶",
        "🐢           🚶",
        "🐢          🚶",
        "🐢         🚶",
        "🐢        🚶",
        "🐢       🚶",
        "🐢      🚶",
        "🐢     🚶",
        "🐢    🚶",
        "🐢   🚶",
        "🐢  🚶",
        "🐢 🚶",
        "🐢🚶",
        "🚶🐢",
        "🚶 🐢",
        "🚶  🐢",
        "🚶   🐢",
        "🚶    🐢",
        "🚶     🐢",
        "🚶      🐢",
        "🚶       🐢",
        "🚶        🐢",
        "🚶         🐢",
        "🚶          🐢",
        "🚶           🐢",
        "🚶            🐢",
        "🚶             🐢",
        "🚶              🐢",
        "🚶               🐢",
        "🚶                🐢",
        "🚶                 🐢",
        "🚶                  🐢",
        "🚶                   🐢",
        "🚶                    🐢",
        "🚶                     🐢",
        "🚶                      🐢",
        "🚶                       🐢",
        "🚶                        🐢",
        "🚶                         🐢",
        "🚶                          🐢",
        "🚶                           🐢",
        "🚶                            🐢",
        "🚶                             🐢",
        "🚶                              🐢",
        "🚶                               🐢",
        "🚶                                🐢",
        "`GABUT`"
    ]

    for frame in gabut_frames:
        await e.edit(frame)
        await asyncio.sleep(0.3)

@PY.UBOT("fadmin")
@PY.TOP_CMD
async def _(client, message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 20)
    await message.edit("Admin Proses....")
    animation_chars = [
            "**Promoting User As Admin...**",
            "**Enabling All Permissions To User...**",
            "**(1) Send Messages: ☑️**",
            "**(1) Send Messages: ✅**",
            "**(2) Send Media: ☑️**",
            "**(2) Send Media: ✅**",
            "**(3) Send Stickers & GIFs: ☑️**",
            "**(3) Send Stickers & GIFs: ✅**",
            "**(4) Send Polls: ☑️**",
            "**(4) Send Polls: ✅**",
            "**(5) Embed Links: ☑️**",
            "**(5) Embed Links: ✅**",
            "**(6) Add Users: ☑️**",
            "**(6) Add Users: ✅**",
            "**(7) Pin Messages: ☑️**",
            "**(7) Pin Messages: ✅**",
            "**(8) Change Chat Info: ☑️**",
            "**(8) Change Chat Info: ✅**",
            "**Permission Granted Successfully**",
            "**pRoMooTeD SuCcEsSfUlLy**"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 20])

@PY.UBOT("fleave")
@PY.TOP_CMD
async def _(client, message):
    if message.forward_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 17)
    await message.edit("Leave Proses....")
    animation_chars = [
            "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",
            "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",
            "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",
            "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
            "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
            "**Chat Message Exported To** `./Inpu/`",
            "**Chat Message Exported To** `./Inpu/homework/`",
            "**Chat Message Exported To** `./Inpu/homework/groupchat.txt`",
            "__Legend is leaving this chat.....! Bye geys..__",
            "__Legend is leaving this chat.....! Bye geys..__"

    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 17])


@PY.UBOT("tupload")
@PY.TOP_CMD
async def _(client, message):
    if message.forward_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 11)
    await message.edit("Start Uploas....")
    animation_chars = [
            "Uploading File From Telegram To Whatsapp...",
            " User Online: True\nTelegram API Access: True\nWhatsapp API Access: True\nRead Storage: True ",
            "DOWNLOADING STARTED... \n\n0% [░░░░░░░░░░░░░░░░░░░░]\n`Connecting To WhatsApp API...`\nETA: 0m, 20s",
            "DOWNLOADING... \n\n11.07% [██░░░░░░░░░░░░░░░░░░]\n\nETA: 0m, 18s",
            "DOWNLOADING... \n\n20.63% [███░░░░░░░░░░░░░░░░░]\n\nETA: 0m, 16s",
            "FILE DOWNLOADED, UPLOADING TO ADMIN'S WHATSAPP GROUP [CHUTIYA GENG BOYS]... \n\n34.42% [█████░░░░░░░░░░░░░░░]\n\nETA: 0m, 14s",
            "UPLOADING... \n\n42.17% [███████░░░░░░░░░░░░░]\n\nETA: 0m, 12s",
            "UPLOADING... \n\n55.30% [█████████░░░░░░░░░░░]\n\nETA: 0m, 10s",
            "UPLOADING... \n\n64.86% [███████████░░░░░░░░░]\n\nETA: 0m, 08s",
            "UPLOADED TO ADMIN'S WHATSAPP GROUP SERVER ... \n\n74.02% [█████████████░░░░░░░]\n\nETA: 0m, 06s",
            "SPLITTING FILE IN WHATSAPP SUPPORTED SIZE & UPLOADING IT ... 86.21% [███████████████░░░░░]\n\nETA: 0m, 04s",
            "SPLITTING FILE IN WHATSAPP SUPPORTED SIZE & UPLOADING IT... 93.50% [█████████████████░░░]\n\nETA: 0m, 02s",
            "UPLOADING TO ADMIN'S WHATSAPP GROUP [CHUTIYA GANG BOYS]... 100% [████████████████████]\n`Scanning file...`\nETA: 0m, 00s",
            "UPLOADING FILE TO WHATSAPP GROUP COMPLETED!\nFILE VERIFIED: ✅",
            "API TERMINATED UNTIL FURTHER USAGE..."
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 11])

@PY.UBOT("hadiah")
@PY.TOP_CMD
async def gahah(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 17)
    await message.edit("Ada Hadiah.....")
    animation_chars = [
"⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://t.me/moirestore1)⬜",
            "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://t.me/moirestore1)⬜",
            "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://t.me/moirestore1)⬜",
            "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://t.me/moirestore1)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://t.me/moirestore1)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://t.me/moirestore1)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://t.me/moirestore1)⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://t.me/moirestore1)⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://t.me/moirestore1)⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜[🎁](https://t.me/moirestore1)⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜[🎁](https://t.me/moirestore1)⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n[🎁](https://t.me/moirestore1)⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜",
            "⬜⬜⬜\n⬜⬜⬜\n⬜⬜⬜",
            "⬜⬜\n⬜⬜",
            "[🎁](https://t.me/moirestore1)"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 17])

async def edit_or_reply(message: Message, text: str):
    if message.from_user.is_self:
        return await message.edit_text(text)
    else:
        return await message.reply_text(text)

@PY.UBOT("polisi")
@PY.TOP_CMD
async def adadino(client: Client, message: Message):
    typew = await edit_or_reply(message, "`mek....`")
    await asyncio.sleep(1)
    await typew.edit("`apa tu.......!!`")
    await asyncio.sleep(0.5)

    dino_chase_frames = [
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",            
            "OUB **Polisi sedang mengejarmu sekarang**"
    ]

    for frame in dino_chase_frames:
        await typew.edit(frame)
        await asyncio.sleep(0.5)