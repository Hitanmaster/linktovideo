# telegram_bot.py
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

bot_token = '6163881554:AAFg-PjrEpDht6Hq0lfPNOLja4utgoa5hk0'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send me a video download link, and I will send it back to you.')

def handle_text(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text
    
    if message_text.startswith('http') or message_text.startswith('www'):
        response = requests.get(message_text)
        update.message.reply_video(video=response.content, supports_streaming=True)
    else:
        update.message.reply_text('Invalid URL. Please send a valid video download link.')

def main() -> None:
    updater = Updater(token=bot_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
