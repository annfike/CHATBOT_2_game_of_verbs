import os
from dotenv import load_dotenv
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
from detect_intent import detect_intent_texts


logger = logging.getLogger(__file__)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def tg_bot_answer(update: Update, context: CallbackContext, project_id) -> None:
    intent = detect_intent_texts(project_id, update.message.chat_id, update.message.text, 'ru-RU')
    text = intent.query_result.fulfillment_text
    update.message.reply_text(text)


def main() -> None:
    load_dotenv()
    tg_token = os.getenv('TG_BOT_TOKEN')
    project_id = os.getenv('PROJECT_ID')
    os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

    updater = Updater(tg_token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, tg_bot_answer))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


