import os
from dotenv import load_dotenv

load_dotenv(".env")

API_ID = int(os.getenv("API_ID", "20124949"))
API_HASH = os.getenv("API_HASH", "ff39880b27afecc7b5063766a78591db")

BOT_TOKEN = os.getenv("BOT_TOKEN")
MAX_BOT = int(os.getenv("MAX_BOT", "30"))

DEVS = list(map(int, os.getenv("DEVS", "7500830844").split()))
OWNER_ID = int(os.getenv("OWNER_ID", "7500830844"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002580967407").split()))
LOGS_MAKER_UBOT = list(map(int, os.getenv("LOGS_MAKER_UBOT", "-1002864434436").split()))
LOGS_ON_UBOT = int(os.getenv("LOGS_ON_UBOT", "-1002580967407"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL")
NAMA_DB = os.getenv("NAMA_DB", "IdolGacor")





# IDOL ID
DEK_ANAT = 5060242603
PIRA_BIDUAN = 1760398550
SAIKO_SAHABAT = 6244458400
ASHEL_SLEBEW = 7650569132

IDOL_GACOL = [
    DEK_ANAT,
    PIRA_BIDUAN,
    SAIKO_SAHABAT,
    ASHEL_SLEBEW
]
