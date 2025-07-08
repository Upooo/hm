import asyncio
from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from pyrogram.errors.exceptions import FloodWait

from IdolUbot import *

__MODULE__ = "bcdb"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʀᴏᴀᴅᴅʙ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}bcdb</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢɪʀɪᴍ ᴘᴇꜱᴀɴ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴋᴇ ɢʀᴜᴘ/ᴘᴇꜱᴀɴ ᴅᴀᴛᴀʙᴀꜱᴇ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}adddb</code>
🦠 ᴋᴇᴛ : ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴅᴀᴛᴀʙᴀꜱᴇ ʙʀᴏᴀᴅᴄᴀꜱᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}undb</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢʜᴀᴘᴜꜱ ᴅᴀᴛᴀʙᴀꜱᴇ ʙʀᴏᴀᴅᴄᴀꜱᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}listdb</code>
🦠 ᴋᴇᴛ : ᴍᴇʟɪʜᴀᴛ ᴛᴏᴛᴀʟ ᴅᴀᴛᴀʙᴀꜱᴇ ʙʀᴏᴀᴅᴄᴀꜱᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}ralldb</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢʜᴀᴘᴜꜱ ꜱᴇᴍᴜᴀ ᴅᴀᴛᴀʙᴀꜱᴇ ʙʀᴏᴀᴅᴄᴀꜱᴛ.</b></blockquote>    
"""

@PY.UBOT("bcdb")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    bcs = await EMO.BROADCAST(client)
    _msg = f"{prs}proccesing..."
    gcs = await message.reply(_msg)
    if not message.reply_to_message:
        return await gcs.edit(f"⌭{ggl} mohon balas ke pesan !⌭")
    text = message.reply_to_message
    database = await get_list_from_vars(client.me.id, "DB_ID")
    done = 0
    failed = 0
    for chat_id in database:
        try:
            await text.copy(chat_id)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await text.copy(chat_id)
            done += 1
        except Exception:
            failed += 1
            pass
    if client.me.is_premium:
        await gcs.delete()
        _gcs = f"""
⌭ {brhsl} berrhasil kirim ke {done} chat database
⌭ {ggl} gagal kirim ke {failed} chat database

"""
    else:
        await gcs.delete()
        _gcs = f"""
⌭ gcast telah selesai
⌭ berrhasil {done} chat database
⌭ gagal {failed} chat database
"""
    return await message.reply(_gcs)

@PY.UBOT("adddb")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BERHASIL(client)
    _msg = f"{prs}proceꜱꜱing..."

    msg = await message.reply(_msg)
    try:
        chat_id = message.chat.id
        database = await get_list_from_vars(client.me.id, "DB_ID")

        if chat_id in database:
            txt = f"""
⌭ {grp}ꜱudah ada dalam database broadcaꜱt
"""
        else:
            await add_to_vars(client.me.id, "DB_ID", chat_id)
            txt = f"""
⌭ {grp}berhaꜱil di tambahkan ke database broadcaꜱt
"""

        return await msg.edit(txt)
    except Exception as error:
        return await msg.edit(str(error))


@PY.UBOT("undb")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BERHASIL(client)
    _msg = f"{prs}proceꜱꜱing..."

    msg = await message.reply(_msg)
    try:
        chat_id = get_arg(message) or message.chat.id
        database = await get_list_from_vars(client.me.id, "DB_ID")

        if chat_id not in database:
            response = f"""
⌭ {grp}tidak ada dalam database broadcaꜱt
"""
        else:
            await remove_from_vars(client.me.id, "DB_ID", chat_id)
            response = f"""
⌭ {grp}berhaꜱil di hapuꜱ dalam database broadcaꜱt
"""

        return await msg.edit(response)
    except Exception as error:
        return await msg.edit(str(error))


@PY.UBOT("listdb")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    _msg = f"{prs}proceꜱꜱing..."
    mzg = await message.reply(_msg)

    database = await get_list_from_vars(client.me.id, "DB_ID")
    total_database = len(database)

    list = f"{brhsl} daftar database\n"

    for chat_id in database:
        try:
            chat = await client.get_chat(chat_id)
            list += f" ├ {chat.title} | {chat.id}\n"
        except:
            list += f" ├ {chat_id}\n"

    list += f"{ktrng} total database {total_database}"
    return await mzg.edit(list)


@PY.UBOT("ralldb")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    _msg = f"{prs}proceꜱꜱing..."

    msg = await message.reply(_msg)
    databases = await get_list_from_vars(client.me.id, "DB_ID")

    if not databases:
        return await msg.edit(f"{ggl}database broadcaꜱt anda koꜱong")

    for chat_id in databases:
        await remove_from_vars(client.me.id, "DB_ID", chat_id)

    await msg.edit(f"{brhsl}ꜱemua database broadcaꜱt berhaꜱil di hapuꜱ")
