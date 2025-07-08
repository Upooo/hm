__MODULE__ = "bl"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʟᴀᴄᴋʟɪsᴛ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}addbl</code>
🦠 ᴋᴇᴛ : ᴍᴀꜱᴜᴋᴀɴ ɢʀᴏᴜᴘ ᴋᴇ ᴅᴀꜰᴛᴀʀ ʙʟᴀᴄᴋʟɪꜱᴛ ʙʀᴏᴀᴅᴄᴀꜱᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}unbl</code>
🦠 ᴋᴇᴛ : ʜᴀᴘᴜꜱ ɢʀᴏᴜᴘ ᴋᴇ ᴅᴀꜰᴛᴀʀ ʙʟᴀᴄᴋʟɪꜱᴛ ʙʀᴏᴀᴅᴄᴀꜱᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}listbl</code>
🦠 ᴋᴇᴛ : ʟɪʜᴀᴛ ᴅᴀꜰᴛᴀʀ ɢʀᴏᴜᴘ ʙʟᴀᴄᴋʟɪꜱᴛ ʙʀᴏᴀᴅᴄᴀꜱᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}rallbl</code>
🦠 ᴋᴇᴛ : ʜᴀᴘᴜꜱ ꜱᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴋᴇ ᴅᴀꜰᴛᴀʀ ʙʟᴀᴄᴋʟɪꜱᴛ ʙʀᴏᴀᴅᴄᴀꜱᴛ.</b></blockquote>
"""

from IdolUbot import *

@PY.UBOT("addbl")
@PY.IDOL("caddbl")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrn = await EMO.BL_KETERANGAN(client)
    _msg = f"<blockquote><b>{prs} ᴛᴜɴɢɢᴜ ʙᴇɴᴛᴀʀ...</b></blockquote>"

    msg = await message.reply(_msg)
    try:
        chat_id = message.chat.id
        blacklist = await get_list_from_vars(client.me.id, "BL_ID")

        if chat_id in blacklist:
            txt = f"""
<blockquote><b>⌭ {grp} ɢʀᴏᴜᴘ: {message.chat.title}</blockquote></b>
<blockquote><b>⌭ {ktrn} ᴋᴇᴛ: sᴜᴅᴀʜ ᴀᴅᴀ ᴅᴀʟᴀᴍ ʟɪsᴛ</blockquote></b>
"""
        else:
            await add_to_vars(client.me.id, "BL_ID", chat_id)
            txt = f"""
<blockquote><b>⌭ {grp} ɢʀᴏᴜᴘ: {message.chat.title}</blockquote></b>\n<blockquote><b>⌭ {ktrn} ᴋᴇᴛ: ʙᴇʀʜᴀsɪʟ ᴅɪ ᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀʟᴀᴍ ʟɪsᴛ ᴊᴇᴍʙᴏᴛ</blockquote></b>
"""

        return await msg.edit(txt)
    except Exception as error:
        return await msg.edit(str(error))


@PY.UBOT("unbl")
@PY.IDOL("cunbl")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrn = await EMO.BL_KETERANGAN(client)
    _msg = f"{prs}proceꜱꜱing..."

    msg = await message.reply(_msg)
    try:
        chat_id = get_arg(message) or message.chat.id
        blacklist = await get_list_from_vars(client.me.id, "BL_ID")

        if chat_id not in blacklist:
            response = f"""
<blockquote><b>⌭ {grp} ɢʀᴏᴜᴘ: {message.chat.title}</blockquote></b>
<blockquote><b>⌭ {ktrn} ᴋᴇᴛ: ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ʟɪsᴛ </b></blockquote>
"""
        else:
            await remove_from_vars(client.me.id, "BL_ID", chat_id)
            response = f"""
<blockquote><b>⌭ {grp} ɢʀᴏᴜᴘ: {message.chat.title}</blockquote ></b>
<blockquote><b>⌭ {ktrn} ᴋᴇᴛ: ʙᴇʀʜᴀsɪʟ ᴅɪ ʜᴀᴘᴜs ᴋᴇ ᴅᴀʟᴀᴍ ʟɪsᴛ </blockquote></b>
"""

        return await msg.edit(response)
    except Exception as error:
        return await msg.edit(str(error))


@PY.UBOT("listbl")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    _msg = f"{prs}proceꜱꜱing..."
    mzg = await message.reply(_msg)

    blacklist = await get_list_from_vars(client.me.id, "BL_ID")
    total_blacklist = len(blacklist)

    list = f"{brhsl} ᴅᴀꜰᴛᴀʀ ʙʟᴀᴄᴋʟɪꜱᴛ\n"

    for chat_id in blacklist:
        try:
            chat = await client.get_chat(chat_id)
            list += f" ├ {chat.title} | {chat.id}\n"
        except:
            list += f" ├ {chat_id}\n"

    list += f"{ktrng} ᴛᴏᴛᴀʟ ʙʟᴀᴄᴋʟɪꜱᴛ : {total_blacklist}"
    return await mzg.edit(list)


@PY.UBOT("rallbl")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    _msg = f"{prs} ᴘʀᴏᴄᴇꜱꜱɪɴɢ..."

    msg = await message.reply(_msg)
    blacklists = await get_list_from_vars(client.me.id, "BL_ID")

    if not blacklists:
        return await msg.edit(f"{ggl} ʙʟᴀᴄᴋʟɪꜱᴛ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀɴᴅᴀ ᴋᴏꜱᴏɴɢ.")

    for chat_id in blacklists:
        await remove_from_vars(client.me.id, "BL_ID", chat_id)

    await msg.edit(f"{brhsl} ꜱᴇᴍᴜᴀ ʙʟᴀᴄᴋʟɪꜱᴛ ʙʀᴏᴀᴅᴄᴀꜱᴛ ʙᴇʀʜᴀꜱɪʟ ᴅɪ ʜᴀᴘᴜꜱ.")
