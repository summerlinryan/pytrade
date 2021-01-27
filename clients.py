from typing import List, Optional

import alpaca_trade_api
import alpaca_trade_api.entity

from assets import Chart, TimeFrame, Bar, Asset
from utilities import partition


class AssetClient:
    _api: alpaca_trade_api.REST

    def __init__(self):
        self._api = alpaca_trade_api.REST()

    def get_available_assets(self) -> List[Asset]:
        return [Asset(asset) for asset in self._api.list_assets()
                if asset.status == 'active' and asset.tradable]

    def get_charts(self, assets: List[Asset], time_frame: Optional[TimeFrame] = TimeFrame.DAILY) -> List[Chart]:
        charts = []
        max_assets_per_request = 200

        for i, assets_partition in enumerate(partition(assets, max_assets_per_request)):
            barsets = self._api.get_barset([asset.symbol for asset in assets_partition], time_frame.value)

            for asset in assets_partition:
                bars = [Bar(bar) for bar in barsets[asset.symbol]]
                charts.append(Chart(asset, time_frame, bars))

            print(f'Processed asset partition {i + 1}')

        return charts
