from IdolUbot import *
from datetime import datetime, timedelta

#Callback handler untuk tombol free trial
@PY.CALLBACK("trial_ubot")
async def free_trial_callback(client, callback_query):
    user_id = callback_query.from_user.id

    # Cek apakah user sudah pernah mendapat premium gratis
    free_users = await get_list_from_vars(client.me.id, "FREE_PREM_USERS")
    if user_id in free_users:
        return await callback_query.answer("❌ eh lu siapa. tolol. enak banemget mau make akses trial gua kan 1 kali untuk 1 orang", show_alert=True)

    # Tambahkan 1 hari premium
    now = datetime.now(timezone("Asia/Jakarta"))
    expired = now + timedelta(hours=12)

    await set_expired_date(user_id, expired)
    await add_to_vars(client.me.id, "PREM_USERS", user_id)
    await add_to_vars(client.me.id, "FREE_PREM_USERS", user_id)

    # Kirim pesan ke user dengan status free trial
    await callback_query.answer("✅ Anda mendapatkan akses free trial selama 1 hari!", show_alert=True)
    
    # Kirim pesan dengan tombol inline
    buttons = [
        [InlineKeyboardButton("⦪ ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ⳼", callback_data="buat_ubot")],
    ]
    await bot.send_message(
        user_id,
        f"""
<blockquote><b>✅ Akses free trial selama 1 hari telah diaktifkan!</b>

<b>💬 Dengan akses ini, Anda sekarang dapat membuat Userbot Anda sendiri.</b></blockquote>
""",
        reply_markup=InlineKeyboardMarkup(buttons),
  )
  
