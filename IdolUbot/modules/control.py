from IdolUbot import *

__MODULE__ = "control"
__HELP__ = """
<blockquote>Bantuan Untuk Control

perintah : <code>{0}prefix</code>
   untuk merubah prefix/handler perintah

perintah : <code>{0}create & {0}createbot</code>
   untuk membuat group atau channel atau bot

perintah : <code>{0}emoji</code> query emojiprem
   untuk merubah emoji pada tampilan tertentu

query:
    ><code>{0}pong</code>
    ><code>{0}owner</code>
    ><code>{0}ubot</code>
    ><code>{0}gcast</code>
    ><code>{0}sukses</code>
    ><code>{0}gagal</code>
    ><code>{0}proses</code>
    ><code>{0}group</code>
    ><code>{0}catatan</code>
    ><code>{0}afk</code>
    ><code>{0}waktu</code>
    ><code>{0}alasan</code></blockquote>
"""


@PY.UBOT("creat")
@PY.TOP_CMD
async def _(client, message):
    if len(message.command) < 3:
        return await message.reply(
            f"{message.text} [group/channel] [name/titlee]")
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.reply("memproꜱeꜱ...")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "group":
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"berhaꜱil membuat telegram grup: [{group_name}]({link.invite_link})",
            disable_web_page_preview=True,
        )
    elif group_type == "channel":
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"berhaꜱil membuat telegram channel: [{group_name}]({link.invite_link})",
            disable_web_page_preview=True,
        )


@PY.UBOT("prefix")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    Tm = await message.reply(f"{prs}memproses...", quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"{ggl}{message.text} [simbol]")
    else:
        ub_prefix = []
        for prefix in message.command[1:]:
            if prefix.lower() == "threnone":
                ub_prefix.append("")
            else:
                ub_prefix.append(prefix)
        try:
            client.set_prefix(message.from_user.id, ub_prefix)
            await set_pref(message.from_user.id, ub_prefix)
            parsed_prefix = " ".join(f"{prefix}" for prefix in ub_prefix)
            return await Tm.edit(f"{brhsl}  Prefix diatur ke : {parsed_prefix}")
        except Exception as error:
            return await Tm.edit(str(error))

@PY.UBOT("emoji")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    try:
        msg = await message.reply(f"{prs}memproses...", quote=True)

        if not client.me.is_premium:
            return await msg.edit(
                f"{ggl}beli prem dulu anjg"
            )

        if len(message.command) < 3:
            return await msg.edit(f"{ggl}tolong masukkan query dan valeu nya")

        query_mapping = {
          "pong": "EMOJI_PING",
          "owner": "EMOJI_MENTION",
          "ubot": "EMOJI_USERBOT",
          "proses": "EMOJI_PROSES",
          "gcast": "EMOJI_BROADCAST",
          "sukses": "EMOJI_BERHASIL",
          "gagal": "EMOJI_GAGAL",
          "catatan": "EMOJI_KETERANGAN",
          "group": "EMOJI_GROUP",
          "menunggu": "EMOJI_MENUNGGU",
          "alasan": "EMOJI_ALASAN",
          "waktu": "EMOJI_WAKTU",
          "afk": "EMOJI_AFKA",
        }
        command, mapping, value = message.command[:3]

        if mapping.lower() in query_mapping:
            query_var = query_mapping[mapping.lower()]
            emoji_id = None
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break

            if emoji_id:
                await set_vars(client.me.id, query_var, emoji_id)
                await msg.edit(
                    f"{brhsl}emoJi berhasil di setting ke: <emoji id={emoji_id}>{value}</emoji>"
                )
            else:
                await msg.edit(f"{ggl}tidak dapat menemukan emoji premium")
        else:
            await msg.edit(f"{ggl}mapping tidak ditemukan")

    except Exception as error:
        await msg.edit(str(error))


@PY.UBOT("createbot")
@PY.TOP_CMD
async def create_bot_command(client, message):
    # Ambil argumen dari pesan
    args = message.text.split(maxsplit=2)

    if len(args) < 3:
        await message.reply_text(
            "<blockquote><b>⚠️ Gunakan format: createbot [nama_bot] [username_bot]</b></blockquote>\n"
            "Contoh: <code>.createbot MyNewBot MyNew_Bot</code>"
        )
        return

    bot_name = args[1]
    bot_username = args[2]

    if not bot_username.endswith("Bot"):
        await message.reply_text("❌ **Username bot harus diakhiri dengan 'Bot'.**")
        return

    try:
        botfather = "@BotFather"
        
        # Kirim perintah ke BotFather
        await client.send_message(botfather, "/newbot")
        await asyncio.sleep(2)
        await client.send_message(botfather, bot_name)
        await asyncio.sleep(2)
        await client.send_message(botfather, bot_username)

        await message.reply_text(
            f"<blockquote><b>✅ **Permintaan pembuatan bot telah dikirim ke @BotFather!**\n"
            f"🆕 **Nama Bot:** `{bot_name}`\n"
            f"🔗 **Username:** @{bot_username}\n\n"
            "Silakan cek @BotFather untuk melanjutkan proses konfigurasi.</blockquote></b>"
        )
    
    except Exception as e:
        await message.reply_text(f"⚠️ Terjadi kesalahan: {str(e)}")