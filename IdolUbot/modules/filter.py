from IdolUbot import *

# Ekstrak nama filter dan pesan yang dibalas
def extract_type_and_msg(message):
    args = message.text.split(None, 2)
    if len(args) < 2:
        return None, None
    type_name = args[1]
    reply_msg = message.reply_to_message
    return type_name, reply_msg

@PY.NO_CMD_UBOT("FILTER_MSG", ubot)
async def filter_message(client, message):
    try:
        chat_logs = await get_vars(client.me.id, "ID_LOGS")
        all_filters = await all_vars(client.me.id, "FILTERS") or {}

        for key, value in all_filters.items():
            if key == message.text.split()[0]:
                msg = await client.get_messages(int(chat_logs), int(value))
                return await msg.copy(message.chat.id, reply_to_message_id=message.id)
    except Exception:
        pass

@PY.UBOT("filter")
@PY.TOP_CMD
async def filter_cmd(client, message):
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.BERHASIL(client)
    txt = await message.reply(f"{proses} Sedang memproses")
    arg = get_arg(message)

    if not arg or arg.lower() not in ["off", "on"]:
        return await txt.edit(f"{gagal} harap baca menu bantuan terlebih dahulu")

    state = True if arg.lower() == "on" else False
    await set_vars(client.me.id, "FILTER_ON_OFF", state)
    return await txt.edit(f"{sukses} filters berhasil diaktifkan: <b>{state}</b>")

@PY.UBOT("addfilter")
@PY.TOP_CMD
async def addfilter_cmd(client, message):
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.BERHASIL(client)
    txt = await message.reply(f"{proses} Sedang memproses")

    type_name, reply_msg = extract_type_and_msg(message)

    if not type_name or not reply_msg:
        return await txt.edit(f"{gagal} Balas pesan dan beri nama filter!\nContoh: <code>.addfilter salam</code> (dengan reply)")

    logs = await get_vars(client.me.id, "ID_LOGS")
    if not logs:
        return await txt.edit(f"{gagal} Logs belum diaktifkan!")

    try:
        copied = await reply_msg.copy(int(logs))
        await set_vars(client.me.id, type_name, copied.id, "FILTERS")
        await txt.edit(f"{sukses} Filter <b>{type_name}</b> berhasil disimpan.")
    except Exception as e:
        await txt.edit(f"{gagal} Gagal menyimpan filter:\n<code>{e}</code>")

@PY.UBOT("delfilter")
@PY.TOP_CMD
async def delfilter_cmd(client, message):
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.BERHASIL(client)
    txt = await message.reply(f"{proses} Tunggu sebentar...")
    arg = get_arg(message)

    if not arg:
        return await txt.edit(f"{gagal} Gunakan: <code>.delfilter nama_filter</code>")

    logs = await get_vars(client.me.id, "ID_LOGS")
    all = await all_vars(client.me.id, "FILTERS")

    if arg not in all:
        return await txt.edit(f"{gagal} Filter <b>{arg}</b> tidak ditemukan.")

    try:
        await remove_vars(client.me.id, arg, "FILTERS")
        await client.delete_messages(int(logs), int(all[arg]))
        await txt.edit(f"{sukses} Filter <b>{arg}</b> berhasil dihapus.")
    except Exception as e:
        await txt.edit(f"{gagal} Gagal menghapus filter:\n<code>{e}</code>")

@PY.UBOT("filters")
@PY.TOP_CMD
async def filters_cmd(client, message):
    vars = await all_vars(client.me.id, "FILTERS")
    if vars:
        alasan = await EMO.ALASAN(client)
        msg = f"<b>{alasan} ᴅᴀғᴛᴀʀ ғɪʟᴛᴇʀs:</b>\n"
        for x in vars.keys():
            msg += f"<b> ├ <code>{x}</code></b>\n"
        msg += f"<b> ╰ ᴛᴏᴛᴀʟ ғɪʟᴛᴇʀs: {len(vars)}</b>"
    else:
        gagal = await EMO.GAGAL(client)
        msg = f"<b>{gagal} Tidak ada filters yang tersimpan.</b>"

    return await message.reply(msg, quote=True)
