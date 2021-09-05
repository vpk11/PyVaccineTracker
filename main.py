from services.cowin_service import CowinService
import utils.constants as constants

def main():
    CowinService(constants.pin_code).publish_pin_search_to_telegram()

if __name__ == "__main__":
    main()
