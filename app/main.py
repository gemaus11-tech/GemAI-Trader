from app.banner import show_banner
from coinspot.client import CoinSpotClient
from config.settings import check_settings


def main():
    show_banner()

    if check_settings():
        print("✅ API credentials loaded")
    else:
        print("❌ API credentials not found")
        return

    print()

    client = CoinSpotClient()
    client.check_connection()

    print()
    print("Status: READ ONLY")
    print("Next step: Retrieve portfolio")


if __name__ == "__main__":
    main()
