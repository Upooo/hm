from IdolUbot.core.helpers.tools import get_data_id
from IdolUbot import *
__MODULE__ = "ᴀʀᴄʜɪᴠᴇ"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀʀᴄʜɪᴠᴇ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}arch</code>
🦠 ᴋᴇᴛ : ᴀʀꜱɪᴘᴋᴀɴ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴘʀɪʙᴀᴅɪ ᴍᴀᴜᴘᴜɴ ᴄʜᴀɴɴᴇʟ</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}unarch</code>
🦠 ᴋᴇᴛ : ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴀʀꜱɪᴘ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴘʀɪʙᴀᴅɪ ᴍᴀᴜᴘᴜɴ ᴄʜᴀɴɴᴇʟ</b></blockquote>
"""

@PY.UBOT("arch")
@PY.TOP_CMD
async def archive_user(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) <2:
        return await message.reply(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ᴀʀᴄʜ ᴀʟʟ, ᴜꜱᴇʀꜱ, ɢʀᴏᴜᴘ</b></blockquote>")
    anjai = await message.reply(f"<blockquote><b>{prs} ᴘʀᴏᴄᴄᴇꜱɪɴɢ...</b></blockquote>")
    anjir = message.command[1]
    xx = await get_data_id(client, anjir)
    for anu in xx:
        await client.archive_chats(anu)
    
    await anjai.edit(f"<blockquote><b>{brhsl} ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɢᴜɴᴀʀᴄʜɪᴠᴇᴋᴀɴ ꜱᴇᴍᴜᴀ {anjir}</b></blockquote>")

@PY.UBOT("unarch")
@PY.TOP_CMD
async def unarchive_user(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) <2:
        return await message.reply(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ᴀʀᴄʜ ᴀʟʟ, ᴜꜱᴇʀꜱ, ɢʀᴏᴜᴘ</b></blockquote>")
    anjai = await message.reply(f"<blockquote><b>{prs} ᴘʀᴏᴄᴄᴇꜱɪɴɢ...</b></blockquote>")
    anjir = message.command[1]
    xx = await get_data_id(client, anjir)
    for anu in xx:
        await client.unarchive_chats(anu)
    await anjai.edit(f"<blockquote><b>{brhsl} ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɢᴜɴᴀʀᴄʜɪᴠᴇᴋᴀɴ ꜱᴇᴍᴜᴀ {anjir}</b></blockquote>")
