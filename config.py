import os
from os import getenv
from dotenv import load_dotenv

# Load .env if running locally
if os.path.exists("local.env"):
    load_dotenv("local.env")

# --- Required / Important Configs with fallback or validation ---

# API_ID must be an integer
api_id = getenv("API_ID", "27079591")
if not api_id.isdigit():
    raise ValueError("API_ID is missing or not a valid integer.")
API_ID = int(api_id)

# API_HASH can be empty but ideally should be set
API_HASH = getenv("API_HASH", "c81ae4c3dc026ea4bf49842a8ce4a5f9")

# OWNER_ID must be an integer
owner_id = getenv("OWNER_ID")
if not owner_id or not owner_id.isdigit():
    raise ValueError("OWNER_ID is missing or not a valid integer.")
OWNER_ID = int(owner_id)

# SUDO_USERS must be a list of integers
SUDO_USERS = list(map(int, getenv("SUDO_USERS", str(OWNER_ID)).split()))

# MongoDB URL
MONGO_URL = getenv("MONGO_URL")
if not MONGO_URL:
    raise ValueError("MONGO_URL is missing.")

# Bot token
BOT_TOKEN = getenv("BOT_TOKEN", "")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing.")

# --- Optional Configs with fallback defaults ---

ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/5badd2112e1e0cdf03a1f.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "✨ I'm alive and ready to vibe!")
PM_LOGGER = getenv("PM_LOGGER", "")
LOG_GROUP = getenv("LOG_GROUP", "")

GIT_TOKEN = getenv("GIT_TOKEN", "")  # GitHub personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/TEAMPURVI/ALPHA_USERBOT")
BRANCH = getenv("BRANCH", "main")

# --- String Sessions (10 slots) ---

STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
