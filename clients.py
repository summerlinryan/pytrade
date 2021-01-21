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

    def get_charts(self, symbols: List[str], time_frame: Optional[TimeFrame] = TimeFrame.DAILY) -> List[Chart]:
        charts = []
        max_symbols_per_request = 200

        for i, symbols_group in enumerate(partition(symbols, max_symbols_per_request)):
            barsets = self._api.get_barset(symbols_group, time_frame.value)
            for symbol in symbols_group:
                bars = [Bar(bar) for bar in barsets[symbol]]
                charts.append(Chart(symbol, time_frame, bars))

            print(f'Processed symbol partition {i + 1}')

        return charts
