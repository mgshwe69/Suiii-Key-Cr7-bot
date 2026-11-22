import os
import secrets
from datetime import datetime, timedelta, timezone
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes, ConversationHandler
)
from supabase import create_client, Client
from flask import Flask
import threading

# --- RENDER KEEP-ALIVE SERVER ---
web_app = Flask(__name__)

@web_app.route('/')
def health():
    return "Bot is alive", 200

def run_web():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host="0.0.0.0", port=port)
# -------------------------------

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
BOT_TOKEN = os.getenv("BOT_TOKEN")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

ASK_KEY_NAME, ASK_EXTEND_DAYS, ASK_DEVICE_LIMIT, CONFIRM_DELETE = range(4)

# ... (BAAKI KA SAARA PURANA CODE YAHAN SAME RAHEGA) ...
