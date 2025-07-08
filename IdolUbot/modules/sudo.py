__MODULE__ = "sudo"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴜᴅᴏ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}addsudo</code> [@username/user_id/reply]
🦠 ᴋᴇᴛ : ᴍᴇɴᴀᴍʙᴀʜ ᴘᴇɴɢɢᴜɴᴀ ᴋᴇ ᴅᴀʟᴀᴍ sᴜᴅᴏ ʟɪsᴛ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}delsudo</code> [@username/user_id/reply]
🦠 ᴋᴇᴛ : ᴍᴇɴɢʜᴀᴘᴜs ᴘᴇɴɢɢᴜɴᴀ ᴅᴀʀɪ sᴜᴅᴏ ʟɪsᴛ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}sudolist</code>
🦠 ᴋᴇᴛ : ᴍᴇʟɪʜᴀᴛ ᴅᴀғᴛᴀʀ sᴜᴅᴏ ʏᴀɴɢ ᴀᴋᴛɪꜰ.</blockquote>
"""



import asyncio

from pyrogram.enums import *
from pyrogram.errors import FloodWait
from pyrogram.types import *

from IdolUbot import *

@PY.UBOT("addsudo")
async def _(client, message):
    msg = await message.reply("⏳ Tunggu Sebentar. . .")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit("📚 Gunakan Perintah: .addsudo [@username] .addsudo [user_id] .addsudo [balas_pengguna]")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(f"Error: {error}")

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USER", "ID_NYA") or []
    
    if user.id in sudo_users:
        return await msg.edit(f"{user.first_name} sudah menjadi pengguna sudo.")

    try:
        await add_to_vars(client.me.id, "SUDO_USER", user.id, "ID_NYA")
        return await msg.edit(f"{user.first_name} berhasil ditambahkan sebagai pengguna sudo.")
    except Exception as error:
        return await msg.edit(f"Error: {error}")

@PY.UBOT("delsudo")
async def _(client, message):
    msg = await message.reply("⏳ Tunggu Sebentar. . .")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit("📚 Gunakan Perintah: .delsudo [@username] .delsudo [user_id] .delsudo [balas_pengguna]")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(f"Error: {error}")

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USER", "ID_NYA") or []
    
    if user.id not in sudo_users:
        return await msg.edit(f"{user.first_name} bukan bagian dari pengguna sudo.")

    try:
        await remove_from_vars(client.me.id, "SUDO_USER", user.id, "ID_NYA")
        return await msg.edit(f"{user.first_name} berhasil dihapus dari daftar pengguna sudo.")
    except Exception as error:
        return await msg.edit(f"Error: {error}")

@PY.UBOT("sudolist")
async def _(client, message):
    msg = await message.reply("Processing...")
    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USER", "ID_NYA") or []

    if not sudo_users:
        return await msg.edit("Tidak ada pengguna sudo ditemukan.")

    sudo_list = []
    for user_id in sudo_users:
        try:
            user = await client.get_users(int(user_id))
            sudo_list.append(f" • {user.first_name} | {user.id}")
        except:
            continue

    response = f"Daftar Pengguna Sudo:\n" + "\n".join(sudo_list)
    return await msg.edit(response)
