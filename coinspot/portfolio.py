"""
Portfolio processing module.
"""


class Portfolio:

    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)