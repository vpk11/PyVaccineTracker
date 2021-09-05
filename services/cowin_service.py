from models.session import Session
from services.telegram_service import TelegramSerivce as Telegram
from services.api_services.cowin_api_service import CowinApiService
from datetime import datetime, timedelta
from utils.helper_methods import resolve_find_by_pin_tg_messages

class CowinService(object):
    def __init__(self, pin_code):
        self.pin_code = pin_code
    
    def publish_pin_search_to_telegram(self):
        cowin_api_service = CowinApiService()
        today = datetime.today().strftime("%d-%m-%Y")
        tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d-%m-%Y")
        day_after_tomorrow = (datetime.today() + timedelta(days=2)).strftime("%d-%m-%Y")
        for date in [today, tomorrow, day_after_tomorrow]:
            data = cowin_api_service.find_by_pin(self.pin_code, date)
            messages = resolve_find_by_pin_tg_messages(data)
            telegram = Telegram()
            if not messages:
                telegram.publish(f"*{date}*: No Slots Availbale")
            else:
                for message in messages:
                    telegram.publish(message)

        return True
