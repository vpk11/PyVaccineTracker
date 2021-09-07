from services.cowin_service import CowinService
import utils.constants as constants

def main():
    for pin_code in constants.pin_codes:
        CowinService(pin_code).publish_pin_search_to_telegram()

if __name__ == "__main__":
    main()
