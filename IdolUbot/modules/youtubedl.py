from IdolUbot import *
import asyncio
import math
import os
from datetime import timedelta
from time import time

import wget
from pyrogram.errors import FloodWait, MessageNotModified
from youtubesearchpython import VideosSearch

__MODULE__ = "yt"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʏᴏᴜᴛᴜʙᴇ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}song</code>
🦠 ᴋᴇᴛ : ʙᴜᴀᴛ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜꜱɪᴄ ʏᴀɴɢ ᴅɪ ᴍᴀᴜ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}vsong</code>
🦠 ᴋᴇᴛ : ʙᴜᴀᴛ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴅɪ ᴍᴀᴜ.</b></blockquote>
"""

def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "kb", 2: "mb", 3: "gb", 4: "tb"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return f"{str(round(size, 2))} {dict_power_n[raised_to_pow]}"


def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        (f"{str(days)} ʜᴀʀɪ, " if days else "")
        + (f"{str(hours)} ᴊᴀᴍ, " if hours else "")
        + (f"{str(minutes)} ᴍᴇɴɪᴛ, " if minutes else "")
        + (f"{str(seconds)} ᴅᴇᴛɪᴋ, " if seconds else "")
        + (f"{str(milliseconds)} ᴍɪᴋʀᴏᴅᴇᴛɪᴋ, " if milliseconds else "")
    )
    return tmp[:-2]


async def progress(current, total, message, start, type_of_ps, file_name=None):
    now = time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join("" for _ in range(math.floor(percentage / 10))),
            "".join("~" for _ in range(10 - math.floor(percentage / 10))),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} ᴏꜰ {1}\nᴇꜱᴛɪᴍᴀꜱɪ : {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await message.edit(
                    f"""
{type_of_ps}

file_id: {file_name}

{tmp}
"""
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass
        else:
            try:
                await message.edit(f"{type_of_ps}\n{tmp}")
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass


async def vsong_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            f"<blockquote><b><emoji id =5929358014627713883>❌</emoji> ᴠɪᴅᴇᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ,\nᴍᴏʜᴏɴ ᴍᴀꜱᴜᴋᴀɴ ᴊᴜᴅᴜʟ ᴠɪᴅᴇᴏ ᴅᴇɴɢᴀɴ ʙᴇɴᴀʀ.</b></blockquote>",
        )
    infomsg = await message.reply_text(f"<blockquote><b><emoji id =5803403369913520877>🔍</emoji> ᴘᴇɴᴄᴀʀɪᴀɴ...</b></blockquote>", quote=False)
    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()[
            "result"
        ][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await infomsg.edit(f"<blockquote><b><emoji id =5803403369913520877>🔍</emoji> ᴘᴇɴᴄᴀʀɪᴀɴ...</b></blockquote>\n\n{error}")
    try:
        (
            file_name,
            title,
            url,
            duration,
            views,
            channel,
            thumb,
            data_ytp,
        ) = await YoutubeDownload(link, as_video=True)
    except Exception as error:
        return await infomsg.edit(f"<blockquote><b><emoji id =5375452661036358740>🔥</emoji> ᴅᴏᴡɴʟᴏᴀᴅᴇʀ...\n\n{error}</b><blockquote>")
    thumbnail = wget.download(thumb)
    await client.send_video(
        message.chat.id,
        video=file_name,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        supports_streaming=True,
        caption=data_ytp.format(
            "video",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            bot.me.mention,
        ),
        progress=progress,
        progress_args=(
            infomsg,
            time(),
            "📥 ᴅᴏᴡɴʟᴏᴀᴅᴇʀ...",
            f"{search['id']}.mp4",
        ),
        reply_to_message_id=message.id,
    )
    await infomsg.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)

@PY.UBOT("vsong")
@PY.TOP_CMD
async def _(client, message):
    await vsong_cmd(client, message)


@PY.UBOT("song")
@PY.TOP_CMD
async def song_cmd(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    if len(message.command) < 2:
        return await message.reply_text(
            f"<blockquote>{ggl}ᴀᴜᴅɪᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ! ᴍᴏʜᴏɴ ᴍᴀꜱᴜᴋᴀɴ ᴊᴜᴅᴜʟ ᴀᴜᴅɪᴏ ᴅᴇɴɢᴀɴ ʙᴇɴᴀʀ</blockquote>",
        )
    infomsg = await message.reply_text(f"<blockquote>{prs}ᴘᴇɴᴄᴀʀɪᴀɴ...</blockquote>", quote=False)
    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()[
            "result"
        ][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await infomsg.edit(f"{prs}ᴘᴇɴᴄᴀʀɪᴀɴ...\n\n{error}")
    try:
        (
            file_name,
            title,
            url,
            duration,
            views,
            channel,
            thumb,
            data_ytp,
        ) = await YoutubeDownload(link, as_video=False)
    except Exception as error:
        return await infomsg.edit(f"{ggl}downloader..\n\n{error}")
    thumbnail = wget.download(thumb)
    await client.send_audio(
        message.chat.id,
        audio=file_name,
        thumb=thumbnail,
        file_name=title,
        performer=channel,
        duration=duration,
        caption=data_ytp.format(
            "audio",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            bot.me.mention,
        ),
        progress=progress,
        progress_args=(
            infomsg,
            time(),
            f"<blockquote>{prs}ᴘʀᴏᴄᴇꜱɪɴɢ...<blockquote>",
            f"{search['id']}.mp3",
        ),
        reply_to_message_id=message.id,
    )
    await infomsg.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)
