import asyncio

from IdolUbot import *

__MODULE__ = "purge"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘᴜʀɢᴇ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}purge</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢʜᴀᴘᴜs sᴇᴍᴜᴀ ᴘᴇsᴀɴ ᴅᴀʀɪ ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪʙᴀʟᴀs sᴀᴍᴘᴀɪ sᴇᴋᴀʀᴀɴɢ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}del</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢʜᴀᴘᴜs ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪʙᴀʟᴀs.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}purgeme</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢʜᴀᴘᴜs ᴘᴇsᴀɴ ᴀɴᴅᴀ sᴇɴᴅɪʀɪ.</blockquote>
"""



@PY.UBOT("del")
@PY.TOP_CMD
async def _(client, message):
    rep = message.reply_to_message
    await message.delete()
    await rep.delete()


@PY.UBOT("purgeme")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) != 2:
        return await message.delete()
    n = (
        message.reply_to_message
        if message.reply_to_message
        else message.text.split(None, 1)[1].strip()
    )
    if not n.isnumeric():
        return await message.reply(f"{ggl}argumen tidak valid")
    n = int(n)
    if n < 1:
        return await message.reply(f"{ggl}butuh nomer 1-999")
    chat_id = message.chat.id
    message_ids = [
        m.id
        async for m in client.search_messages(
            chat_id,
            from_user=int(message.from_user.id),
            limit=n,
        )
    ]
    if not message_ids:
        return await message.reply_text(f"{ggl}tidak ada pesan yang ditemukan")
    to_delete = [message_ids[i : i + 999] for i in range(0, len(message_ids), 999)]
    for hundred_messages_or_less in to_delete:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=hundred_messages_or_less,
            revoke=True,
        )
        mmk = await message.reply(f"{brhsl} {n} pesan telah di hapus")
        await asyncio.sleep(1)
        await mmk.delete()


@PY.UBOT("purge")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    await message.delete()
    if not message.reply_to_message:
        return await message.reply_text(f"{ggl}membalas pesan untuk dibersihka")
    chat_id = message.chat.id
    message_ids = []
    for message_id in range(
        message.reply_to_message.id,
        message.id,
    ):
        message_ids.append(message_id)
        if len(message_ids) == 100:
            await client.delete_messages(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=True,
            )
            message_ids = []
    if len(message_ids) > 0:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=message_ids,
            revoke=True,
        )
