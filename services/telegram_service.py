import requests
import utils.constants as constants


class TelegramSerivce(object):
    def __init__(self):
        print('TelegramSerivce')

    def publish(self, message):
        print(f"message: {message}")
        payload = {'chat_id': constants.telegram_chat_id,
                   'text': message, 'parse_mode': constants.parse_mode}
        requests.post(constants.bot_url, params=payload)
