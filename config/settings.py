from dotenv import load_dotenv
import os

load_dotenv()

COINSPOT_API_KEY = os.getenv("COINSPOT_API_KEY")
COINSPOT_API_SECRET = os.getenv("COINSPOT_API_SECRET")


def check_settings():
    if COINSPOT_API_KEY and COINSPOT_API_SECRET:
        return True
    return False