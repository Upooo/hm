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


from IdolUbot.core.database.expired import *
from IdolUbot.core.database.userbot import *
from IdolUbot.core.database.pref import *
from IdolUbot.core.database.variabel import *