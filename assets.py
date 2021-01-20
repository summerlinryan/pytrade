from enum import Enum
from typing import List

import alpaca_trade_api
import alpaca_trade_api.entity


class TimeFrame(Enum):
    MINUTE = '1Min'
    FIVE_MINUTE = '5Min'
    FIFTEEN_MINUTE = '15Min'
    DAILY = '1D'


class Bar:
    open: float
    high: float
    low: float
    close: float
    volume: float
    time: int

    def __init__(self, bar):
        self.open = bar.o
        self.high = bar.h
        self.low = bar.l
        self.close = bar.c
        self.volume = bar.v
        self.time = bar.t

    @property
    def is_green(self):
        return self.close > self.open

    @property
    def is_red(self):
        return self.close < self.open


class Asset:
    api: alpaca_trade_api.REST
    asset: alpaca_trade_api.entity.Asset

    def __init__(self, symbol: str):
        self.api = alpaca_trade_api.REST()
        self.asset = self.api.get_asset(symbol)

    def get_chart(self, time_frame: TimeFrame):
        bars = [Bar(bar) for bar in (self.api.get_barset(
            symbols=[self.asset.symbol],
            timeframe=time_frame.value,
        )[self.asset.symbol])]

        return Chart(bars)

    @property
    def symbol(self):
        return self.asset.symbol


class Chart:
    bars: List[Bar]

    def __init__(self, bars: List[Bar]):
        self.bars = bars

    @property
    def last_percent_change(self) -> float:
        return (self.bars[-1].close - self.bars[-2].close) / self.bars[-2].close
