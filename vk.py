import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api as vk
import os
from dotenv import load_dotenv
import random
from detect_intent import detect_intent_texts
import telegram
import logging


logger = logging.getLogger('vk')

class TelegramLogsHandler(logging.Handler):
    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = tg_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def vk_bot_answer(event, vk_api, project_id):
    intent = detect_intent_texts(project_id, event.user_id, event.text, 'ru-RU')
    if not intent.query_result.intent.is_fallback:
        text = intent.query_result.fulfillment_text
        vk_api.messages.send(
            user_id=event.user_id,
            message=text,
            random_id=random.randint(1,1000)
        )


if __name__ == '__main__':
    load_dotenv()
    vk_token = os.getenv('VK_TOKEN')
    project_id = os.getenv('PROJECT_ID')
    os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

    tg_token_admin = os.getenv('TG_BOT_ADMIN_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    tg_bot = telegram.Bot(token=tg_token_admin)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(TelegramLogsHandler(tg_bot, chat_id))
    logger.info('Бот в VK запущен.')

    try:
        vk_session = vk.VkApi(token=vk_token)
        vk_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                vk_bot_answer(event, vk_api, project_id)
    except Exception:
            logger.exception('Ошибка в VK!')
