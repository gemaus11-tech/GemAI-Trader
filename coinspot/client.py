import requests
from rich import print

class CoinSpotClient:
    def __init__(self):
        self.base_url = "https://www.coinspot.com.au"

    def check_connection(self):
        print("[green]✓ CoinSpot client created successfully[/green]")
        print(f"Base URL: {self.base_url}")