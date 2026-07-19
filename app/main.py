from app.banner import show_banner
from coinspot.client import CoinSpotClient
from config.settings import check_settings
from app.dashboard import show_dashboard

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

show_dashboard()

print()
print("Status: READ ONLY")
print("Next step: Retrieve portfolio")