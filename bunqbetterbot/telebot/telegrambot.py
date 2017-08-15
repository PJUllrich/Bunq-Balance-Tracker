import logging
import os

from telegram.ext import Updater

from conversation.main import Main
from logic.interface import BotInterface

logger = logging.getLogger(__name__)

_WEBHOOK_URL = os.environ['BUNQ_BOT_URL']
_WEBHOOK_PATH = os.environ['BUNQ_BOT_URL_PATH']
_BOT_TOKEN = os.environ['BUNQ_BOT_TOKEN']

_WEBHOOK_PORT = 8525
_WEBHOOK_URLPATH = f'{_WEBHOOK_URL}/{_WEBHOOK_PATH}'


class TelegramBot:
    actions = BotInterface()

    def __init__(self):
        self.updater = Updater(token=_BOT_TOKEN)
        self.dispatcher = self.updater.dispatcher

        self.setup_handlers()

        self.setup_webhook()

    def setup_handlers(self):
        handler_main = Main().handler
        self.dispatcher.add_handler(handler_main)

        self.dispatcher.add_error_handler(self.error)

    def setup_webhook(self):
        self.updater.start_webhook(port=_WEBHOOK_PORT,
                                   url_path=_WEBHOOK_PATH,
                                   webhook_url=_WEBHOOK_URLPATH)
        self.updater.bot.set_webhook(url=_WEBHOOK_URLPATH)
        logger.info(f'Telegram bot is now listening on port {_WEBHOOK_PORT}.')

    def error(self, bot, update, error):
        logger.error(f'Error: {error} caused by Update: {update}')
