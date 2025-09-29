"""
Telegram Bot
-----------
A simple Telegram bot that responds to /start, /help, and text messages.
Author: SB1450
"""
import os
import telebot
from dotenv import load_dotenv
import logging

# ---------------------- Bot Configuration ----------------------
# Configure logging for debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = os.getenv("ADMIN_IDS")

# Initialize the bot
bot = telebot.TeleBot(TOKEN)


# ---------------------- Message Handlers ----------------------
# Handle /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f"Hello {user_name}! Welcome to my bot. How can I assist you?")

# Handle text messages
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.reply_to(message, "I received your message! Currently, I only respond to text.")

# Handle Admin/s user/s
@bot.message_handler(commands=['admin'])
def admin_command(message):
    if message.from_user.id in ADMIN_IDS:
        bot.reply_to(message, "Welcome Admin!")
    else:
        bot.reply_to(message, "You don't have access to this function")


# ---------------------- Main Function ----------------------
if __name__ == "__main__":
    try:
        logger.info("Starting bot...")
        bot.infinity_polling(timeout=20, long_polling_timeout=5)
    except Exception as e:
        logger.error(f"Bot crashed: {e}")