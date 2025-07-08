import asyncio

from pyrogram.enums import UserStatus

from IdolUbot import *

__MODULE__ = "invite"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪɴᴠɪᴛᴇ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}invite</code> [username/id]
🦠 ᴋᴇᴛ : ᴍᴇɴɢᴜɴᴅᴀɴɢ sᴀᴛᴜ ᴀɴɢɢᴏᴛᴀ ᴋᴇ ɢʀᴏᴜᴘ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}inviteall</code> [username_gc/id_gc] [delay]
🦠 ᴋᴇᴛ : ᴍᴇɴɢᴜɴᴅᴀɴɢ sᴇᴍᴜᴀ ᴀɴɢɢᴏᴛᴀ ᴀᴋᴛɪꜰ ᴅᴀʀɪ ɢʀᴏᴜᴘ ʟᴀɪɴ ᴅᴇɴɢᴀɴ ᴊᴇᴅᴀ ʙᴇʀᴅᴀꜱᴀʀᴋᴀɴ delay.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}cancel</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢʜᴇɴᴛɪᴋᴀɴ ᴘʀᴏꜱᴇꜱ <code>inviteall</code> ʏᴀɴɢ sᴇᴅᴀɴɢ ʙᴇʀᴊᴀʟᴀɴ.</b></blockquote>
"""



@PY.UBOT("invite")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    mg = await message.reply(f"{prs}menambahkan pengguna!")
    if len(message.command) < 2:
        return await mg.delete()
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit(
            f"{ktrng}beri saya pengguna untuk ditambahkan!\nperiksa menu bantuan untuk info lebih lanjut!"
        )
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except Exception as e:
        return await mg.edit(f"{e}")
    await mg.edit(f"{brhsl}berhasil ditambahkan {len(user_list)} ke grup ini")



invite_id = []

@PY.UBOT("inviteall")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)

    Tm = await message.reply(f"{prs}processing . . .")
    if len(message.command) < 3:
        await message.delete()
        return await Tm.delete()

    try:
        chat = await client.get_chat(message.command[1])
    except Exception as error:
        return await Tm.edit(f"{ggl} {error}")

    if message.chat.id in invite_id:
        return await Tm.edit_text(
            f"{ktrng}Sedang menginvite member.\nGunakan perintah <code>cancel</code> untuk membatalkan."
        )

    done, failed = 0, 0
    invite_id.append(message.chat.id)

    await Tm.edit_text(f"{prs}Mengundang anggota dari {chat.title}...")

    try:
        async for member in client.get_chat_members(chat.id):
            if member.user.status in [
                UserStatus.ONLINE,
                UserStatus.OFFLINE,
                UserStatus.RECENTLY,
                UserStatus.LAST_WEEK,
            ]:
                try:
                    await client.add_chat_members(message.chat.id, member.user.id)
                    done += 1
                except Exception:
                    failed += 1
                await asyncio.sleep(int(message.command[2]))
    except Exception as e:
        await Tm.edit(f"{ggl} Error: {e}")
        invite_id.remove(message.chat.id)
        return

    invite_id.remove(message.chat.id)
    await Tm.delete()

    await message.reply(
        f"""
{brhsl} {done} anggota berhasil diundang.
{ggl} {failed} anggota gagal diundang.
"""
    )


@PY.UBOT("cancel")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    if message.chat.id not in invite_id:
        return await message.reply_text("🚫 Tidak ada proses <code>inviteall</code> yang sedang berjalan.")
    try:
        invite_id.remove(message.chat.id)
        await message.reply_text("✅ Perintah <code>inviteall</code> berhasil dibatalkan.")
    except Exception as e:
        await message.reply_text(f"⚠️ Gagal membatalkan: {e}")
