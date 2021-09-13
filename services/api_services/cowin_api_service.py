import requests
from services.api_services.base import Base
from utils.helper_methods import response_parser
import utils.constants as constants

class CowinApiService(Base):
    def __init__(self):
        print('CowinApiService')

    def find_by_pin(self, pin_code, date):
        try:
            url = constants.find_by_pincode_url.format(pin_code, date)
            response = requests.get(url)
            json_data = response.json()
            print(f"Json data:find_by_pin -> {json_data}")
            return response_parser(json_data)
        except Exception as e:
            print(f"Exception: {e}")
            return self.handle_error(e)

    def calendar_by_district(self, district_id, date):
        try:
            url = constants.calendar_by_district_url.format(district_id, date)
            response = requests.get(url)
            json_data = response.json()
            print(f"Json data:find_by_pin -> {json_data}")
            return response_parser(json_data)
        except Exception as e:
            print(f"Exception: {e}")
            return self.handle_error(e)
