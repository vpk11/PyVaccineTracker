from services.cowin_service import CowinService

def main():
    CowinService(671532).publish_pin_search_to_telegram()

if __name__ == "__main__":
    main()
