from motor.motor_asyncio import AsyncIOMotorClient

from IdolUbot.config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client.idoluserbot #GANTI

from IdolUbot.core.database.expired import *
from IdolUbot.core.database.userbot import *
from IdolUbot.core.database.pref import *
from IdolUbot.core.database.variabel import *