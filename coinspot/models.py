"""
Portfolio models.
"""


class Asset:

    def __init__(self, coin, balance, aud_value):
        self.coin = coin
        self.balance = balance
        self.aud_value = aud_value