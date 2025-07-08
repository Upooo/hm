from motor.motor_asyncio import AsyncIOMotorClient
from IdolUbot.config import MONGO_URL, NAMA_DB

# Inisialisasi koneksi MongoDB
mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client[NAMA_DB]

# Koleksi (collections)
user_expired_collection = mongodb["users"]
prefix_collection = mongodb["prefix"]
ubot_collection = mongodb["idol"]
vars_collection = mongodb["varsX"]

# Fungsi dari setiap modul (dengan absolute import)
# from IdolUbot.core.database.expired import (
#     get_expired_date,
#     set_expired_date,
#     rem_expired_date,
# )

# from IdolUbot.core.database.pref import (
#     get_pref,
#     set_pref,
#     rem_pref,
# )

# from IdolUbot.core.database.userbot import (
#     add_ubot,
#     remove_ubot,
#     get_userbots,
# )

# from IdolUbot.core.database.variabel import (
#     set_vars,
#     get_vars,
#     remove_vars,
#     all_vars,
#     remove_all_vars,
#     get_list_from_vars,
#     add_to_vars,
#     remove_from_vars,
#     get_pm_id,
#     add_pm_id,
#     remove_pm_id,
#     set_status,
#     get_status,
# )

# daftar semua yang bisa diakses langsung
# __all__ = [
#     # MongoDB
#     "mongo_client",
#     "mongodb",
#     "user_expired_collection",
#     "prefix_collection",
#     "ubot_collection",
#     "vars_collection",

#     # expired.py
#     "get_expired_date",
#     "set_expired_date",
#     "rem_expired_date",

#     # pref.py
#     "get_pref",
#     "set_pref",
#     "rem_pref",

#     # userbot.py
#     "add_ubot",
#     "remove_ubot",
#     "get_userbots",

#     # variabel.py
#     "set_vars",
#     "get_vars",
#     "remove_vars",
#     "all_vars",
#     "remove_all_vars",
#     "get_list_from_vars",
#     "add_to_vars",
#     "remove_from_vars",
#     "get_pm_id",
#     "add_pm_id",
#     "remove_pm_id",
#     "set_status",
#     "get_status",
# ]
