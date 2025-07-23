# bot/middleware/force_subscribe.py

from telegram import Update
from telegram.ext import CallbackContext
import requests
from bot.config import API_BASE_URL

def get_required_channels():
    """
    Fetch the list of required channels from API.
    """
    try:
        resp = requests.get(f"{API_BASE_URL}/settings/force_subscribe_channels")
        if resp.status_code == 200:
            return resp.json().get("channels", [])
        return []
    except Exception:
        return []

async def force_subscribe(update: Update, context: CallbackContext):
    """
    Middleware function to ensure user is subscribed to required channels.
    """
    user_id = update.effective_user.id
    channels = get_required_channels()
    if not channels:
        return True  # No channels required

    missing_channels = []
    for channel in channels:
        try:
            member = await context.bot.get_chat_member(channel, user_id)
            if member.status not in ["member", "administrator", "creator"]:
                missing_channels.append(channel)
        except Exception:
            missing_channels.append(channel)

    if missing_channels:
        msg = "বট ব্যবহারের জন্য আপনাকে অবশ্যই নিচের চ্যানেলগুলোতে জয়েন করতে হবে:\n"
        for ch in missing_channels:
            msg += f"👉 {ch}\n"
        await update.effective_message.reply_text(msg, disable_web_page_preview=True)
        return False

    return True
