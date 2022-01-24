import os
from dotenv import load_dotenv
import telegram
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
from detect_intent import detect_intent_texts


logger = logging.getLogger('tg')

class TelegramLogsHandler(logging.Handler):
    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = tg_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def tg_bot_answer(update: Update, context: CallbackContext) -> None:
    intent = detect_intent_texts(context.bot_data['project_id'], update.message.chat_id, update.message.text, 'ru-RU')
    text = intent.query_result.fulfillment_text
    update.message.reply_text(text)


def main() -> None:
    load_dotenv()
    tg_token = os.getenv('TG_BOT_TOKEN')
    project_id = os.getenv('PROJECT_ID')
    os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

    tg_token_admin = os.getenv('TG_BOT_ADMIN_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    tg_bot = telegram.Bot(token=tg_token_admin)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(TelegramLogsHandler(tg_bot, chat_id))
    logger.info('Бот в ТГ запущен.')

    updater = Updater(tg_token)
    dispatcher = updater.dispatcher
    dispatcher.bot_data = {'project_id': project_id}
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, tg_bot_answer))

    try:
        updater.start_polling()
        updater.idle()
    except Exception:
            logger.exception('Ошибка в ТГ!')


if __name__ == '__main__':
    main()


