import os
from dotenv import load_dotenv

load_dotenv()

base_url = 'https://cdn-api.co-vin.in'
find_by_pincode_url = base_url + '/api/v2/appointment/sessions/public/findByPin?pincode={0}&date={1}'

bot_url = os.environ['BOT_URL']
telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
parse_mode="Markdown"
pin_codes = [671531, 671532, 671541]
