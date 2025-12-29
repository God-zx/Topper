import os

API_ID    = os.environ.get("34943077", "")
API_HASH  = os.environ.get("11aeec678349456f1d190f02975ed89f", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8870))  # Default to 8000 if not set
